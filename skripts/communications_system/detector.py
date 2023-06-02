import numpy as np

class Detector_block:

    symbol_time = None
    beta = None 
    symbol_block_len = None
    constellation = None
    responsivity = None
    sigma_sh = None
    sigma_th = None

    def __init__(self, symbol_time, beta, symbol_block_len, constellation, responsivity, sigma_sh, sigma_th):
        self.symbol_time = symbol_time
        self.beta = beta
        self.symbol_block_len = symbol_block_len
        self.constellation = constellation
        self.responsivity = responsivity
        self.sigma_sh = sigma_sh
        self.sigma_th = sigma_th

    def decode(self,y,z):
        pass
        
    


