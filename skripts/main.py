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
file_name = "communications_system/representative_classes/2-4SQAM_n3.npy"
sym_block_len = 3
baud_rate = 1e6
sym_time = 1/baud_rate
sps = 21
fs = (sps-1)/sym_time
beta = 0.5
responsivity = 10 # R_APD = M_APD*R_D
sigma2_sh = photodiode.get_sigma2_sh(M_APD=20, F=12.78, R_APD=10, BW_2side=fs)
sigma2_th = photodiode.get_sigma2_th(Tk=300, RL=15, BW_2side=fs)
print(f"shot noise power\t{sigma2_sh: .3e}")
print(f"thermal noise power\t{sigma2_th: .3e}")

N_sym_blocks = 10_000
rng_seed = None

########################## system blocks creation #################################
class_rep_block = class_representative.Class_representative_block(file_name,sym_block_len)
sig_block = signaling.Signaling_block(sym_time, sps, beta, adjust_beta=True)
beta = sig_block.beta
photodiode_block = photodiode.Photodiode(responsivity, sigma2_sh, sigma2_th, rng_seed)
int_dump_block = integrate_dump.Integrate_dump_block(sig_block)
detector_block = detector.Detector_block(sym_time, beta, sym_block_len, responsivity, sigma2_sh, sigma2_th)


########################## Simulation #####################################
constellation = const_mk.nr_np_SQAM([1,1+np.sqrt(2)],4)
constellation = const_mk.normalize_constellation_x_dBm(constellation,-17)
class_rep_block.set_up_const_and_rep_class(constellation)
detector_block.set_representative_class(class_rep_block.representative_class)
s = time.time()
rng = np.random.default_rng(rng_seed)
k_tx = rng.choice(len(class_rep_block.representative_class), N_sym_blocks)
symbols = class_rep_block.get_symbol_blocks(k_tx)
tx_signal = sig_block.generate_signal(symbols)
rx_signal = photodiode_block.square_law_detection(tx_signal)
y,z = int_dump_block.integrate_dump(rx_signal)
k_rx = detector_block.decode(y,z,N_sym_blocks)
e = time.time()
print(f"simulation time: {e-s: .3f} seconds")
print(f"SER: {np.mean(k_tx != k_rx)}")
