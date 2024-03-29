from algorithm.pitch.abstract_chord import OctavedAbstractChord
from algorithm.pitch.applied_scale import AppliedOctavedScale


class AppliedOctavedChord:
    def __init__(self, applied_scale, abstract_chord, chord_anchor=None):
        self.applied_scale = applied_scale
        self.abstract_chord = abstract_chord
        self.chord_anchor = chord_anchor or self.applied_scale.scale_anchor
        self.chord = self.generate_chord()

    @property
    def applied_scale(self):
        return self._applied_scale

    @applied_scale.setter
    def applied_scale(self, applied_scale):
        if not isinstance(applied_scale, AppliedOctavedScale):
            raise TypeError("Applied scale must be of type AppliedOctavedScale")
        self._applied_scale = applied_scale

    @property
    def abstract_chord(self):
        return self._abstract_chord

    @abstract_chord.setter
    def abstract_chord(self, abstract_chord):
        if not isinstance(abstract_chord, OctavedAbstractChord):
            raise TypeError("Abstract chord must be of type OctavedAbstractChord")
        self._abstract_chord = abstract_chord

    @property
    def symbol(self):
        if not hasattr(self, "_symbol"):
            if isinstance(self.chord_anchor, str):
                note_name = self.chord_anchor
            else:
                if isinstance(self.chord_anchor, int):
                    target_index = self.chord_anchor
                else:
                    target_index = self.applied_scale.chromatic_context.flat_chromatic_scale.index(self.chord_anchor)
                note_name = self.applied_scale.chromatic_context.flat_note_names[target_index]
            note_name = "".join(j for j in note_name if not j.isdigit())
            self._symbol = self.abstract_chord.render_symbol(note_name)
        return self._symbol

    @property
    def chord_in_scale(self):
        return len(set(self.chord) - set(self.applied_scale.flat_scale)) == 0

    @property
    def chord_degrees_in_scale(self):
        single_octave_chord_degrees = set(
            [
                d % self.applied_scale.chromatic_context.single_octave_note_count
                for d in self.abstract_chord.chord_degrees
            ]
        )
        return len(single_octave_chord_degrees - set([0] + self.applied_scale.abstract_scale.scale_degrees)) == 0

    def generate_chord(self):
        if isinstance(self.chord_anchor, int):
            target_index = self.chord_anchor
        elif isinstance(self.chord_anchor, float):
            target_index = self.applied_scale.chromatic_context.flat_chromatic_scale.index(self.chord_anchor)
        else:
            target_index = self.applied_scale.chromatic_context.flat_note_names.index(self.chord_anchor)
        chord = [self.applied_scale.chromatic_context.flat_chromatic_scale[target_index]]
        for chord_degree in self.abstract_chord.chord_degrees:
            if target_index + chord_degree >= len(self.applied_scale.chromatic_context.flat_chromatic_scale):
                break
            chord.append(self.applied_scale.chromatic_context.flat_chromatic_scale[target_index + chord_degree])
        return chord
