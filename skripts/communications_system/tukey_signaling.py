import numpy as np
import pickle

import constellation_maker as const_mk
import class_representative
import signaling
import photodiode
import integrate_dump
import detector
from channel_metrics import get_BER, get_MI, get_SER


class Tukey_signaling: 

    file_name = None
    sym_block_len = None
    baud_rate = None
    sym_time = None
    sps = None
    fs = None
    responsivity = None
    sigma2_sh = None
    sigma2_th = None
    ideal = None
    beta = None
    constellation = None

    class_rep_block = None
    sig_block = None
    photodiode_block = None
    int_dump_block = None
    detector_block = None


    def __init__(self, file_name, sym_block_len, baud_rate, sps, responsivity, N0_sh, N0_th, constellation, ideal=False):
        self.file_name = file_name
        self.sym_block_len = sym_block_len
        self.baud_rate = baud_rate
        self.sym_time = 1/self.baud_rate
        self.sps = sps
        self.fs = (self.sps-1)/self.sym_time
        self.responsivity = responsivity
        self.sigma2_sh = N0_sh*self.fs
        self.sigma2_th = N0_th*self.fs
        self.constellation = constellation
        self.ideal = ideal

    def setup_system(self, beta, rng_seed, adjust_beta=True):
        self.class_rep_block = class_representative.Class_representative_block(self.file_name,self.sym_block_len)
        self.sig_block = signaling.Signaling_block(self.sym_time, self.sps, beta, adjust_beta=adjust_beta)
        self.beta = self.sig_block.beta
        self.photodiode_block = photodiode.Photodiode(self.responsivity, self.sigma2_sh, self.sigma2_th, 
                                                      rng_seed, ideal=self.ideal)
        self.int_dump_block = integrate_dump.Integrate_dump_block(self.sig_block)
        self.detector_block = detector.Detector_block(self.sym_time, self.sig_block.Ts, self.beta, self.sym_block_len,
                                                      self.responsivity, self.sigma2_sh, self.sigma2_th)
        
    def simulate_transmission(self, N_sym_blocks, rop_dBm, rng_seed=None):
        constellation = const_mk.normalize_constellation_x_dBm(self.constellation,rop_dBm)
        self.class_rep_block.set_up_const_and_rep_class(constellation)
        self.detector_block.set_representative_class(self.class_rep_block.representative_class)
        rng = np.random.default_rng(rng_seed)
        len_rep_class = len(self.class_rep_block.representative_class)
        k_tx = rng.choice(len_rep_class, N_sym_blocks)
        symbols = self.class_rep_block.get_symbol_blocks(k_tx)
        tx_signal = self.sig_block.generate_signal(symbols)
        rx_signal = self.photodiode_block.square_law_detection(tx_signal)
        y,z = self.int_dump_block.integrate_dump(rx_signal)
        k_rx = self.detector_block.decode_loglikelihood(y,z,N_sym_blocks)
        ser = get_SER(k_tx, k_rx)
        ber = get_BER(k_tx, k_rx, len_rep_class)
        mi = get_MI(k_tx, k_rx, len_rep_class, self.sym_block_len)
        return ser, ber, mi
    
    def save_results(self, file_name, **kwargs):
        save_data = {"sym_block_len": self.sym_block_len,
                     "baud_rate": self.baud_rate,
                     "sym_time": self.sym_time,
                     "sps": self.sps,
                     "fs": self.fs,
                     "responsivity": self.responsivity,
                     "sigma2_sh": self.sigma2_sh,
                     "sigma2_th": self.sigma2_th,
                     "constellation": self.constellation}
        for key, value in kwargs.items():
            save_data[key] = value

        pickle.dump(save_data, open(file_name, "wb"))