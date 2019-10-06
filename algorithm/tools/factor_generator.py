from random import gauss


class FactorGenerator:

    def __init__(self, base_probability=None, base_standard_deviation=None):
        self.base_probability = self.set_base_probability(base_probability)
        self.base_standard_deviation = self.set_base_standard_deviation(base_standard_deviation)

    def set_base_probability(self, base_probability):
        if base_probability is None:
            return 0.5
        if (not isinstance(base_probability, float) and not isinstance(base_probability, int)) or \
                not 0 <= base_probability <= 1:
            raise ValueError('Base probability must be a float or int between 0.0 and 1.0')
        return base_probability

    def set_base_standard_deviation(self, base_standard_deviation):
        if base_standard_deviation is None:
            return 0.15
        if (not isinstance(base_standard_deviation, float) and not isinstance(base_standard_deviation, int)) or \
                not 0 <= base_standard_deviation <= 1:
            raise ValueError('Base standard deviation must be a float or int between 0.0 and 1.0')
        return base_standard_deviation

    def generate_factor(self, factor=None, probability=None, standard_deviation=None):
        if factor is not None:
            if (not isinstance(factor, float) and not isinstance(factor, int)) or \
                    not 0 <= factor <= 1:
                raise ValueError('Factor must be a float between 0.0 and 1.0')
            return factor
        base_probability = probability or self.base_probability
        if (not isinstance(base_probability, float) and not isinstance(base_probability, int)) or \
                not 0 <= base_probability <= 1:
            raise ValueError('Probability must be a float or int between 0.0 and 1.0')
        base_standard_deviation = standard_deviation or self.base_standard_deviation
        if (not isinstance(base_standard_deviation, float) and not isinstance(base_standard_deviation, int)) or \
                not 0 <= base_standard_deviation <= 1:
            raise ValueError('Standard deviation must be a float or int between 0.0 and 1.0')
        possible_factor = gauss(base_probability, base_standard_deviation)
        return max(0.0, min(1.0, possible_factor))
