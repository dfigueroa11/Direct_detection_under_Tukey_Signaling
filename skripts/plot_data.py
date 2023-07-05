import numpy as np
import matplotlib.pyplot as plt

files_ser = ("2-4SQAM_n4_M256_b 30_SER.npy",
             "2-4SQAM_n4_M256_b 50_SER.npy",
             "2-4SQAM_n4_M256_b 60_SER.npy",
             "2-4SQAM_n4_M256_b 70_SER.npy",
             "2-4SQAM_n4_M256_b 90_SER.npy")

files_ber = ("2-4SQAM_n4_M256_b 30_BER.npy",
             "2-4SQAM_n4_M256_b 50_BER.npy",
             "2-4SQAM_n4_M256_b 60_BER.npy",
             "2-4SQAM_n4_M256_b 70_BER.npy",
             "2-4SQAM_n4_M256_b 90_BER.npy")

files_mi = ("2-4SQAM_n3_M72_b 10_MI.npy",
            "2-4SQAM_n3_M72_b 50_MI.npy",
            "2-4SQAM_n3_M72_b 70_MI.npy",
            "2-4SQAM_n3_M72_b 90_MI.npy")


betas = np.array([0.3,0.5,0.6,0.7,0.9])
optical_power_range = np.arange(-17,-6)

betas_mi = np.array([0.1,0.5,0.7,0.9])
optical_power_range_mi = np.arange(-33,-4)


ser_results = np.empty((len(betas),len(optical_power_range)))
ber_results = np.empty((len(betas),len(optical_power_range)))
mi_results = np.empty((len(betas_mi),len(optical_power_range_mi)))


for i,file in enumerate(files_ber):
    ber_results[i,:] = np.load("whole_system_sim_results/"+file)
for i,file in enumerate(files_ser):
    ser_results[i,:] = np.load("whole_system_sim_results/"+file)
for i,file in enumerate(files_mi):
    mi_results[i,:] = np.load("whole_system_sim_results/"+file)


plt.figure(0)
for ber,beta in zip(ber_results,betas):
    plt.semilogy(optical_power_range, ber, label=f"beta={beta}")
plt.legend()
plt.grid()
plt.ylabel("BER")
plt.xlabel("ROP [dBm]")
plt.ylim(bottom=1e-4)
plt.xlim(-17,-7)
plt.xticks(optical_power_range)


plt.figure(1)
for mi,beta in zip(mi_results,betas_mi):
    plt.plot(optical_power_range_mi, mi, label=f"beta={beta}")
plt.legend()
plt.grid()
plt.ylabel("MI")
plt.xlabel("ROP [dBm]")
plt.ylim(0,(3-0.9433583328525624)*1.05)
plt.xlim(-33,-5)
plt.xticks(optical_power_range_mi[::2])


plt.show()


