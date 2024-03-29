from dataclasses import dataclass
from typing import List


@dataclass
class OptionProbability:
    option: int
    probability: float


class OptionProbabilityContainer:
    def __init__(self, *option_probabilities: OptionProbability):
        self.option_probabilities = option_probabilities

    @property
    def options(self) -> List[int]:
        return [option_probability.option for option_probability in self.option_probabilities]

    @property
    def probabilities(self) -> List[float]:
        return [option_probability.probability for option_probability in self.option_probabilities]

    def __iter__(self):
        return iter(self.option_probabilities)


SINGLE_OCTAVE_NOTE_COUNTS = OptionProbabilityContainer(
    OptionProbability(option=2, probability=0.5),
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
    OptionProbability(option=20, probability=2),
)
OCTAVE_RANGES = OptionProbabilityContainer(
    OptionProbability(option=1, probability=92),
    OptionProbability(option=2, probability=3),
    OptionProbability(option=3, probability=2),
    OptionProbability(option=4, probability=1),
    OptionProbability(option=5, probability=1),
    OptionProbability(option=6, probability=0.5),
    OptionProbability(option=7, probability=0.25),
    OptionProbability(option=8, probability=0.25),
)
SCALE_DEGREES_INCREMENTS = OptionProbabilityContainer(
    OptionProbability(option=1, probability=25),
    OptionProbability(option=2, probability=60),
    OptionProbability(option=3, probability=10),
    OptionProbability(option=4, probability=2.5),
    OptionProbability(option=5, probability=1.25),
    OptionProbability(option=6, probability=1.25),
)
BAR_BEATS = OptionProbabilityContainer(
    OptionProbability(option=2, probability=85),
    OptionProbability(option=3, probability=10),
    OptionProbability(option=5, probability=2),
    OptionProbability(option=7, probability=1),
    OptionProbability(option=11, probability=0.75),
    OptionProbability(option=13, probability=0.5),
    OptionProbability(option=17, probability=0.25),
    OptionProbability(option=19, probability=0.25),
    OptionProbability(option=23, probability=0.25),
)
