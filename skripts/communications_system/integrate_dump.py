import numpy as np

import signaling


class Integrate_dump_block:
    
    Ts = None
    sps = None
    ISI_free_len = None
    ISI_present_len = None

    def __init__(self, signaling_block:signaling.Signaling_block):
        self.window_len = signaling_block.window_len
        self.Ts = signaling_block.Ts
        self.sps = signaling_block.sps
        self.ISI_free_len = np.count_nonzero(signaling_block.tukey_window == np.max(signaling_block.tukey_window))
        self.ISI_present_len = (self.window_len-self.ISI_free_len)//2
        if self.ISI_free_len+self.ISI_present_len*2 != self.window_len:
            print("somthing is wrong with the window")
    
    def integrate_dump(self, signal):
        num_symbols = int((len(signal)-self.window_len)/(self.sps-1)+1)
        y = np.empty(num_symbols)
        z = np.empty(num_symbols)
        for i in range(num_symbols):
            start_y = i*(self.ISI_present_len+self.ISI_free_len-1)+self.ISI_present_len
            start_z = start_y+self.ISI_free_len-1
            y[i] = np.trapz(signal[start_y : start_y+self.ISI_free_len], dx=self.Ts)
            z[i] = np.trapz(signal[start_z : start_z+self.ISI_present_len+1], dx=self.Ts)
        return y,z