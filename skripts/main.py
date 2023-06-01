import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt 

import class_representative
import signaling
import photodiode
import integrate_dump

file_name = "communications_system/representative_classes/2-Ring_4-Ary_n3.npy"
class_rep_block = class_representative.Class_representative_block(file_name)
sig_block = signaling.Signaling_block(symbol_time=1, sps=101, beta=0.5, adjust_beta=True)
photodiode_block = photodiode.Photodiode(responsivity=1, sigma2_sh=0, sigma_2_th=0)
int_dump_block = integrate_dump.Integrate_dump_block(sig_block)


# rng = np.random.default_rng()
# N_sym_blocks = 10

# k_vec = rng.choice(class_rep_block.representative_class_size, N_sym_blocks)
# symbols = class_rep_block.get_symbol_blocks(k_vec)
# tx_signal = sig_block.generate_signal(symbols)
# rx_signal = photodiode_block.square_law_detection(tx_signal)
# y,z = int_dump_block.integrate_dump(rx_signal)



plt.figure(1)
plt.stem(sig_block.time_vec,sig_block.tukey_window)


# plt.figure(2)
# plt.stem(np.arange(len(rx_signal))*sig_block.Ts, rx_signal)

# plt.figure(3)
# plt.stem(y)

# plt.figure(4)
# plt.stem(z)


plt.show()
