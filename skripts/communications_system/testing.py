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
symbols = constellation[np.random.choice(4, size=int(4e3))]

start = time.time()
signal = sig_block_1.generate_signal_1(symbols=symbols)
end = time.time()
print("method 1 needed :{} to complete the task".format(end-start))
start = time.time()
signal = sig_block_1.generate_signal_2(symbols=symbols)
end = time.time()
print("method 2 needed :{} to complete the task".format(end-start))
start = time.time()
signal = sig_block_1.generate_signal_3(symbols=symbols)
end = time.time()
print("method 3 needed :{} to complete the task".format(end-start))
start = time.time()
signal = sig_block_1.generate_signal_4(symbols=symbols)
end = time.time()
print("method 4 needed :{} to complete the task".format(end-start))
start = time.time()
signal = sig_block_1.generate_signal_5(symbols=symbols)
end = time.time()
print("method 5 needed :{} to complete the task".format(end-start))
