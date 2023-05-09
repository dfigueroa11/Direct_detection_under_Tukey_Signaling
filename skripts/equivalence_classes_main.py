import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import equiv_classes_calculator
import equiv_class_analyzator
import constellation_maker as const_mk

################## definition of the communication scheme ##################
# constellation = np.array([1, 1j, -1, -1j])
# constellation = np.append(constellation,constellation*(1+np.sqrt(2)))
# constellation_name = "2-Ring_4-Ary"
# symbol_block_length_start = 3
# symbol_block_length_end = 3
# results_folder = "results/"+constellation_name+"/"
############################################################################

# eq_classes_calc = equiv_classes_calculator.Equivalence_classes_calculator(constellation,constellation_name)

# for symbol_block_length in range (symbol_block_length_start,symbol_block_length_end+1):
#     eq_classes_calc.symbol_block_length = symbol_block_length
#     eq_classes_calc.calculate_equivalence_classes()
#     eq_classes_calc.save_results(results_folder)

eq_class_analyzer = equiv_class_analyzator.Equiv_class_analyzator("results/2-Ring_4-Ary/EqClasses_2-Ring_4-Ary_n3.npy",3)


# eq_class_analyzer.plot_all_equivalence_classes(eq_class_analyzer.get_equiv_classes_of_size_n(8), constellation)
# plt.show()

plt.figure(0, figsize=(8,8))
eq_class_analyzer.plot_constellation(const_mk.n_QAM(64))
plt.show()