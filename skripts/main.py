import time
import numpy as np
import matplotlib.pyplot as plt 

import constellation_maker as const_mk
import class_representative
import signaling
import photodiode
import integrate_dump
import detector
from channel_metrics import get_BER, get_MI, get_SER

betas = np.array([0.1,0.5,0.7,0.9])
start = time.time()
for beta in betas:
    ########################## Problem definition #####################################
    file_name = "communications_system/representative_classes/2-4SQAM_n3_all.npy"
    sym_block_len = 3
    baud_rate = 10e9
    sym_time = 1/baud_rate
    sps = 21
    fs = (sps-1)/sym_time
    R_apd = 10 # R_APD = M_APD*R_D
    sigma2_sh = photodiode.get_sigma2_sh(M_APD=20, F=12.78, R_apd=10, BW_2side=fs)
    sigma2_th = photodiode.get_sigma2_th(Tk=300, RL=15, BW_2side=fs)
    ideal = False
    optical_power_range = np.arange(-33,-4)

    N_sym_blocks = 100000#200_000
    rng_seed = 55

    ########################## system blocks creation #################################
    class_rep_block = class_representative.Class_representative_block(file_name,sym_block_len)
    sig_block = signaling.Signaling_block(sym_time, sps, beta, adjust_beta=True)
    beta = sig_block.beta
    photodiode_block = photodiode.Photodiode(R_apd, sigma2_sh, sigma2_th, rng_seed, ideal=ideal)
    int_dump_block = integrate_dump.Integrate_dump_block(sig_block)
    detector_block = detector.Detector_block(sym_time, sig_block.Ts, beta, sym_block_len, R_apd, sigma2_sh, sigma2_th)

    ########################## Simulation #####################################

    # ser = np.empty_like(optical_power_range, dtype=float)
    # ber = np.empty_like(optical_power_range, dtype=float)
    mi = np.empty_like(optical_power_range, dtype=float)
    for i,op_pow in enumerate(optical_power_range):
        constellation = const_mk.nr_np_SQAM([1,1+np.sqrt(2)],4)
        constellation = const_mk.normalize_constellation_x_dBm(constellation,op_pow)
        class_rep_block.set_up_const_and_rep_class(constellation)
        detector_block.set_representative_class(class_rep_block.representative_class)
        s = time.time()
        rng = np.random.default_rng(rng_seed)
        k_tx = rng.choice(len(class_rep_block.representative_class), N_sym_blocks)
        symbols = class_rep_block.get_symbol_blocks(k_tx)
        tx_signal = sig_block.generate_signal(symbols)
        rx_signal = photodiode_block.square_law_detection(tx_signal)
        y,z = int_dump_block.integrate_dump(rx_signal)
        k_rx = detector_block.decode_logliklyhood(y,z,N_sym_blocks)
        e = time.time()
        # ser[i] = get_SER(k_tx, k_rx)
        # ber[i] = get_BER(k_tx, k_rx, len(class_rep_block.representative_class))
        mi[i] = get_MI(k_tx, k_rx, len(class_rep_block.representative_class), 3)
        print(f"\tsimulation for ROP = {op_pow} dBm done successfully")
        print(f"\tsimulation time: {e-s: .3f} seconds")
    

    print(f"simulation for beta = {beta} done successfully")
    # with open(f'hole_system_sim_results/2-4SQAM_n4_M256_b{beta*100: .0f}_SER.npy', 'wb') as f:
    #     np.save(f, ser)

    # with open(f'hole_system_sim_results/2-4SQAM_n4_M256_b{beta*100: .0f}_BER.npy', 'wb') as f:
    #     np.save(f, ber)

    with open(f'whole_system_sim_results/2-4SQAM_n3_M72_b{beta*100: .0f}_MI.npy', 'wb') as f:
        np.save(f, mi)
    

end = time.time()
with open(f"whole_system_sim_results/2-4SQAM_n3_M72_resume.txt", 'w') as f:
    f.write(f"number of symbol blocks simulated: {N_sym_blocks}\n")
    f.write(f"simulation time: {end-start: .0f} seconds\n")
    f.write(f"simulated betas: {np.array2string(betas)}\n")
    f.write(f"simulated optical power range in dBm: {np.array2string(optical_power_range)}\n")
    f.write(f"baud rate: {baud_rate: .5e} Hz\n")
    f.write(f"sps: {sps}\n")
    f.write(f"beta: {beta: .5f}\n")
    f.write(f"sigma2_sh: {sigma2_sh: .5e}\n")
    f.write(f"sigma2_th: {sigma2_th: .5e}\n")
    f.write(f"check numbers for rng: {rng.choice(1000,4)}\n")
    f.write(f"random generator seed: {rng_seed}")

