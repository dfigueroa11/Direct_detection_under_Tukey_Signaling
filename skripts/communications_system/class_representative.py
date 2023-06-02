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
    
    def get_symbol_blocks(self,k_vec):
        base = len(self.constellation)
        indices = np.zeros(self.symbol_block_length*len(k_vec), dtype=np.int32)
        i = 0
        for sym in self.representative_class[k_vec]:
            for j in range(self.symbol_block_length):
                indices[i] = int(sym % base)
                sym //= base
                i = i + 1
        return self.constellation[indices]

