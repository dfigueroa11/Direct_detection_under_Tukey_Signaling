import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt 
import time

import signaling
import constellation_maker

sig_block_1 = signaling.Signaling_block(symbol_time=1, sps=21, beta=0.5)
plt.figure(0)
plt.stem(sig_block_1.time_vec,sig_block_1.tukey_window)
plt.grid(visible=True)

constellation = constellation_maker.n_ring_m_ary_phase([1,2,3,4],4)
symbols = constellation[np.random.choice(len(constellation), size=int(30))]

signal = sig_block_1.generate_signal(symbols=symbols)


plt.figure(1)
plt.plot(np.real(signal))
plt.plot(np.imag(signal))
plt.show()