import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt 

import signaling


sig_block_1 = signaling.Signaling_block(symbol_time=1, sps=1001, beta=0.3)
plt.plot(sig_block_1.time_vec,sig_block_1.tukey_window)
plt.grid(visible=True)
plt.show()