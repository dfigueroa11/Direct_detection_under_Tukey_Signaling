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

def n_QAM(M):
    constellation = np.zeros(M, dtype=complex)
    if int( np.sqrt( M ) ) == np.sqrt( M ):
        k = int( np.log2( M ) )
        for m in range(0,M):
            b_bin = np.binary_repr( m, width=k)
            b = [ (-1)**( int(x) ) for x in b_bin]
            d = np.sqrt( M ) / 2
            dx = 1
            dy = 1
            s = 0 + 1j*0
            for n in np.arange(0, int(k/2)):
                dx *= b[ 2*n ]
                dy *= b[ 2*n + 1 ]
                s += d * ( dx + 1j * dy )
                d = d/2;
            constellation[ m ] = s
    elif int(np.sqrt(2*M)) == np.sqrt(2*M):
        const_temp = n_QAM( 2*M )
        constellation = [c for c in const_temp if np.imag(c)<0]
        constellation -= np.average( constellation )
    return constellation

def normalize_constellation_x_dBm(constellation, dBm=0):
    p_lin = 10**(dBm/10-3)
    p_const = np.mean(np.abs(constellation)**2)
    return constellation*np.sqrt(p_lin/p_const)