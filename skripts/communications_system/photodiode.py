import numpy as np


class Photodiode:

    responsivity = None
    sigma_sh = None
    sigma_th = None
    rng = None

    def __init__(self,responsivity, sigma2_sh, sigma_2_th, seed=None):
        self.responsivity = responsivity
        self.sigma_sh = np.sqrt(sigma2_sh)
        self.sigma_th = np.sqrt(sigma_2_th)
        self.rng = np.random.default_rng(seed)


    def square_law_detection(self,signal):
        abs_signal = np.abs(signal)
        square_law_signal = self.responsivity*abs_signal**2
        shot_noise = abs_signal * self.rng.normal(0, self.sigma_sh, size=np.shape(signal))
        thermal_noise = self.rng.normal(0, self.sigma_th, size=np.shape(signal))
        return square_law_signal + shot_noise + thermal_noise