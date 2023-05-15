import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import equiv_class_analyzator
import constellation_maker as const_mk


def plot_eq_class(file_name, constellation, symbol_block_length, class_size, num_classes_ploted, num_sym_blocks_ploted):
    rng = np.random.default_rng()
    eq_class_analyzer = equiv_class_analyzator.Equiv_class_analyzator(file_name,symbol_block_length)
    eq_classes_size_n = eq_class_analyzer.get_equiv_classes_of_size_n(class_size)
    num_classes_ploted = min(num_classes_ploted,np.shape(eq_classes_size_n)[0])
    num_sym_blocks_ploted = min(num_sym_blocks_ploted,np.shape(eq_classes_size_n)[1])
    select_classes = rng.choice(np.shape(eq_classes_size_n)[0], size=num_classes_ploted, replace=False)
    select_sym_block = rng.choice(class_size, size=num_sym_blocks_ploted, replace=False)
    eq_classes_size_n_plot = eq_classes_size_n[select_classes,:,:]
    eq_classes_size_n_plot = eq_classes_size_n_plot[:,select_sym_block,:]
    eq_class_analyzer.plot_all_equivalence_classes(eq_classes_size_n_plot,constellation)
    plt.show()



# #########################################################################
# file_name = "results/10-Ring_10-Ary/EqClasses_10-Ring_10-Ary_n3.npy"
# const = const_mk.n_ring_m_ary_phase([1,2,3,4,5,6,7,8,9,10],10)
# sym_block_len = 3
# class_size = 40
# num_classes_ploted = 40
# num_sym_blocks_ploted = 1
# plot_eq_class(file_name, const, sym_block_len, class_size, num_classes_ploted, num_sym_blocks_ploted)
# #########################################################################

# #########################################################################
# file_name = "results/8-Ring_8-Ary/EqClasses_8-Ring_8-Ary_n3.npy"
# const = const_mk.n_ring_m_ary_phase([1,2,3,4,5,6,7,8],8)
# sym_block_len = 3
# class_size = 16 # 8 16 32
# num_classes_ploted = 40
# num_sym_blocks_ploted = 1
# plot_eq_class(file_name, const, sym_block_len, class_size, num_classes_ploted, num_sym_blocks_ploted)
# #########################################################################

# #########################################################################
# file_name = "results/5-Ring_5-Ary/EqClasses_5-Ring_5-Ary_n4.npy"
# const = const_mk.n_ring_m_ary_phase([1,2,3,4,5],5)
# sym_block_len = 4
# class_size = 40 # 5 10 20 40
# num_classes_ploted = 20
# num_sym_blocks_ploted = 40
# plot_eq_class(file_name, const, sym_block_len, class_size, num_classes_ploted, num_sym_blocks_ploted)
# #########################################################################

# #########################################################################
# file_name = "results/4-Ring_4-Ary/EqClasses_4-Ring_4-Ary_n3.npy"
# const = const_mk.n_ring_m_ary_phase([1,2,3,4],4)
# sym_block_len = 3
# class_size = 16 # 4 8 16
# num_classes_ploted = 40
# num_sym_blocks_ploted = 4
# plot_eq_class(file_name, const, sym_block_len, class_size, num_classes_ploted, num_sym_blocks_ploted)
# #########################################################################
 
# #########################################################################
# file_name = "results/2-4SQAM/EqClasses_2-4SQAM_n3.npy"
# const = const_mk.nr_np_SQAM([1,2],4)
# sym_block_len = 3
# class_size = 8 # 4 8 16
# num_classes_ploted = 4
# num_sym_blocks_ploted = 8
# plot_eq_class(file_name, const, sym_block_len, class_size, num_classes_ploted, num_sym_blocks_ploted)
# #########################################################################


