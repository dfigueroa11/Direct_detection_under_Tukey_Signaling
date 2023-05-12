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
# num_classes_ploted = 40
# num_sym_blocks_ploted = 1
# plot_eq_class(file_name, const, sym_block_len, class_size, num_classes_ploted, num_sym_blocks_ploted)
# #########################################################################
