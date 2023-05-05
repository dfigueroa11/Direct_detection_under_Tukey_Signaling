import numpy as np
import equiv_classes_calculator

################## definition of the communication scheme ##################
constellation = np.array([1, 1j, -1, -1j])
constellation = np.append(constellation,constellation*(1+np.sqrt(2)))
symbol_block_length = 3
############################################################################

eq_classes_calc = equiv_classes_calculator.Equivalence_classes_calculator(constellation,symbol_block_length)

for i in range (3,6):
    eq_classes_calc.symbol_block_length = i
    eq_classes_calc.calculate_equivalence_classes()
    eq_classes_calc.summarize_results()





