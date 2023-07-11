import numpy as np

class Detector_block:

    symbol_time = None
    Ts = None
    beta = None 
    alpha = None
    symbol_block_len = None
    representative_class = None
    responsivity = None
    sigma2_sh = None
    sigma2_th = None
    __means_y__ = None
    __vars_y__ = None
    __means_z__ = None
    __vars_z__ = None


    def __init__(self, symbol_time, Ts, beta, symbol_block_len, responsivity, sigma2_sh, sigma2_th):
        self.symbol_time = symbol_time
        self.Ts = Ts
        self.beta = beta
        self.alpha2 = 4/(4-self.beta)
        self.symbol_block_len = symbol_block_len
        self.responsivity = responsivity
        self.sigma2_sh = sigma2_sh
        self.sigma2_th = sigma2_th
        
    def set_representative_class(self,representative_class):
        self.representative_class = representative_class
        power_x = np.square(np.abs(self.representative_class))
        self.__means_y__ = self.responsivity*self.alpha2*(1-self.beta)*self.symbol_time*power_x
        self.__vars_y__ = ((1-self.beta)*self.symbol_time)*self.Ts*(self.alpha2*power_x*self.sigma2_sh+self.sigma2_th)
        phi = (1/4*np.square(np.abs(self.representative_class[:,:-1]+self.representative_class[:,1:]))
               +1/8*np.square(np.abs(self.representative_class[:,:-1]-self.representative_class[:,1:])))
        self.__means_z__ = self.responsivity*self.alpha2*self.beta*self.symbol_time*phi
        self.__vars_z__ = (self.beta*self.symbol_time)*self.Ts*(self.alpha2*phi*self.sigma2_sh+self.sigma2_th)


    def decode_loglikelihood(self,y,z,num_sym_blocks):
        y = np.reshape(y,(num_sym_blocks,self.symbol_block_len))
        z = np.reshape(z,(num_sym_blocks,self.symbol_block_len))
        z = z[:,:-1]
        xd = self.loglikelihood_y_z_given_xd(y,z)
        return np.argmin(xd, axis=1)

    def loglikelihood_y_z_given_xd(self,ys,zs):
        return [np.sum(self.loglikelihood_yk_given_xk(y), axis=1)+np.sum(self.loglikelihood_zl_given_xl_xl1(z), axis=1) for y,z in zip(ys,zs)]
    
    def loglikelihood_yk_given_xk(self,y): 
        return self.log_norm_dist(y, means=self.__means_y__, vars=self.__vars_y__)
    
    def loglikelihood_zl_given_xl_xl1(self,z):
        return self.log_norm_dist(z, means=self.__means_z__, vars=self.__vars_z__)
    
    def log_norm_dist(self, x, means, vars):
        return [np.log(var) + (x-mean)**2/var for mean,var in zip(means,vars)]
    
    def decode_likelihood(self,y,z,num_sym_blocks):
        y = np.reshape(y,(num_sym_blocks,self.symbol_block_len))
        z = np.reshape(z,(num_sym_blocks,self.symbol_block_len))
        z = z[:,:-1]
        xd = self.likelihood_y_z_given_xd(y,z)
        #print(xd)
        return np.argmax(xd, axis=1)

    def likelihood_y_z_given_xd(self,ys,zs):
        return [np.prod(self.likelihood_yk_given_xk(y), axis=1)*np.prod(self.likelihood_zl_given_xl_xl1(z), axis=1) for y,z in zip(ys,zs)]
    
    def likelihood_yk_given_xk(self,y): 
        return self.norm_dist(y, means=self.__means_y__, vars=self.__vars_y__)
    
    def likelihood_zl_given_xl_xl1(self,z):
        return self.norm_dist(z, means=self.__means_z__, vars=self.__vars_z__)
    
    def norm_dist(self, x, means, vars):
        return [1/np.sqrt(2*np.pi*var)*np.exp(-(x-mean)**2/(2*var)) for mean,var in zip(means,vars)]