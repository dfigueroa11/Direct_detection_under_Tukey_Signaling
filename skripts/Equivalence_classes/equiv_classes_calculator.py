import numpy as np


class Equivalence_classes_calculator:
    
    constellation = None
    constellation_name = None
    symbol_block_length = None
    equivalence_classes = None

            
    def __init__(self,constell=None,constell_name=None,symbol_block_len=None):
        self.constellation =   constell
        self.symbol_block_length = symbol_block_len
        self.constellation_name = constell_name

    ################# main algorithm to find the equivalent classes

    def calculate_equivalence_classes(self):
        self.equivalence_classes = {}
        for n in range(len(self.constellation)**self.symbol_block_length):
            symbol_block = self.generate_symbol_block(n)
            int_dump_out = self.integrate_and_dump_no_noise(symbol_block)
            eqv_class = self.equivalence_classes.get(int_dump_out,np.empty((0,1),dtype=np.int32))
            self.equivalence_classes[int_dump_out] = np.append(eqv_class, n)
        
    def generate_symbol_block(self,num):
        indices = self.numberToBaseN(num)
        return self.constellation[indices]

    def numberToBaseN(self, num):
        b = len(self.constellation)
        digits = np.zeros(self.symbol_block_length, dtype=np.int32)
        i = 0
        while num:
            digits[i] = int(num % b)
            num //= b
            i = i + 1
        return digits

    def integrate_and_dump_no_noise(self,symbol_block):
        ISI_free = np.abs(symbol_block)**2
        ISI_present = 1/4*np.abs(symbol_block[:-1]+symbol_block[1:])**2+1/8*np.abs(symbol_block[:-1]-symbol_block[1:])**2    
        return tuple(np.around(np.append(ISI_free , ISI_present),5))

    ################# saving and printing results functions
    
    def save_results(self, path, calc_time):
        file_name = "EqClasses_" + self.constellation_name + "_n" + str(self.symbol_block_length) + ".npy"
        np.save(path+file_name,self.equivalence_classes)
        file_name = "Summary_EqClasses_" + self.constellation_name + "_n" + str(self.symbol_block_length) + ".txt"
        with open(path+file_name,"w") as file:
            file = open(path+file_name,"w")
            self.print_info(file.write)
            file.write("--- %s seconds ---\n" % (calc_time))

    def print_info(self, print_target=print):
        print_target("For the constellation {}\n".format(self.constellation_name))
        print_target("and symbol block length n = "+str(self.symbol_block_length)+"\n")
        self.summarize_results(print_target)

    def summarize_results(self, print_target = print):
        class_size_cnt = {}
        for key, value in self.equivalence_classes.items():
            class_size = len(value)
            class_size_cnt[class_size] = class_size_cnt.get(class_size,0) + 1
        total_classes = 0
        print_target("Class size \tNumber of classes\n")
        for key, value in class_size_cnt.items():
            print_target(str(key)+"\t\t"+str(value)+"\n")
            total_classes += value 
        rate_loss = 1/self.symbol_block_length*np.log2(len(self.constellation)**self.symbol_block_length/total_classes)
        print_target("total amount of equivalence classes: " + str(total_classes)+"\n")
        print_target("rate loss: "+str(rate_loss)+" [bit/sym]\n")
