from algorithm.pitch.abstract_scale import OctavedAbstractScale
from algorithm.pitch.chromatic_context import TrueOctavedChromaticContext


class AppliedOctavedScale:

    def __init__(self, chromatic_context, abstract_scale, scale_anchor=None):
        self.chromatic_context = chromatic_context
        self.abstract_scale = abstract_scale
        self.scale_anchor = scale_anchor or self.chromatic_context.anchor_hz
        self.flat_tonic_indexes, self.scale_note = self.generate_flat_tonic_indexes()
        self.named_scale, self.altered_named_scale = self.generate_named_scale()

    @property
    def chromatic_context(self):
        return self._chromatic_context

    @chromatic_context.setter
    def chromatic_context(self, chromatic_context):
        if not isinstance(chromatic_context, TrueOctavedChromaticContext):
            raise TypeError('Chromatic context must be of type TrueOctavedChromaticContext')
        self._chromatic_context = chromatic_context

    @property
    def abstract_scale(self):
        return self._abstract_scale

    @abstract_scale.setter
    def abstract_scale(self, abstract_scale):
        if not isinstance(abstract_scale, OctavedAbstractScale):
            raise TypeError('Abstract scale must be of type OctavedAbstractScale')
        if abstract_scale.chromatic_single_octave_note_count != self.chromatic_context.single_octave_note_count:
            raise ValueError('Abstract scale and chromatic context must have same single octave note count')
        self._abstract_scale = abstract_scale

    @property
    def flat_named_scale(self):
        if not hasattr(self, '_flat_named_scale'):
            self._flat_named_scale = [note for single_octave_scale in self.named_scale for note in single_octave_scale]
        return self._flat_named_scale

    @property
    def flat_altered_named_scale(self):
        if not hasattr(self, '_flat_altered_named_scale'):
            self._flat_altered_named_scale = [note for single_octave_scale in self.altered_named_scale
                                              for note in single_octave_scale]
        return self._flat_altered_named_scale

    @property
    def scale(self):
        if not hasattr(self, '_scale'):
            self._scale = [[note for name, note in single_octave_scale] for single_octave_scale in self.named_scale]
        return self._scale

    @property
    def flat_scale(self):
        if not hasattr(self, '_flat_scale'):
            self._flat_scale = [note for single_octave_scale in self.scale for note in single_octave_scale]
        return self._flat_scale

    @property
    def note_names(self):
        if not hasattr(self, '_note_names'):
            self._note_names = [[name for name, note in single_octave_scale]
                                for single_octave_scale in self.named_scale]
        return self._note_names

    @property
    def flat_note_names(self):
        if not hasattr(self, '_flat_note_names'):
            self._flat_note_names = [note for single_octave_scale in self.note_names for note in single_octave_scale]
        return self._flat_note_names

    @property
    def altered_scale(self):
        if not hasattr(self, '_altered_scale'):
            self._altered_scale = [[note for name, note in single_octave_scale]
                                   for single_octave_scale in self.altered_named_scale]
        return self._altered_scale

    @property
    def flat_altered_scale(self):
        if not hasattr(self, '_flat_altered_scale'):
            self._flat_altered_scale = [note for single_octave_scale in self.altered_scale
                                        for note in single_octave_scale]
        return self._flat_altered_scale

    @property
    def altered_note_names(self):
        if not hasattr(self, '_altered_note_names'):
            self._altered_note_names = [[name for name, note in single_octave_scale]
                                        for single_octave_scale in self.altered_named_scale]
        return self._altered_note_names

    @property
    def flat_altered_note_names(self):
        if not hasattr(self, '_flat_altered_note_names'):
            self._flat_altered_note_names = [note for single_octave_scale in self.altered_note_names
                                             for note in single_octave_scale]
        return self._flat_altered_note_names

    def generate_flat_tonic_indexes(self):
        if isinstance(self.scale_anchor, str) and not any(j for j in self.scale_anchor if j.isdigit()):
            target_note = self.scale_anchor
        else:
            if isinstance(self.scale_anchor, int):
                target_index = self.scale_anchor
            elif isinstance(self.scale_anchor, float):
                target_index = self.chromatic_context.flat_chromatic_scale.index(self.scale_anchor)
            else:
                target_index = self.chromatic_context.flat_note_names.index(self.scale_anchor)
            target_note = ''.join(i for i in self.chromatic_context.flat_note_names[target_index]
                                  if not i.isdigit())
        tonic_indexes = [i for i, note_name in enumerate(self.chromatic_context.flat_note_names)
                         if ''.join(j for j in note_name if not j.isdigit()) == target_note]
        if not tonic_indexes:
            raise ValueError('Scale anchor must be present in the chromatic context')
        if tonic_indexes[0] != 0:
            tonic_indexes.insert(0, tonic_indexes[0] - self.chromatic_context.single_octave_note_count)
        return tonic_indexes, target_note

    def generate_named_scale(self):
        scale_octaves = list()
        altered_scale_octaves = list()
        for flat_tonic_index in self.flat_tonic_indexes:
            scale = list()
            altered_scale = list()
            for i in range(self.chromatic_context.single_octave_note_count):
                target_index = flat_tonic_index + i
                if target_index < 0:
                    continue
                if target_index >= len(self.chromatic_context.flat_named_chromatic_scale):
                    break
                if i == 0 or i in self.abstract_scale.scale_degrees:
                    scale.append(self.chromatic_context.flat_named_chromatic_scale[target_index])
                else:
                    altered_scale.append(self.chromatic_context.flat_named_chromatic_scale[target_index])
            scale_octaves.append(scale)
            altered_scale_octaves.append(altered_scale)
        return scale_octaves, altered_scale_octaves
