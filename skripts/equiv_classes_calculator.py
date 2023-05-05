import numpy as np


class Equivalence_classes_calculator:
    constellation = None
    symbol_block_length = None
    equivalence_classes = None
    
    def __init__(self,constell,symbol_block_len):
        self.constellation =   constell
        self.symbol_block_length = symbol_block_len

    def integrate_and_dump_no_noise(self,symbol_block):
        ISI_free = np.abs(symbol_block)**2
        ISI_present = 1/4*np.abs(symbol_block[:-1]+symbol_block[1:])**2+1/8*np.abs(symbol_block[:-1]-symbol_block[1:])**2    
        return tuple(np.append(ISI_free , ISI_present))

    def add_values_in_dict(self, int_damp_out, symbol_block):
        if int_damp_out not in self.equivalence_classes:
            self.equivalence_classes[int_damp_out] = np.array(symbol_block)    
        else:
            self.equivalence_classes[int_damp_out] = np.append(self.equivalence_classes[int_damp_out],symbol_block)
        
    def numberToBaseN(self, n):
        b = len(self.constellation)
        digits = np.zeros(self.symbol_block_length, dtype=np.int64)
        i = 0
        while n:
            digits[i] = int(n % b)
            n //= b
            i = i + 1
        return digits
    
    def generate_symbol_block(self,n):
        indices = self.numberToBaseN(n)
        return np.choose(indices,self.constellation)

    def calculate_equivalence_classes(self):
        self.equivalence_classes = {}
        for n in range(len(self.constellation)**self.symbol_block_length):
            symbol_block = self.generate_symbol_block(n)
            int_damp_out = self.integrate_and_dump_no_noise(symbol_block)
            self.add_values_in_dict(int_damp_out,symbol_block)


