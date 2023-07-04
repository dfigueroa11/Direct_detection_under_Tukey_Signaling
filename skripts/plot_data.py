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

betas = np.array([0.3,0.5,0.6,0.7,0.9])
optical_power_range = np.arange(-17,-6)

ser_results = np.empty((len(betas),len(optical_power_range)))
ber_results = np.empty((len(betas),len(optical_power_range)))

for i,file in enumerate(files_ber):
    ber_results[i,:] = np.load("hole_system_sim_results/"+file)
for i,file in enumerate(files_ser):
    ser_results[i,:] = np.load("hole_system_sim_results/"+file)

plt.figure()
for ber,beta in zip(ber_results,betas):
    plt.semilogy(optical_power_range, ber, label=f"beta={beta}")
plt.legend()
plt.grid()
plt.ylabel("BER")
plt.xlabel("ROP [dBm]")
plt.ylim(bottom=1e-4)
plt.xlim(-17,-7)
plt.xticks(optical_power_range)
plt.show()
