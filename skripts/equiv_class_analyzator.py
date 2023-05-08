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

    def get_equiv_classes_of_size_n(self, class_size):
        classes_of_size_n = np.empty((0,class_size,self.symbol_block_length))
        for equiv_class in self.equivalence_classes.values():
            if np.shape(equiv_class)[0] == class_size:
                classes_of_size_n = np.append(classes_of_size_n, [equiv_class], axis=0)
        return classes_of_size_n
    
    def plot_constellation():
        pass

    def plot_symbol_block():
        pass

    def plot_equivalence_class():
        pass
