import time 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import equiv_classes_calculator as eq_cls_calc
import constellation_maker as const_mk


def calculate_equiv_classes(constellation, sym_block_len_start, sym_block_len_end, constellation_name):
    results_folder = "results/"+constellation_name+"/"
    eq_classes_calc = eq_cls_calc.Equivalence_classes_calculator(constellation,constellation_name)
    for sym_block_len in range (sym_block_len_start,sym_block_len_end+1):
        eq_classes_calc.symbol_block_length = sym_block_len
        start_time = time.time()
        eq_classes_calc.calculate_equivalence_classes()
        calc_time = time.time() - start_time
        eq_classes_calc.save_results(results_folder,calc_time)


# ###########################################################################
# const_name = "4-PSK"
# const = const_mk.n_ring_m_ary_phase([1],4)
# calculate_equiv_classes(const, 3, 8, const_name)
# ###########################################################################

# ###########################################################################
# const_name = "2-4SQAM"
# const = const_mk.nr_np_SQAM([1,2],4)
# calculate_equiv_classes(const, 3, 7, const_name)
# ###########################################################################

# ###########################################################################
# const_name = "2-Ring_4-Ary"
# const = const_mk.n_ring_m_ary_phase([1,2],4)
# calculate_equiv_classes(const, 3, 7, const_name)
# ###########################################################################

# ###########################################################################
# const_name = "4-Ring_4-Ary"
# const = const_mk.n_ring_m_ary_phase([1,2,3,4],4)
# calculate_equiv_classes(const, 3, 5, const_name)
# ###########################################################################

# ###########################################################################
# const_name = "8-Ring_8-Ary"
# const = const_mk.n_ring_m_ary_phase([1,2,3,4,5,6,7,8],8)
# calculate_equiv_classes(const, 3, 4, const_name)
# ###########################################################################

# ###########################################################################
# const_name = "10-Ring_10-Ary"
# const = const_mk.n_ring_m_ary_phase([1,2,3,4,5,6,7,8,9,10],10)
# calculate_equiv_classes(const, 3, 3, const_name)
# ###########################################################################

# ###########################################################################
# const_name = "16-QAM"
# const = const_mk.n_QAM(16)
# calculate_equiv_classes(const, 3, 5, const_name)
# ###########################################################################
