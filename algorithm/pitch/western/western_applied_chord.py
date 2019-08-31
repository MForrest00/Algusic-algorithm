from algorithm.pitch.applied_chord import AppliedOctavedChord
from algorithm.pitch.western.western_abstract_chord import WesternOctavedAbstractChord
from algorithm.pitch.western.western_applied_scale import WesternAppliedScale


class WesternAppliedChord(AppliedOctavedChord):

    def __init__(self, applied_scale, abstract_chord, chord_anchor=None):
        super().__init__(applied_scale, abstract_chord, chord_anchor)

    @property
    def applied_scale(self):
        return self._applied_scale

    @applied_scale.setter
    def applied_scale(self, applied_scale):
        if not isinstance(applied_scale, WesternAppliedScale):
            raise TypeError('Applied scale must be of type WesternAppliedScale')
        self._applied_scale = applied_scale

    @property
    def abstract_chord(self):
        return self._abstract_chord

    @abstract_chord.setter
    def abstract_chord(self, abstract_chord):
        if not isinstance(abstract_chord, WesternOctavedAbstractChord):
            raise TypeError('Abstract chord must be of type WesternOctavedAbstractChord')
        self._abstract_chord = abstract_chord

    @property
    def name(self):
        if not hasattr(self, '_name'):
            if isinstance(self.chord_anchor, str):
                note_name = self.chord_anchor
            else:
                if isinstance(self.chord_anchor, int):
                    target_index = self.chord_anchor
                else:
                    target_index = self.applied_scale.chromatic_context.flat_chromatic_scale.index(self.chord_anchor)
                note_name = self.applied_scale.chromatic_context.flat_note_names[target_index]
            note_name = ''.join(j for j in note_name if not j.isdigit())
            self._name = self.abstract_chord.render_name(note_name)
        return self._name
