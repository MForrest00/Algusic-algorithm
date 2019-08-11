from algorithm.music_elements.applied_scale_context import AppliedOctavedScaleContext
from algorithm.music_elements.chord_context import OctavedChordContext


class AppliedOctavedChordContext:

    def __init__(self, applied_scale_context, chord_context, chord_anchor=None):
        self.applied_scale_context = applied_scale_context
        self.chord_context = chord_context
        self.chord_anchor = chord_anchor or self.applied_scale_context.scale_anchor
        self.chord = self.generate_chord()

    @property
    def applied_scale_context(self):
        return self._applied_scale_context

    @applied_scale_context.setter
    def applied_scale_context(self, applied_scale_context):
        if not isinstance(applied_scale_context, AppliedOctavedScaleContext):
            raise TypeError('Applied scale context must be of type AppliedOctavedScaleContext')
        self._applied_scale_context = applied_scale_context

    @property
    def chord_context(self):
        return self._chord_context

    @chord_context.setter
    def chord_context(self, chord_context):
        if not isinstance(chord_context, OctavedChordContext):
            raise TypeError('Chord context must be of type OctavedChordContext')
        self._chord_context = chord_context

    def generate_chord(self):
        if isinstance(self.chord_anchor, str):
            note_names = [k for i in self.applied_scale_context.chromatic_context.flat_named_chromatic_scale
                          for k, v in i.items()]
            chord_anchor = note_names.index(self.chord_anchor)
        elif isinstance(self.chord_anchor, int):
            chord_anchor = self.chord_anchor
        else:
            chord_anchor = self.applied_scale_context.chromatic_context.flat_chromatic_scale.index(self.chord_anchor)
        chord = [self.applied_scale_context.chromatic_context.flat_chromatic_scale[chord_anchor]]
        for chord_degree in self.chord_context.chord_degrees:
            chord.append(self.applied_scale_context.chromatic_context.flat_chromatic_scale[chord_anchor + chord_degree])
        return chord
