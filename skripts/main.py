import time
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt 

import constellation_maker as const_mk
import class_representative
import signaling
import photodiode
import integrate_dump
import detector

########################## Problem definition #####################################
file_name = "communications_system/representative_classes/2-Ring_4-Ary_n3.npy"
constellation = const_mk.n_ring_m_ary_phase([1,2],4)
sym_block_len = 3
sym_time = 1
sps = 11
beta = 0.6
responsivity = 1
sigma2_sh = photodiode.get_sigma2_sh(M_APD=20, F=12.78, R_APD=10) # values from the paper
sigma2_th = photodiode.get_sigma2_th(Tk=300, RL=15) # values from the paper

N_sym_blocks = 10_000
rng_seed = 4

########################## system blocks creation #################################
class_rep_block = class_representative.Class_representative_block(file_name,constellation,sym_block_len)
sig_block = signaling.Signaling_block(sym_time, sps, beta, adjust_beta=True)
beta = sig_block.beta
photodiode_block = photodiode.Photodiode(responsivity, sigma2_sh, sigma2_th, rng_seed)
int_dump_block = integrate_dump.Integrate_dump_block(sig_block)
detector_block = detector.Detector_block(sym_time, beta, sym_block_len, class_rep_block.representative_class,
                                        responsivity, sigma2_sh, sigma2_th)

########################## Simulation #####################################

s = time.time()
rng = np.random.default_rng(rng_seed)
k_tx = rng.choice(class_rep_block.representative_class_size, N_sym_blocks)
symbols = class_rep_block.get_symbol_blocks(k_tx)
tx_signal = sig_block.generate_signal(symbols)
rx_signal = photodiode_block.square_law_detection(tx_signal)
y,z = int_dump_block.integrate_dump(rx_signal)
k_rx = detector_block.decode(y,z,N_sym_blocks)
e = time.time()
print(e-s)
print(np.where(k_tx != k_rx))


# plt.figure(1)
# plt.stem(sig_block.time_vec,sig_block.tukey_window)


# plt.figure(2)
# plt.stem(np.arange(len(rx_signal))*sig_block.Ts, rx_signal)


# plt.show()