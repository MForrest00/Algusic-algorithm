from random import gauss


class FactorGenerator:
    BASE_PROBABILITY = 0.5
    BASE_STANDARD_DEVIATION = 0.15

    def __init__(self, base_probability=None, base_standard_deviation=None):
        self.base_probability = self.set_base_probability(base_probability)
        self.base_standard_deviation = self.set_base_standard_deviation(base_standard_deviation)

    def set_base_probability(self, base_probability):
        if base_probability is None:
            return FactorGenerator.BASE_PROBABILITY
        if not isinstance(base_probability, (int, float)):
            raise TypeError('Base probability must be an integer or float')
        if not 0 <= base_probability <= 1:
            raise ValueError('Base probability must be between 0.0 and 1.0')
        return float(base_probability)

    def set_base_standard_deviation(self, base_standard_deviation):
        if base_standard_deviation is None:
            return FactorGenerator.BASE_STANDARD_DEVIATION
        if not isinstance(base_standard_deviation, (int, float)):
            raise TypeError('Base standard deviation must be an integer or float')
        if not 0 <= base_standard_deviation <= 1:
            raise ValueError('Base standard deviation must be between 0.0 and 1.0')
        return float(base_standard_deviation)

    def generate_factor(self, factor=None, probability=None, standard_deviation=None):
        if factor is not None:
            if not isinstance(factor, (int, float)):
                raise TypeError('Factor must be an integer or float')
            if not 0 <= factor <= 1:
                raise ValueError('Factor must be between 0.0 and 1.0')
            return float(factor)
        base_probability = probability or self.base_probability
        if not isinstance(base_probability, (int, float)):
            raise TypeError('Probability must be an integer or float')
        if not 0 <= base_probability <= 1:
            raise ValueError('Probability must be between 0.0 and 1.0')
        base_standard_deviation = standard_deviation or self.base_standard_deviation
        if not isinstance(base_standard_deviation, (int, float)):
            raise TypeError('Standard deviation must be an integer or float')
        if not 0 <= base_standard_deviation <= 1:
            raise ValueError('Standard deviation must be between 0.0 and 1.0')
        possible_factor = gauss(base_probability, base_standard_deviation)
        return max(0.0, min(1.0, possible_factor))
