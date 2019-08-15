from random import choices
from algorithm.general_tools.option_probabilities import SCALE_DEGREES_INCREMENTS


class OctavedAbstractScale:

    def __init__(self, chromatic_single_octave_note_count, scale_degrees=None):
        self.chromatic_single_octave_note_count = chromatic_single_octave_note_count
        self.scale_degrees = scale_degrees or self.generate_scale_degrees()

    @property
    def scale_degrees(self):
        return self._scale_degrees

    @scale_degrees.setter
    def scale_degrees(self, scale_degrees):
        if max(scale_degrees) > self.chromatic_single_octave_note_count - 1:
            raise ValueError('Highest scale degree cannot be greater than the number of notes in a single octave')
        self._scale_degrees = scale_degrees

    def generate_scale_degrees(self):
        scale_degrees = list()
        current_degree = 0
        while True:
            current_degree += choices(SCALE_DEGREES_INCREMENTS.options,
                                      weights=SCALE_DEGREES_INCREMENTS.probabilities)[0]
            if current_degree > self.chromatic_single_octave_note_count - 1:
                break
            scale_degrees.append(current_degree)
        if not scale_degrees:
            scale_degrees = [1]
        return scale_degrees
