import numpy as np

class Class_representative_block:

    __representative_class_file__ = None
    representative_class = None
    symbol_block_length = None
    constellation = None

    def __init__(self, rep_class_file, symbol_block_len):
        self.symbol_block_length = symbol_block_len
        self.__representative_class_file__ = np.load(rep_class_file)

    def get_symbol_blocks(self, k_vec):
        symbol_blocks = np.empty(shape=self.symbol_block_length*len(k_vec),dtype=complex)
        for i,k in enumerate(k_vec):
            symbol_blocks[i*self.symbol_block_length:(i+1)*self.symbol_block_length] = self.representative_class[k,:]
        return symbol_blocks

    def set_up_const_and_rep_class(self, constellation):
        nums = self.__representative_class_file__
        self.constellation = constellation
        self.representative_class = np.empty((len(nums),self.symbol_block_length), dtype=complex)
        for i, num in enumerate(nums):
            self.representative_class[i,:] = self.num_2_symbol_block(num)
        
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