from algorithm.pitch.chromatic_context import EqualTemperedTrueOctavedChromaticContext, \
    TrueOctavedChromaticContext, UnequalTemperedTrueOctavedChromaticContext


__all__ = ['WesternEqualTempered432ChromaticContext', 'WesternEqualTempered434ChromaticContext',
           'WesternEqualTempered436ChromaticContext', 'WesternEqualTempered438ChromaticContext',
           'WesternEqualTempered440ChromaticContext', 'WesternEqualTempered442ChromaticContext',
           'WesternEqualTempered444ChromaticContext', 'WesternEqualTempered446ChromaticContext',
           'WesternJustTemperedA440ChromaticContext']


class WesternChromaticContext(TrueOctavedChromaticContext):
    NOTE_NAMES = ['A', 'A♯/B♭', 'B', 'C', 'C♯/D♭', 'D', 'D♯/E♭', 'E', 'F', 'F♯/G♭', 'G', 'G♯/A♭']

    def __init__(self, **kwargs):
        super().__init__(octave_range=1, **kwargs)

    @property
    def anchor_note_name(self):
        if not hasattr(self, '_anchor_note_name'):
            return 'A'
        return self._anchor_note_name

    @anchor_note_name.setter
    def anchor_note_name(self, anchor_note_name):
        self._anchor_note_name = anchor_note_name

    def generate_note_name_components(self):
        note_index = WesternChromaticContext.NOTE_NAMES.index(self.anchor_note_name)
        ordered_note_names = WesternChromaticContext.NOTE_NAMES[note_index:] + \
            WesternChromaticContext.NOTE_NAMES[:note_index]
        note_name_components = list()
        c_encountered = False
        for ordered_note_name in ordered_note_names:
            if ordered_note_name == 'C':
                c_encountered = True
            if not c_encountered:
                note_name_components.append((ordered_note_name, -1))
            else:
                note_name_components.append((ordered_note_name, 0))
        return note_name_components

    def generate_note_names(self):
        octaves = list()
        for i, single_octave_chromatic_scale in enumerate(self.chromatic_scale):
            scale = list()
            for note, note_name_components in zip(single_octave_chromatic_scale,
                                                  self.generate_note_name_components()):
                if note is None:
                    scale.append(None)
                    continue
                letter_component, octave_number_component = note_name_components
                note_name = letter_component + str(octave_number_component + i)
                scale.append(note_name)
            octaves.append(scale)
        return octaves


class WesternEqualTemperedChromaticContext(EqualTemperedTrueOctavedChromaticContext, WesternChromaticContext):

    def __init__(self, minimum_hz=16.3515, maximum_hz=7902.1329, anchor_hz=440.0):
        super().__init__(minimum_hz=minimum_hz, maximum_hz=maximum_hz, anchor_hz=anchor_hz,
                         single_octave_note_count=12)

    def __str__(self):
        return f'Classic western equal tempered chromatic context, with A4 on {self.anchor_hz} hz'


class WesternJustTemperedChromaticContext(UnequalTemperedTrueOctavedChromaticContext, WesternChromaticContext):
    NOTE_RATIOS = [25/24, 9/8, 6/5, 5/4, 4/3, 45/32, 3/2, 8/5, 5/3, 9/5, 15/8]

    def __init__(self, minimum_hz=16.4999, maximum_hz=7920.0001, anchor_hz=440.0, anchor_note_name='A'):
        super().__init__(minimum_hz=minimum_hz, maximum_hz=maximum_hz, anchor_hz=anchor_hz,
                         single_octave_note_count=len(WesternJustTemperedChromaticContext.NOTE_RATIOS) + 1,
                         note_ratios=WesternJustTemperedChromaticContext.NOTE_RATIOS)
        self.anchor_note_name = anchor_note_name

    def __str__(self):
        return f'Classic western just tempered chromatic context in {self.anchor_note_name}, with ' + \
               f'{self.anchor_note_name}4 on {self.anchor_hz} hz'


WesternEqualTempered432ChromaticContext = \
    WesternEqualTemperedChromaticContext(minimum_hz=16.0542, maximum_hz=7758.4577, anchor_hz=432.0)
WesternEqualTempered434ChromaticContext = \
    WesternEqualTemperedChromaticContext(minimum_hz=16.1286, maximum_hz=7794.3765, anchor_hz=434.0)
WesternEqualTempered436ChromaticContext = \
    WesternEqualTemperedChromaticContext(minimum_hz=16.2029, maximum_hz=7830.2953, anchor_hz=436.0)
WesternEqualTempered438ChromaticContext = \
    WesternEqualTemperedChromaticContext(minimum_hz=16.2772, maximum_hz=7866.2141, anchor_hz=438.0)
WesternEqualTempered440ChromaticContext = WesternEqualTemperedChromaticContext()
WesternEqualTempered442ChromaticContext = \
    WesternEqualTemperedChromaticContext(minimum_hz=16.4259, maximum_hz=7938.0517, anchor_hz=442.0)
WesternEqualTempered444ChromaticContext = \
    WesternEqualTemperedChromaticContext(minimum_hz=16.5002, maximum_hz=7973.9704, anchor_hz=444.0)
WesternEqualTempered446ChromaticContext = \
    WesternEqualTemperedChromaticContext(minimum_hz=16.5745, maximum_hz=8009.8892, anchor_hz=446.0)


WesternJustTemperedA440ChromaticContext = WesternJustTemperedChromaticContext()
