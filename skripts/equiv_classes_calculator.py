import numpy as np


class Equivalence_classes_calculator:
    constellation = None
    constellation_name = None
    symbol_block_length = None
    equivalence_classes = None
    
    def __init__(self,constell,constell_name,symbol_block_len):
        self.constellation =   constell
        self.symbol_block_length = symbol_block_len
        self.constellation_name = constell_name

    def __init__(self,constell,constell_name):
        self.constellation =   constell
        self.constellation_name = constell_name

    ################# main algorithm to find the equivalent classes

    def calculate_equivalence_classes(self):
        self.equivalence_classes = {}
        for n in range(len(self.constellation)**self.symbol_block_length):
            symbol_block = self.generate_symbol_block(n)
            int_damp_out = self.integrate_and_dump_no_noise(symbol_block)
            eqv_class = self.equivalence_classes.get(int_damp_out,np.empty((0,self.symbol_block_length)))
            self.equivalence_classes[int_damp_out] = np.append(eqv_class, [symbol_block], axis=0)
        
    def generate_symbol_block(self,n):
        indices = self.numberToBaseN(n)
        return np.choose(indices,self.constellation)

    def numberToBaseN(self, n):
        b = len(self.constellation)
        digits = np.zeros(self.symbol_block_length, dtype=np.int64)
        i = 0
        while n:
            digits[i] = int(n % b)
            n //= b
            i = i + 1
        return digits

    def integrate_and_dump_no_noise(self,symbol_block):
        ISI_free = np.abs(symbol_block)**2
        ISI_present = 1/4*np.abs(symbol_block[:-1]+symbol_block[1:])**2+1/8*np.abs(symbol_block[:-1]-symbol_block[1:])**2    
        return tuple(np.around(np.append(ISI_free , ISI_present),5))

    ################# saving and printing results functions
    
    def save_results(self, path, calc_tiem):
        file_name = "EqClasses_" + self.constellation_name + "_n" + str(self.symbol_block_length) + ".npy"
        np.save(path+file_name,self.equivalence_classes)
        file_name = "Summary_EqClasses_" + self.constellation_name + "_n" + str(self.symbol_block_length) + ".txt"
        file = open(path+file_name,"w")
        self.print_info(file.write)
        file.write("--- %s seconds ---\n" % (calc_tiem))
        file.close()

    def print_info(self, print_target=print):
        print_target("For the constellation "+ self.constellation_name + " with points:\n")
        print_target(np.array2string(self.constellation, precision = 4, separator = "\n",
                                     prefix="",suffix="\n"))
        print_target("\nand symbol block length n = "+str(self.symbol_block_length)+"\n")
        self.summarize_results(print_target)

    def summarize_results(self, print_target = print):
        class_size_cnt = {}
        for key, value in self.equivalence_classes.items():
            class_size = np.shape(value)[0]
            class_size_cnt[class_size] = class_size_cnt.get(class_size,0) + 1
        total_classes = 0
        print_target("Class size \tNumber of classes\n")
        for key, value in class_size_cnt.items():
            print_target(str(key)+"\t\t"+str(value)+"\n")
            total_classes += value 
        rate_loss = 1/self.symbol_block_length*np.log2(len(self.constellation)**self.symbol_block_length/total_classes)
        print_target("total amount ocf classes equivalence classes: " + str(total_classes)+"\n")
        print_target("rate loss: "+str(rate_loss)+" [bit/sym]\n")
