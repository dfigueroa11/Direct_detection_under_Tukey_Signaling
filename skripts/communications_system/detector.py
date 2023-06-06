import numpy as np

class Detector_block:

    symbol_time = None
    beta = None 
    alpha = None
    symbol_block_len = None
    representative_class = None
    responsivity = None
    sigma2_sh = None
    sigma2_th = None

    def __init__(self, symbol_time, beta, symbol_block_len, representative_class, responsivity, sigma2_sh, sigma2_th):
        self.symbol_time = symbol_time
        self.beta = beta
        self.alpha2 = 4/(4-self.beta)
        self.symbol_block_len = symbol_block_len
        self.representative_class = representative_class
        self.responsivity = responsivity
        self.sigma2_sh = sigma2_sh
        self.sigma2_th = sigma2_th

    def decode(self,y,z,num_sym_blocks):
        k_hat = -np.ones(num_sym_blocks, dtype=int)
        for rx_sym_block in range(num_sym_blocks):
            max_liklyhood = 0
            for k_ML,sym_block in enumerate(self.representative_class):
                liklyhood = self.liklyhood_y_z_given_xd(y[self.symbol_block_len*rx_sym_block:self.symbol_block_len*(rx_sym_block+1)],
                                                        z[self.symbol_block_len*rx_sym_block:self.symbol_block_len*(rx_sym_block+1)-1],
                                                        sym_block)
                if liklyhood > max_liklyhood:
                    max_liklyhood = liklyhood
                    k_hat[rx_sym_block] = k_ML
        return k_hat

    def liklyhood_y_z_given_xd(self,y,z,sym_block):
        return np.prod(self.liklyhood_yk_given_xk(y,sym_block))*np.prod(self.liklyhood_zl_given_xl_xl1(z,sym_block))
    
    def liklyhood_yk_given_xk(self,y,sym_block):
        norm_x = np.abs(sym_block)**2
        return self.norm_dist(y, mean=self.alpha2*(1-self.beta)*self.symbol_time*norm_x,
                              var=(1-self.beta)*self.symbol_time*(self.alpha2*norm_x+self.sigma2_sh+self.sigma2_th))
    
    def liklyhood_zl_given_xl_xl1(self,z,sym_block):
        phi = 1/4*np.abs(sym_block[:-1]+sym_block[1:])**2 + 1/8*np.abs(sym_block[:-1]-sym_block[1:])**2
        return self.norm_dist(z, mean=self.alpha2*self.beta*self.symbol_time*phi,
                                var=self.beta*self.symbol_time*(self.alpha2*phi+self.sigma2_sh+self.sigma2_th))
    
    def norm_dist(self, x, mean, var):
        return 1/np.sqrt(2*np.pi*var)*np.exp(-(x-mean)**2/(2*var))