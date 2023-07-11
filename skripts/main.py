import time
import numpy as np

from tukey_signaling import Tukey_signaling
import constellation_maker as const_mk
import photodiode


####################### Definition of the system and simulation #######################
tukey_sig_system = Tukey_signaling(file_name="communications_system/representative_classes/2-4SQAM_n3_all.npy",
                                   sym_block_len=3,
                                   baud_rate=10e9,
                                   sps=21,
                                   responsivity=10,                                             # R_APD = M_APD*R_D
                                   N0_sh=photodiode.get_N0_sh(M_APD=20, F=12.78, R_apd=10),
                                   N0_th=photodiode.get_N0_th(Tk=300, RL=15),
                                   constellation=const_mk.nr_np_SQAM([1,1+np.sqrt(2)],4),
                                   ideal=False)


betas = np.array([0.1,0.5,0.7,0.9])
rop_range_dBm = np.arange(-13,-4)
N_sym_blocks = 100
rng_seed = 55

##################################### Simulation ######################################
ser = np.empty((len(betas),len(rop_range_dBm)))
ber = np.empty((len(betas),len(rop_range_dBm)))
mi = np.empty((len(betas),len(rop_range_dBm)))

start_time = time.time()
for i,beta in enumerate(betas):
    print(f"starting simulation for beta = {beta}")
    tukey_sig_system.setup_system(beta, rng_seed, adjust_beta=True)
    for j,rop_dBm in enumerate(rop_range_dBm):
        print(f"\tstarting simulation for ROP = {rop_dBm} dBm")
        sub_start_time = time.time()
        ser[i,j],ber[i,j],mi[i,j] = tukey_sig_system.simulate_transmission(N_sym_blocks, rop_dBm, rng_seed)
        sub_end_time = time.time()
        print(f"\tsimulation for ROP = {rop_dBm} dBm done successfully")
        print(f"\tsimulation time: {sub_end_time-sub_start_time: .3f} seconds")
    print(f"simulation for beta = {beta} done successfully")
end_time = time.time()

################################## Saving results ###################################
tukey_sig_system.save_results("whole_system_sim_results/2-4SQAM_n3_all.p",
                              N_sym_blocks=N_sym_blocks,
                              betas=betas,
                              rop_range_dBm=rop_range_dBm,
                              ser=ser,
                              ber=ber,
                              mi=mi,
                              sim_time=end_time-start_time,
                              rng_seed=rng_seed)