# #########################################################################
# file_name = "results/10-Ring_10-Ary/EqClasses_10-Ring_10-Ary_n3.npy"
# const = const_mk.n_ring_m_ary_phase([1,2,3,4,5,6,7,8,9,10],10)
# sym_block_len = 3
# class_size = 20
# eq_class_analyzer = equiv_class_analyzator.Equiv_class_analyzator(file_name,sym_block_len)
# eq_classes_size_n = eq_class_analyzer.get_equiv_classes_of_size_n(class_size)
# total_num_classes = np.shape(eq_classes_size_n)[0]
# i_class_size_20 = 7771
# i_sym_blocks_1 = (2,5,7,9,11,13,15,16,18,0)
# i_sym_blocks_2 = (6,4,3,1,19,17,14,12,10,8)
# #rng = np.random.default_rng()
# for i in i_sym_blocks_1:#range(class_size):#i_class_size_20:#rng.choice(total_num_classes, size=20):
#     plt.figure(i,figsize=(8,8))
#     eq_class_analyzer.plot_constellation(const)
#     eq_class_analyzer.plot_symbol_block(eq_classes_size_n[i_class_size_20,i,:])
# for i in i_sym_blocks_2:#range(class_size):#i_class_size_20:#rng.choice(total_num_classes, size=20):
#     plt.figure(i,figsize=(8,8))
#     eq_class_analyzer.plot_constellation(const)
#     eq_class_analyzer.plot_symbol_block(eq_classes_size_n[i_class_size_20,i,:])
# plt.figure(figsize=(8,8))
# eq_class_analyzer.plot_constellation(const)
# eq_class_analyzer.plot_equivalence_class(eq_classes_size_n[i_class_size_20,(0,8),:])
# plt.figure(figsize=(8,8))
# eq_class_analyzer.plot_constellation(const)
# eq_class_analyzer.plot_equivalence_class(eq_classes_size_n[i_class_size_20,i_sym_blocks_1,:])
# plt.figure(figsize=(8,8))
# eq_class_analyzer.plot_constellation(const)
# eq_class_analyzer.plot_equivalence_class(eq_classes_size_n[i_class_size_20,i_sym_blocks_2,:])
# plt.figure(figsize=(8,8))
# eq_class_analyzer.plot_constellation(const)
# eq_class_analyzer.plot_equivalence_class(eq_classes_size_n[i_class_size_20,:,:])
# plt.show()
# #########################################################################

#########################################################################
file_name = "results/10-Ring_10-Ary/EqClasses_10-Ring_10-Ary_n3.npy"
const = const_mk.n_ring_m_ary_phase([1,2,3,4,5,6,7,8,9,10],10)
sym_block_len = 3
class_size = 40
eq_class_analyzer = equiv_class_analyzator.Equiv_class_analyzator(file_name,sym_block_len)
eq_classes_size_n = eq_class_analyzer.get_equiv_classes_of_size_n(class_size)
total_num_classes = np.shape(eq_classes_size_n)[0]
i_class_size_40 = (19042,8460,6926,16099)
i_sym_blocks_2 = (37,39,19,17)
rng = np.random.default_rng()
for j in [1000]:#rng.choice(total_num_classes, size=1):
    plt.figure(figsize=(8,8))
    eq_class_analyzer.plot_constellation(const)
    eq_class_analyzer.plot_equivalence_class(eq_classes_size_n[j,:,:])
    for i in i_sym_blocks_2:#range(class_size):#i_class_size_40:#rng.choice(total_num_classes, size=20):#
        plt.figure(i,figsize=(8,8))
        eq_class_analyzer.plot_constellation(const)
        eq_class_analyzer.plot_symbol_block(eq_classes_size_n[j,i,:])
    # for i in i_sym_blocks_2:#range(class_size):#i_class_size_20:#rng.choice(total_num_classes, size=20):
    #     plt.figure(i,figsize=(8,8))
    #     eq_class_analyzer.plot_constellation(const)
    #     eq_class_analyzer.plot_symbol_block(eq_classes_size_n[i_class_size_20,i,:])
    # plt.figure(figsize=(8,8))
    # eq_class_analyzer.plot_constellation(const)
    # eq_class_analyzer.plot_equivalence_class(eq_classes_size_n[i_class_size_20,(0,8),:])
    # plt.figure(figsize=(8,8))
    # eq_class_analyzer.plot_constellation(const)
    # eq_class_analyzer.plot_equivalence_class(eq_classes_size_n[i_class_size_20,i_sym_blocks_1,:])
    # plt.figure(figsize=(8,8))
    # eq_class_analyzer.plot_constellation(const)
    # eq_class_analyzer.plot_equivalence_class(eq_classes_size_n[i_class_size_20,i_sym_blocks_2,:])
    plt.show()
#########################################################################

