import time
import numpy as np
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
sym_time = 1
sps = 21
beta = 0.5
responsivity = 10
sigma2_sh = photodiode.get_sigma2_sh(M_APD=20, F=12.78, R_APD=10*5e9)#3e-6#photodiode.get_sigma2_sh(M_APD=20, F=12.78, R_APD=1) # values from the paper
sigma2_th = photodiode.get_sigma2_th(Tk=300*5e9, RL=15)#3e-12#photodiode.get_sigma2_th(Tk=300, RL=15) # values from the paper
ideal = False
print(f"shot noise power\t{sigma2_sh: .3e}")
print(f"thermal noise power\t{sigma2_th: .3e}")

N_sym_blocks = 10000
rng_seed = 1

########################## system blocks creation #################################
class_rep_block = class_representative.Class_representative_block(file_name,sym_block_len)
sig_block = signaling.Signaling_block(sym_time, sps, beta, adjust_beta=True)
beta = sig_block.beta
photodiode_block = photodiode.Photodiode(responsivity, sigma2_sh, sigma2_th, rng_seed, ideal=ideal)
int_dump_block = integrate_dump.Integrate_dump_block(sig_block)
detector_block = detector.Detector_block(sym_time, beta, sym_block_len, responsivity, sigma2_sh, sigma2_th)
print(np.trapz(np.abs(sig_block.tukey_window)**2,dx=sig_block.Ts))

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
sig_power = np.trapz(np.abs(tx_signal)**2, dx=sig_block.Ts)/(sig_block.Ts*len(tx_signal))
sig_power = 10*np.log10(sig_power)+30
noise_power = np.trapz(np.abs(np.abs(tx_signal)**2*responsivity-rx_signal)**2, dx=sig_block.Ts)/(sig_block.Ts*len(tx_signal))
print(f"signal power: {sig_power: .2f} dBm")
print(f"noise power: {noise_power: .3e}")
print(f"simulation time: {e-s: .3f}")
print(f"SER: {np.mean(k_tx != k_rx)}")

y = np.reshape(y,(N_sym_blocks,3))
z = np.reshape(z,(N_sym_blocks,3))
z = z[:,:-1]


# print(np.allclose(np.mean(y, axis=0),detector_block.__means_y__[k_tx[0],:], rtol=1e-2))
# print(np.allclose(np.mean(z, axis=0),detector_block.__means_z__[k_tx[0],:], rtol=1e-2))

# print(np.allclose(np.var(y, axis=0),detector_block.__vars_y__[k_tx[0],:]))
# print(np.allclose(np.var(z, axis=0),detector_block.__vars_z__[k_tx[0],:]))


# plt.figure(1)
# # plt.stem(sig_block.time_vec,sig_block.tukey_window)
# plt.plot(rx_signal)

# plt.figure(2)
# plt.stem(y)
# plt.figure(3)
# plt.stem(z)


plt.show()