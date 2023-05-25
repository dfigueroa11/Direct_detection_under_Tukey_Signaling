import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt 

import class_representative
import signaling
import photodiode

file_name = "communications_system/representative_classes/2-Ring_4-Ary_n3.npy"
class_rep_block = class_representative.Class_representative_block(file_name)
sig_block = signaling.Signaling_block(symbol_time=1, sps=21, beta=0.5)
photodiode_block = photodiode.Photodiode(responsivity=1, sigma2_sh=0.1, sigma_2_th=0.1)



rng = np.random.default_rng(3)
N_sym_blocks = 5

k_vec = rng.choice(class_rep_block.representative_class_size, N_sym_blocks)
symbols = class_rep_block.get_symbol_blocks(k_vec)
tx_signal = sig_block.generate_signal(symbols)
rx_signal = photodiode_block.square_law_detection(tx_signal)

plt.figure(1)
plt.plot(rx_signal)
plt.show()