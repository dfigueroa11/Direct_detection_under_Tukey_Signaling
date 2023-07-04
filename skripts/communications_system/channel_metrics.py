import numpy as np

def get_SER(k_tx, k_rx):
    return np.mean(k_tx != k_rx)

def get_BER(k_tx, k_rx, rep_class_size):
    bits_len = int(np.log2(rep_class_size))
    bits_tx = symbols_to_bits(k_tx, bits_len)
    bits_rx = symbols_to_bits(k_rx, bits_len)
    return np.mean(bits_tx != bits_rx)

def symbols_to_bits(symbols, bits_len):
    return np.array([dec2bin(sym,bits_len) for sym in symbols]).flatten()

def dec2bin(num,len):
    return [int(bit) for bit in bin(num)[2:].zfill(len)]

def get_MI(k_tx, k_rx, rep_class_size, sym_block_len):
    N = len(k_tx)
    MI = 0

    p_r_given_t_mat = np.zeros((rep_class_size,rep_class_size))
    p_t_vec = np.zeros(rep_class_size)
    p_r_vec = np.zeros(rep_class_size)
    for t in range(rep_class_size):
        for r in range(rep_class_size):
            p_r_given_t_mat[r,t] = np.count_nonzero(np.logical_and(k_tx == t, k_rx == r))/np.count_nonzero(k_tx == t)
        p_t_vec[t] = np.count_nonzero(k_tx == t)/N
    
    for r in range(rep_class_size):
        p_r_vec[r] = np.sum([p_r_given_t_mat[r,t]*p_t_vec[t] for t in range(rep_class_size)])
    for tx_sym in range(rep_class_size):
        for rx_sym in range(rep_class_size):
            p_r_and_t = np.count_nonzero(np.logical_and(k_tx == tx_sym, k_rx == rx_sym))/N
            MI +=  prod_log2(p_r_and_t,p_r_given_t_mat[rx_sym,tx_sym]/p_r_vec[rx_sym])
    return MI/sym_block_len

def prod_log2(a,b):
    if a == 0 and b == 0:
        return 0
    return a*np.log2(b) 
