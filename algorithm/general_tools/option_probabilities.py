from collections import namedtuple


class OptionProbabilityContainer:

    def __init__(self, *option_probabilities):
        self.option_probabilities = option_probabilities

    @property
    def options(self):
        return [option_probability.option for option_probability in self.option_probabilities]
    
    @property
    def probabilities(self):
        return [option_probability.probability for option_probability in self.option_probabilities]


OptionProbability = namedtuple('OptionProbability', ['option', 'probability'])


SINGLE_OCTAVE_NOTE_COUNTS = OptionProbabilityContainer(OptionProbability(option=2, probability=0.5),
                                                       OptionProbability(option=3, probability=0.5),
                                                       OptionProbability(option=4, probability=1),
                                                       OptionProbability(option=5, probability=3),
                                                       OptionProbability(option=6, probability=4),
                                                       OptionProbability(option=7, probability=5),
                                                       OptionProbability(option=8, probability=6),
                                                       OptionProbability(option=9, probability=7),
                                                       OptionProbability(option=10, probability=8),
                                                       OptionProbability(option=11, probability=10),
                                                       OptionProbability(option=12, probability=11),
                                                       OptionProbability(option=13, probability=10),
                                                       OptionProbability(option=14, probability=9),
                                                       OptionProbability(option=15, probability=6),
                                                       OptionProbability(option=16, probability=5),
                                                       OptionProbability(option=17, probability=5),
                                                       OptionProbability(option=18, probability=4),
                                                       OptionProbability(option=19, probability=3),
                                                       OptionProbability(option=20, probability=2))
OCTAVE_RANGES = OptionProbabilityContainer(OptionProbability(option=1, probability=92),
                                           OptionProbability(option=2, probability=3),
                                           OptionProbability(option=3, probability=2),
                                           OptionProbability(option=4, probability=1),
                                           OptionProbability(option=5, probability=1),
                                           OptionProbability(option=6, probability=0.5),
                                           OptionProbability(option=7, probability=0.25),
                                           OptionProbability(option=8, probability=0.25))
