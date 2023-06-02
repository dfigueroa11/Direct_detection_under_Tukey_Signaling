import numpy as np

class Class_representative_block:

    representative_class = None
    symbol_block_length = None
    representative_class_size = None
    constellation = None

    def __init__(self, rep_class_file, constellation, symbol_block_len):
        self.symbol_block_length = symbol_block_len
        self.constellation = constellation
        self.representative_class = self.load_rep_class(rep_class_file)
        self.representative_class_size = len(self.representative_class)

    def get_symbol_blocks(self, k_vec):
        symbol_blocks = np.empty(shape=self.symbol_block_length*len(k_vec),dtype=complex)
        for i,k in enumerate(k_vec):
            symbol_blocks[i*self.symbol_block_length:(i+1)*self.symbol_block_length] = self.representative_class[k,:]
        return symbol_blocks

    def load_rep_class(self, rep_class_file):
        nums = np.load(rep_class_file)
        representative_class = np.empty((len(nums),self.symbol_block_length), dtype=complex)
        for i, num in enumerate(nums):
            representative_class[i,:] = self.num_2_symbol_block(num)
        return representative_class
        
    def num_2_symbol_block(self,num):
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