import numpy as np
import equiv_classes_calculator

################## definition of the communication scheme ##################
constellation = np.array([1, 1j, -1, -1j])
constellation = np.append(constellation,constellation*(1+np.sqrt(2)))
symbol_block_length = 3
############################################################################

eq_classes_calc = equiv_classes_calculator.Equivalence_classes_calculator(constellation,symbol_block_length)
eq_classes_calc.calculate_equivalence_classes()


class_size_cnt = np.zeros(7)

for key, value in eq_classes_calc.equivalence_classes.items():
    class_size = len(value)//symbol_block_length
    class_size_cnt[int(np.log2(class_size)-2)] += 1
    
print(class_size_cnt)
print(len(eq_classes_calc.equivalence_classes.keys()))




