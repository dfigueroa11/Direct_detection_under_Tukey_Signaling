import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt 
import time

import signaling

sig_block_1 = signaling.Signaling_block(symbol_time=1, sps=21, beta=0.5)
plt.figure(0)
plt.stem(sig_block_1.time_vec,sig_block_1.tukey_window)
plt.grid(visible=True)

constellation = np.array([1+1j,-1+1j,-1+1j,-1-1j])
symbols = constellation[np.random.choice(4, size=int(5))]

signal = sig_block_1.generate_signal(symbols=symbols)
