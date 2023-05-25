import numpy as np

class Class_representative_block:

    representative_class = None
    symbol_block_lenght = None
    representative_class_size = None

    def __init__(self, rep_class_file):
        self.representative_class = np.load(rep_class_file)
        self.symbol_block_lenght = np.shape(self.representative_class)[1]
        self.representative_class_size = np.shape(self.representative_class)[0]
    
    def get_symbol_blocks(self, k_vec):
        symbol_blocks = np.empty(shape=self.symbol_block_lenght*len(k_vec),dtype=complex)
        for i,k in enumerate(k_vec):
            symbol_blocks[i*self.symbol_block_lenght:(i+1)*self.symbol_block_lenght] = self.representative_class[k,:]
        return symbol_blocks