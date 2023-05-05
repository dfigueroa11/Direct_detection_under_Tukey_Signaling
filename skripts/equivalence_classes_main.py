import numpy as np
import equiv_classes_calculator

################## definition of the communication scheme ##################
constellation = np.array([1, 1j, -1, -1j])
constellation = np.append(constellation,constellation*(1+np.sqrt(2)))
constellation_name = "2-Ring_4-Ary"
symbol_block_length_start = 3
symbol_block_length_end = 7
results_folder = "results/"+constellation_name+"/"
############################################################################

eq_classes_calc = equiv_classes_calculator.Equivalence_classes_calculator(constellation,constellation_name)

for symbol_block_length in range (symbol_block_length_start,symbol_block_length_end+1):
    eq_classes_calc.symbol_block_length = symbol_block_length
    eq_classes_calc.calculate_equivalence_classes()
    eq_classes_calc.save_results(results_folder)





