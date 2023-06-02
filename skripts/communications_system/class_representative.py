import numpy as np

class Class_representative_block:

    representative_class = None
    symbol_block_length = None
    representative_class_size = None
    constellation = None

    def __init__(self, rep_class_file, constellation, symbol_block_len):
        self.representative_class = np.load(rep_class_file)
        self.symbol_block_length = symbol_block_len
        self.constellation = constellation
        self.representative_class_size = len(self.representative_class)
    
    def get_symbol_blocks(self, k_vec):
        symbol_blocks = np.empty(shape=self.symbol_block_length*len(k_vec),dtype=complex)
        for i,k in enumerate(k_vec):
            symbol_blocks[i*self.symbol_block_length:(i+1)*self.symbol_block_length] = self.generate_symbol_block(self.representative_class[k])
        return symbol_blocks
    
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
