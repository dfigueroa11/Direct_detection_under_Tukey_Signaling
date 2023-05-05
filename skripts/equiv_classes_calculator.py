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
            eqv_class = self.equivalence_classes.get(int_damp_out,np.array([]))
            self.equivalence_classes[int_damp_out] = np.append(eqv_class,symbol_block)
        self.organize_equiv_classes_dictionary()
    
    def organize_equiv_classes_dictionary(self):
        # convert the entries of the dictionary from vectors to matrix
        # each row is a symbol_block in the same equivalence class
        for key, value in self.equivalence_classes.items():
            self.equivalence_classes[key] = np.reshape(value,(len(value)//self.symbol_block_length,self.symbol_block_length))

    def summarize_results(self):
        class_size_cnt = {}
        for key, value in self.equivalence_classes.items():
            class_size = np.shape(value)[0]
            class_size_cnt[class_size] = class_size_cnt.get(class_size,0) + 1
        total_classes = 0
        for key, value in class_size_cnt.items():
            print(str(key)+" : "+str(value))
            total_classes += value 
        print("total amount of classes: " + str(total_classes))