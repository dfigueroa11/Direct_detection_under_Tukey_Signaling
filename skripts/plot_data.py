import numpy as np
import pickle
import matplotlib.pyplot as plt

sys_2_4_SQAM_n3 = pickle.load(open("whole_system_sim_results/2-4SQAM_n3_all_MI.p","rb"))
sys_2_4_SQAM_n4 = pickle.load(open("whole_system_sim_results/2-4SQAM_n4_256.p","rb"))


plt.figure(0)
for ber,beta in zip(sys_2_4_SQAM_n4["ber"],sys_2_4_SQAM_n4["betas"]):
    plt.semilogy(sys_2_4_SQAM_n4["rop_range_dBm"], ber, label=f"beta={beta}")
plt.legend()
plt.grid()
plt.ylabel("BER")
plt.xlabel("ROP [dBm]")
plt.ylim(bottom=1e-4)
plt.xlim(-17,-7)
plt.xticks(sys_2_4_SQAM_n4["rop_range_dBm"])


plt.figure(1)
for mi,beta in zip(sys_2_4_SQAM_n3["mi"],sys_2_4_SQAM_n3["betas"]):
    plt.plot(sys_2_4_SQAM_n3["rop_range_dBm"], mi, label=f"beta={beta}")
plt.legend()
plt.grid()
plt.ylabel("MI")
plt.xlabel("ROP [dBm]")
plt.ylim(0,(3-0.9433583328525624)*1.05)
plt.xlim(-33,-5)
plt.xticks(sys_2_4_SQAM_n3["rop_range_dBm"][::2])


plt.show()


