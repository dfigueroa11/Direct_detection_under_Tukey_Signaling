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
rop_range_dBm = np.arange(-33,-4)
N_sym_blocks = 100_000
rng_seed = 55

output_file_name = "whole_system_sim_results/2-4SQAM_n3_all.p"

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
        ################ save partial results in case simulation stops ###################
        tukey_sig_system.save_results(output_file_name,
                                      N_sym_blocks=N_sym_blocks,
                                      betas=betas,
                                      rop_range_dBm=rop_range_dBm,
                                      rep_class_size=len(tukey_sig_system.class_rep_block.representative_class),
                                      ser=ser,
                                      ber=ber,
                                      mi=mi,
                                      rng_seed=rng_seed,
                                      sim_ended=False,
                                      current_beta=beta,
                                      current_rop_dBm=rop_dBm)

    print(f"simulation for beta = {beta} done successfully")
end_time = time.time()

################################## Saving results ###################################
tukey_sig_system.save_results(output_file_name,
                              N_sym_blocks=N_sym_blocks,
                              betas=betas,
                              rop_range_dBm=rop_range_dBm,
                              rep_class_size=len(tukey_sig_system.class_rep_block.representative_class),
                              ser=ser,
                              ber=ber,
                              mi=mi,
                              sim_time=end_time-start_time,
                              rng_seed=rng_seed,
                              sim_ended=True)
