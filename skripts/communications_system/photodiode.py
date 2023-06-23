import numpy as np
from scipy.constants import Boltzmann
from scipy.constants import e


class Photodiode:

    responsivity = None
    sigma_sh = None
    sigma_th = None
    rng = None

    def __init__(self,responsivity, sigma2_sh, sigma2_th, seed=None):
        self.responsivity = responsivity
        self.sigma_sh = np.sqrt(sigma2_sh)
        self.sigma_th = np.sqrt(sigma2_th)
        self.rng = np.random.default_rng(seed)


    def square_law_detection(self,signal):
        abs_signal = np.abs(signal)
        square_law_signal = self.responsivity*abs_signal**2
        shot_noise = abs_signal * self.rng.normal(0, self.sigma_sh, size=np.shape(signal))
        thermal_noise = self.rng.normal(0, self.sigma_th, size=np.shape(signal))
        return square_law_signal + shot_noise + thermal_noise
    
def get_sigma2_sh(M_APD,F,R_APD, BW_2side):
    R_D = R_APD/M_APD
    return e*M_APD**2*F*R_D*BW_2side


def get_sigma2_th(Tk,RL,BW_2side):
    return 2*Boltzmann*Tk/RL*BW_2side