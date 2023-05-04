import numpy as np

def integrate_and_dump_no_noise(symbol_block):
    ISI_free = np.abs(symbol_block)**2
    ISI_present = 1/4*np.abs(symbol_block[:-1]+symbol_block[1:])**2+1/8*np.abs(symbol_block[:-1]-symbol_block[1:])**2    
    return tuple(np.append(ISI_free , ISI_present))


def add_values_in_dict(dict, int_damp_out, symbol_block,):
    if int_damp_out not in dict:
        dict[int_damp_out] = np.array(symbol_block)
    else:
        dict[int_damp_out] = np.append(dict[int_damp_out],symbol_block)
    return dict

def numberToBase(n, b,len):
    digits = np.zeros(len, dtype=np.int64)
    if n == 0:
        return digits
    i = 0
    while n:
        digits[i] = int(n % b)
        n //= b
        i = i + 1
    return digits[::-1]

def generate_symbol_block(constellation, i, symbol_block_length):
    indices = numberToBase(i,len(constellation),symbol_block_length)
    return np.choose(indices,constellation)


################## definition of the communication scheme ##################
constellation = np.array([1, 1j, -1, -1j])
constellation = np.append(constellation,constellation*(1+np.sqrt(2)))
symbol_block_length = 3
############################################################################

equivalence_classes = {} 

for i in range(len(constellation)**symbol_block_length):
    symbol_block = generate_symbol_block(constellation,i,symbol_block_length)
    int_damp_out = integrate_and_dump_no_noise(symbol_block)
    add_values_in_dict(equivalence_classes,int_damp_out,symbol_block)


class_size_cnt = np.zeros(7)

for key, value in equivalence_classes.items():
    class_size = len(value)//symbol_block_length
    class_size_cnt[int(np.log2(class_size)-2)] += 1
    
print(class_size_cnt)
print(len(equivalence_classes.keys()))




