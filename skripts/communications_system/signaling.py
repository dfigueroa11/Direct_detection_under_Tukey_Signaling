import numpy as np
import scipy.signal as sig

class Signaling_block:
    
    symbol_time = None
    sps = None
    fs = None
    Ts = None
    
    window_len = None
    beta = None
    time_vec = None
    tukey_window = None
    
    
    def __init__(self, symbol_time=1, sps=10, beta=0.5):
        self.symbol_time = symbol_time
        self.sps = sps
        self.beta = beta
        self.support_time = symbol_time*(1+beta)
        self.fs = (sps-1)/symbol_time
        self.Ts = 1/self.fs
        self.calc_time_vec()
        self.window_len = len(self.time_vec)
        self.calc_tukey_window()
        
    def calc_time_vec(self):
        
        if self.sps % 2:
            t_pos = np.arange(start=0, stop=self.symbol_time*(1+self.beta)/2+self.Ts, step=self.Ts)
            self.time_vec = np.append(-t_pos[-1:0:-1],t_pos)
        else:
            t_pos = np.arange(start=self.Ts/2, stop=self.symbol_time*(1+self.beta)/2, step=self.Ts)
            self.time_vec = np.append(-t_pos[-1::-1],t_pos)
    
    def calc_tukey_window(self):
        self.tukey_window = np.ones(self.window_len)
        indx = np.where(np.abs(np.abs(self.time_vec/self.symbol_time)-1/2) - self.beta/2 <= 1e-7)
        self.tukey_window[indx] = 1/2*(1-np.sin(np.pi*(2*np.abs(self.time_vec[indx]/self.symbol_time)-1)/(2*self.beta)))
        self.tukey_window *= 2/np.sqrt(4-self.beta)

