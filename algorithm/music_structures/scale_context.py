from random import randint


class ScaleContext:

    def __init__(self, chromatic_context, fundamental_index=None):
        self.chromatic_context = chromatic_context
        self.fundamental_index = fundamental_index or randint(0, len(self.chromatic_context.flat_chromatic_scale))


class TrueOctavedScaleContext(ScaleContext):

    def __init__(self, chromatic_context, scale_degrees=None, **kwargs):
        super().__init__(chromatic_context, **kwargs)
        self.scale_degrees = scale_degrees

    @property
    def scale_degrees(self):
        return self._scale_degrees
    
    @scale_degrees.setter
    def scale_degrees(self, scale_degrees):
        if max(scale_degrees) > self.chromatic_context.single_octave_note_count - 1:
            raise Exception('Highest scale degree cannot be greater than the highest note in a single octave')
        self._scale_degrees = scale_degrees
