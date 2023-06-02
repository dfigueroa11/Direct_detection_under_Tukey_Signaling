import numpy as np

class Detector_block:

    symbol_time = None
    beta = None 
    symbol_block_len = None
    representative_class = None
    responsivity = None
    sigma_sh = None
    sigma_th = None

    def __init__(self, symbol_time, beta, symbol_block_len, representative_class, responsivity, sigma_sh, sigma_th):
        self.symbol_time = symbol_time
        self.beta = beta
        self.symbol_block_len = symbol_block_len
        self.representative_class = representative_class
        self.responsivity = responsivity
        self.sigma_sh = sigma_sh
        self.sigma_th = sigma_th

    def decode(self,y,z,num_sym_blocks):
        for rx_sym_block in range(num_sym_blocks):
            for sym_block in self.representative_class:
                # calculate liklyhood_y_z_given_sym_block
                # if liklyhood is bigger update k:
                pass
            # rx_k[rx_sym_block] = k_hat
        # return rx_k