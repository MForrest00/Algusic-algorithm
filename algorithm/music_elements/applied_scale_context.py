from algorithm.music_elements.chromatic_context import TrueOctavedChromaticContext
from algorithm.music_elements.scale_context import OctavedScaleContext


class AppliedOctavedScaleContext:

    def __init__(self, chromatic_context, scale_context, scale_anchor=None):
        self.chromatic_context = chromatic_context
        self.scale_context = scale_context
        self.scale_anchor = scale_anchor
        self.flat_tonic_indexes = self.generate_flat_tonic_indexes()
        self.named_scale, self.named_altered_scale = self.generate_named_scale()

    @property
    def chromatic_context(self):
        return self._chromatic_context

    @chromatic_context.setter
    def chromatic_context(self, chromatic_context):
        if not isinstance(chromatic_context, TrueOctavedChromaticContext):
            raise Exception('Chromatic context must be of type TrueOctavedChromaticContext')
        self._chromatic_context = chromatic_context

    @property
    def scale_context(self):
        return self._scale_context

    @scale_context.setter
    def scale_context(self, scale_context):
        if not isinstance(scale_context, OctavedScaleContext):
            raise Exception('Scale context must be of type OctavedScaleContext')
        if scale_context.chromatic_single_octave_note_count != self.chromatic_context.single_octave_note_count:
            raise Exception('Scale context and chromatic context must have same single octave note count')
        self._scale_context = scale_context

    @property
    def scale(self):
        if not hasattr(self, '_scale'):
            self._scale = [[k for j in i for k in j.values()] for i in self.named_scale]
        return self._scale

    @property
    def altered_scale(self):
        if not hasattr(self, '_altered_scale'):
            self._altered_scale = [[k for j in i for k in j.values()] for i in self.named_altered_scale]
        return self._altered_scale

    @property
    def flat_named_scale(self):
        if not hasattr(self, '_flat_named_scale'):
            self._flat_named_scale = [note for single_octave_scale in self.named_scale for note in single_octave_scale]
        return self._flat_named_scale

    @property
    def flat_named_altered_scale(self):
        if not hasattr(self, '_flat_named_altered_scale'):
            self._flat_named_altered_scale = [note for single_octave_scale in self.named_altered_scale
                                              for note in single_octave_scale]
        return self._flat_named_altered_scale

    @property
    def flat_scale(self):
        if not hasattr(self, '_flat_scale'):
            self._flat_scale = [note for single_octave_scale in self.scale for note in single_octave_scale]
        return self._flat_scale

    @property
    def flat_altered_scale(self):
        if not hasattr(self, '_flat_altered_scale'):
            self._flat_altered_scale = [note for single_octave_scale in self.altered_scale
                                        for note in single_octave_scale]
        return self._flat_altered_scale

    def generate_flat_tonic_indexes(self):
        if isinstance(self.scale_anchor, str):
            note_names = [k for i in self.chromatic_context.flat_named_chromatic_scale for k, v in i.items()]
            return [i for i, note_name in enumerate(note_names)
                    if ''.join(j for j in note_name if not j.isdigit()) == self.scale_anchor]
        if isinstance(self.scale_anchor, int):
            scale_anchor = self.scale_anchor
        elif isinstance(self.scale_anchor, float):
            scale_anchor = self.chromatic_context.flat_chromatic_scale.index(self.scale_anchor)
        else:
            scale_anchor = self.chromatic_context.flat_chromatic_scale.index(self.chromatic_context.anchor_hz)
        tonic_indexes = [scale_anchor]
        while True:
            next_index = tonic_indexes[-1] + self.chromatic_context.single_octave_note_count
            if next_index > len(self.chromatic_context.flat_chromatic_scale) - 1:
                break
            tonic_indexes.append(next_index)
        negative_index_identified = False
        while True:
            if negative_index_identified:
                break
            next_index = tonic_indexes[0] - self.chromatic_context.single_octave_note_count
            tonic_indexes.insert(0, next_index)
            if next_index < 0:
                negative_index_identified = True
            elif next_index == 0:
                break
        return tonic_indexes

    def generate_named_scale(self):
        scale_octaves = []
        altered_scale_octaves = []
        for flat_tonic_index in self.flat_tonic_indexes:
            scale = []
            altered_scale = []
            for i in range(self.chromatic_context.single_octave_note_count):
                target_index = flat_tonic_index + i
                if target_index < 0:
                    continue
                if target_index > len(self.chromatic_context.flat_chromatic_scale) - 1:
                    break
                if i == 0 or i in self.scale_context.scale_degrees:
                    scale.append(self.chromatic_context.flat_named_chromatic_scale[target_index])
                else:
                    altered_scale.append(self.chromatic_context.flat_named_chromatic_scale[target_index])
            scale_octaves.append(scale)
            altered_scale_octaves.append(altered_scale)
        return scale_octaves, altered_scale_octaves
