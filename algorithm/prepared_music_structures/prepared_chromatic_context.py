from algorithm.music_structures.chromatic_context import ChromaticContext, EqualTemperedTrueOctavedChromaticContext, \
    UnequalTemperedTrueOctavedChromaticContext


class WesternChromaticContext(ChromaticContext):
    NOTE_NAME_COMPONENTS = [('A', -1), ('A♯/B♭', -1), ('B', -1), ('C', 0), ('C♯/D♭', 0), ('D', 0), ('D♯/E♭', 0),
                            ('E', 0), ('F', 0), ('F♯/G♭', 0), ('G', 0), ('G♯/A♭', 0)]
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    @property
    def named_chromatic_scale(self):
        octaves = []
        for i, single_octave_chromatic_scale in enumerate(self.chromatic_scale):
            scale = []
            for note, note_name_components in zip(single_octave_chromatic_scale,
                                                  WesternEqualTemperedChromaticContext.NOTE_NAME_COMPONENTS):
                if note is None:
                    continue
                letter_component, octave_number_component = note_name_components
                note_name = letter_component + str(octave_number_component + i)
                scale.append({note_name: note})
            octaves.append(scale)
        return octaves


class WesternEqualTemperedChromaticContext(EqualTemperedTrueOctavedChromaticContext, WesternChromaticContext):

    def __init__(self, minimum_hz=16.3515, maximum_hz=7902.1329, anchor_hz=440.0):
        super().__init__(minimum_hz=minimum_hz, maximum_hz=maximum_hz, anchor_hz=anchor_hz, note_count=12,
                         octave_range=1)


class WesternJustTemperedChromaticContext(UnequalTemperedTrueOctavedChromaticContext, WesternChromaticContext):
    NOTE_RATIOS = [25/24, 9/8, 6/5, 5/4, 4/3, 45/32, 3/2, 8/5, 5/3, 9/5, 15/8]

    def __init__(self, minimum_hz=16.4999, maximum_hz=7920.0001, anchor_hz=440.0):
        super().__init__(minimum_hz=minimum_hz, maximum_hz=maximum_hz, anchor_hz=anchor_hz, note_count=12,
                         octave_range=1, note_ratios=WesternJustTemperedChromaticContext.NOTE_RATIOS)


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


WesternJustTempered440ChromaticContext = WesternJustTemperedChromaticContext()
