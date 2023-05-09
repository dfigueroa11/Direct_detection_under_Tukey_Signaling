import numpy as np


def n_roots_of_unity(n):
    return np.exp(2j*np.pi*np.arange(n)/n)


def nr_np_SQAM(radius_set, number_phase):
    constellation_base = n_roots_of_unity(number_phase)
    constellation = np.empty(0)
    for radius in radius_set:
        constellation = np.append(constellation,constellation_base*radius)
    return constellation

def n_ring_m_ary_phase(radius_set,m_ary):
    phase_shift = np.exp(2j*np.pi/(2*m_ary))
    return np.append(nr_np_SQAM(radius_set[::2],m_ary),phase_shift*nr_np_SQAM(radius_set[1::2],m_ary))