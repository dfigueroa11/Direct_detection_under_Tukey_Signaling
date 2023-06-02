import numpy as np
import random

import equiv_classes_calculator
import constellation_maker as const_mk




def valid_representative_class(rep_class,constellation,symbol_block_len):
    s = set()
    test = equiv_classes_calculator.Equivalence_classes_calculator(constellation,symbol_block_len=symbol_block_len)
    for sym_block in rep_class:
        signature = test.integrate_and_dump_no_noise(test.generate_symbol_block(sym_block))
        if signature in s: return False
        s.add(signature)
    return True


def save_representative_class(file_in, sym_block_len, file_out, constellation, state=None, num_selected_classes=None):
    rng = np.random.default_rng()
    if state == None:
        state = rng.__getstate__()
    else:
        rng.__setstate__(state)
    equivalence_classes = np.load(file_in, allow_pickle=True).item()
    num_eq_classes = len(equivalence_classes)
    if num_selected_classes is None:
        num_selected_classes = int(2**np.floor(np.log2(num_eq_classes)))
    representative_class = np.empty(num_selected_classes, dtype=np.int32)
    keys = list(equivalence_classes.keys())
    for i, index_key in enumerate(rng.choice(num_eq_classes, size=num_selected_classes, replace=False)):
        eq_class = equivalence_classes.get(keys[index_key])
        sym_block = rng.choice(len(eq_class))
        representative_class[i] = eq_class[sym_block]
    if not valid_representative_class(representative_class,constellation,sym_block_len):
        print("error ocurred, not valid representative class")
        return
    np.save("../communications_system/representative_classes/"+file_out+".npy",representative_class)
    with open("../communications_system/representative_classes/"+file_out+".txt", 'w') as f:
        f.write("representative class done\n")
        f.write("symbol block length = {}\n".format(sym_block_len))
        f.write("number of different symbol blocks: {}\n".format(np.shape(representative_class)[0]))
        f.write("check numbers for rng: {}\n".format(rng.choice(1000,4)))
        f.write(str(state))





##############################################################################
file_in = "results/2-Ring_4-Ary/EqClasses_2-Ring_4-Ary_n3.npy"
sym_block_len = 3
constellation = const_mk.n_ring_m_ary_phase([2,np.pi],4)
file_out = "2-Ring_4-Ary_n3"
save_representative_class(file_in, sym_block_len, file_out, constellation)
