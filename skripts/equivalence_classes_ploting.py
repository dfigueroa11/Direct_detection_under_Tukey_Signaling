import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import equiv_class_analyzator
import constellation_maker as const_mk


def plot_eq_class(file_name, constellation, symbol_block_length, class_size, num_classes, size_classes_selection, size_sym_block_selection):
    rng = np.random.default_rng()
    eq_class_analyzer = equiv_class_analyzator.Equiv_class_analyzator(file_name,symbol_block_length)
    eq_classes_size_n = eq_class_analyzer.get_equiv_classes_of_size_n(class_size,num_classes)
    select_classes = rng.choice(np.shape(eq_classes_size_n)[0], size=size_classes_selection, replace=False)
    select_sym_block = rng.choice(class_size, size=size_sym_block_selection, replace=False)
    eq_classes_size_n_plot = eq_classes_size_n[select_classes,:,:]
    eq_classes_size_n_plot = eq_classes_size_n_plot[:,select_sym_block,:]
    eq_class_analyzer.plot_all_equivalence_classes(eq_classes_size_n_plot,constellation)
    plt.show()


#########################################################################
file_name = "results/10-Ring_10-Ary/EqClasses_10-Ring_10-Ary_n3.npy"
const = const_mk.n_ring_m_ary_phase([1,2,3,4,5,6,7,8,9,10],10)
sym_block_len = 3
class_size = 40
size_sym_block_selection = 10
num_classes = 20250
size_classes_selection = 10
plot_eq_class(file_name, const, sym_block_len, class_size, num_classes,size_classes_selection,size_sym_block_selection)
