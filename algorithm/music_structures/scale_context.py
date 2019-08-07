from random import choices, randint
from algorithm.general_tools.option_probabilities import SCALE_DEGREES_INCREMENT


class ScaleContext:

    def __init__(self, chromatic_context, fundamental_index=None):
        self.chromatic_context = chromatic_context


class TrueOctavedScaleContext(ScaleContext):

    def __init__(self, chromatic_context, scale_degrees=None, **kwargs):
        super().__init__(chromatic_context, **kwargs)
        self.scale_degrees = scale_degrees or self.generate_scale_degrees

    @property
    def scale_degrees(self):
        return self._scale_degrees

    @scale_degrees.setter
    def scale_degrees(self, scale_degrees):
        if max(scale_degrees) > self.chromatic_context.single_octave_note_count - 1:
            raise Exception('Highest scale degree cannot be greater than the highest note in a single octave')
        self._scale_degrees = scale_degrees

    def generate_scale_degrees(self):
        scale_degrees = []
        current_degree = 0
        while True:
            current_degree += choices(SCALE_DEGREES_INCREMENT.options, weights=SCALE_DEGREES_INCREMENT.probabilities)[0]
            if current_degree > self.chromatic_context.single_octave_note_count - 1:
                break
            scale_degrees.append(current_degree)
        if not scale_degrees:
            scale_degrees = [1]
        return scale_degrees


class EqualTemperedTrueOctavedScaleContext(TrueOctavedScaleContext):

    def __init__(self, chromatic_context, tonic_index=None, **kwargs):
        super().__init__(chromatic_context, **kwargs)
        self.tonic_index = tonic_index or randint(0, len(self.chromatic_context.flat_chromatic_scale))


class UnequalTemperedTrueOctavedScaleContext(TrueOctavedScaleContext):

    def __init__(self, chromatic_context, **kwargs):
        super().__init__(chromatic_context, **kwargs)

    @property
    def tonic_index(self):
        return self.chromatic_context.flat_chromatic_scale.index(self.chromatic_context.anchor_hz)
