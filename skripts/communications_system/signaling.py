import numpy as np

class Signaling_block:
    
    symbol_time = None
    sps = None
    fs = None
    Ts = None
    
    window_len = None
    beta = None
    time_vec = None
    tukey_window = None
    
    
    def __init__(self, symbol_time=1, sps=10, beta=0.5, adjust_beta=True):
        self.symbol_time = symbol_time
        self.sps = sps
        self.beta = beta
        self.fs = (sps-1)/symbol_time
        self.Ts = 1/self.fs
        if round((1+beta)*(sps-1)) != (1+beta)*(sps-1):
            print("the choosed beta is not the most apropiate\n"+
                  "time duration of the window do not match a sample point")
            if adjust_beta: 
                self.adjust_beta()
        self.calc_time_vec()
        self.window_len = len(self.time_vec)
        self.calc_tukey_window()
        
    def adjust_beta(self):
        print("original beta: {}".format(self.beta))
        if self.sps % 2:
            n = round(((1+self.beta)*(self.sps-1)-1)/2)
            self.beta = (2*n+1)/(self.sps-1)-1
        else:
            n = round((1+self.beta)*(self.sps-1))
            self.beta = n/(self.sps-1)-1
        print("beta was set to {}".format(self.beta))

    def calc_time_vec(self):
        if self.sps % 2:
            t_pos = np.arange(start=0, stop=self.symbol_time*(1+self.beta)/2+self.Ts, step=self.Ts)
            self.time_vec = np.append(-t_pos[-1:0:-1],t_pos)
        else:
            t_pos = np.arange(start=self.Ts/2, stop=self.symbol_time*(1+self.beta)/2, step=self.Ts)
            self.time_vec = np.append(-t_pos[-1::-1],t_pos)
        if self.time_vec[-1]>(1+self.beta)*self.symbol_time/2:
            self.time_vec = self.time_vec[1:-1]
    
    def calc_tukey_window(self):
        self.tukey_window = np.ones(self.window_len)
        indx = np.where(np.abs(np.abs(self.time_vec/self.symbol_time)-1/2) <= self.beta/2)
        self.tukey_window[indx] = 1/2*(1-np.sin(np.pi*(2*np.abs(self.time_vec[indx]/self.symbol_time)-1)/(2*self.beta)))
        self.tukey_window *= 2/np.sqrt(4-self.beta)*(abs(self.time_vec) < self.symbol_time*(1+self.beta)/2)

    def generate_signal(self, symbols):
        symbols_up_samp = np.zeros((len(symbols)-1)*(self.sps-1)+1, dtype=complex)
        symbols_up_samp[::self.sps-1] = symbols
        return np.convolve(symbols_up_samp,self.tukey_window)
    