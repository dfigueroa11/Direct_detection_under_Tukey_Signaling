import numpy as np
import matplotlib
import matplotlib.pyplot as plt

class Equiv_class_analyzator:
    
    equivalence_classes = None
    symbol_block_length = None

    def __init__(self, file_name,symbol_block_length):
        self.equivalence_classes = self.load_equiv_classes_file(file_name)
        self.symbol_block_length = symbol_block_length

    def load_equiv_classes_file(self, file_name):
        return np.load(file_name, allow_pickle=True).item()

    def get_equiv_classes_of_size_n(self, class_size, num_classes=0):
        if not num_classes:
            print("Give the expected number of classes")
            return None
        
        classes_of_size_n = np.empty((num_classes,class_size,self.symbol_block_length),dtype=np.complex64)
        i = 0
        for equiv_class in self.equivalence_classes.values():
            if np.shape(equiv_class)[0] == class_size:
                classes_of_size_n[i,:,:] = equiv_class
                i += 1
            if i == num_classes:
                return classes_of_size_n
            
        print("warning!! fewer classes found than expected")
        return classes_of_size_n
    
    def plot_constellation(self, constellation, new_fig=False, figsize=(8,8), alpha=0.7, c=[[0.7,0.7,0.7]]):
        if new_fig:
            plt.figure(figsize=figsize)
        plt.scatter(np.real(constellation),np.imag(constellation), alpha=alpha, c=c)

    def plot_symbol_block(self,symbol_block, new_fig=False, figsize=(8,8), color='blue', alpha=1):
        if new_fig:
            plt.figure(figsize=figsize)
        plt.plot(np.real(symbol_block), np.imag(symbol_block), 'o:', color=color, alpha=alpha, fillstyle='none')
        plt.plot(np.real(symbol_block[0]), np.imag(symbol_block[0]), '*:', color=color)
        
    def plot_equivalence_class(self, equivalence_class, new_fig=False, figsize=(8,8), alpha=1):
        if new_fig:
            plt.figure(figsize=figsize)
        for symbol_block in range(np.shape(equivalence_class)[0]):
            self.plot_symbol_block(equivalence_class[symbol_block,:],color='C{}'.format(symbol_block),alpha=alpha)

    def plot_all_equivalence_classes(self, equivalence_classes, constellation):
        for i in range(np.shape(equivalence_classes)[0]):
            plt.figure(i,(8,8))
            self.plot_constellation(constellation)
            self.plot_equivalence_class(equivalence_classes[i,:,:])
        plt.xlabel("Re")
        plt.ylabel("Im")