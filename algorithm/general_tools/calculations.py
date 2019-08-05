from itertools import combinations
from math import e


class VassilakisSRAModel:
    """Reference: http://www.acousticslab.org/learnmoresra/moremodel.html"""

    def __init__(self, sinusoids):
        self.sinusoids = sinusoids
        self.calculated_roughness = self.generate_roughness_value()

    @property
    def dissonance(self):
        return self.calculated_roughness

    def generate_roughness_value_from_pair(self, sinusoid_1, sinusoid_2):
        sinusoid_1_frequency, sinusoid_1_amplitude = sinusoid_1
        sinusoid_2_frequency, sinusoid_2_amplitude = sinusoid_2
        frequency_min = min(sinusoid_1_frequency, sinusoid_2_frequency)
        frequency_max = max(sinusoid_1_frequency, sinusoid_2_frequency)
        amplitude_min = min(sinusoid_1_amplitude, sinusoid_2_amplitude)
        amplitude_max = max(sinusoid_1_amplitude, sinusoid_2_amplitude)
        b1 = 3.5
        b2 = 5.75
        s1 = 0.0207
        s2 = 18.96
        s = 0.24 / ((s1 * frequency_min) + s2)
        X = amplitude_min * amplitude_max
        Y = (2 * amplitude_min) / (amplitude_min + amplitude_max)
        Z = pow(e, -1 * b1 * s * (frequency_max - frequency_min)) - pow(e, -1 * b2 * s * (frequency_max - frequency_min))
        return pow(X, 0.1) * 0.5 * pow(Y, 3.11) * Z

    def generate_roughness_value(self):
        if len(self.sinusoids) < 2:
            return 0
        roughness = 0
        for pair in combinations(self.sinusoids, 2):
            sinusoid_1, sinusoid_2 = pair
            roughness += self.generate_roughness_value_from_pair(sinusoid_1, sinusoid_2)
        return roughness

    def add_sinusoid(self, sinusoid):
        roughness = self.calculated_roughness
        for stored_sinusoid in self.sinusoids:
            roughness += self.generate_roughness_value_from_pair(sinusoid, stored_sinusoid)
        self.calculated_roughness = roughness
        self.sinusoids.append(sinusoid)

    def remove_sinusoid_by_index(self, index):
        sinusoid = self.sinusoids[index]
        roughness = self.calculated_roughness
        for i, stored_sinusoid in self.sinusoids:
            if i == index:
                continue
            roughness -= self.generate_roughness_value_from_pair(sinusoid, stored_sinusoid)
        self.calculated_roughness = roughness
        del self.sinusoids[index]
