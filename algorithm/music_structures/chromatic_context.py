from random import choices, gauss, randint
from string import ascii_uppercase
from algorithm.general_tools.frequency_ranges import NORMAL_MUSIC_RANGE
from algorithm.general_tools.option_probabilities import OCTAVE_RANGES, SINGLE_OCTAVE_NOTE_COUNTS


class ChromaticContext:

    def __init__(self, minimum_hz=NORMAL_MUSIC_RANGE.lower_hz, maximum_hz=NORMAL_MUSIC_RANGE.upper_hz - 1,
                 anchor_hz=None):
        self.minimum_hz = minimum_hz
        self.maximum_hz = maximum_hz
        self.anchor_hz = anchor_hz or randint(self.minimum_hz, self.maximum_hz)
        self.chromatic_scale = [[]]
        self.named_chromatic_scale = [[]]

    def generate_named_chromatic_scale(self):
        octaves = []
        for i, single_octave_chromatic_scale in enumerate(self.chromatic_scale):
            scale = []
            for j, note in enumerate(single_octave_chromatic_scale):
                if note is None:
                    continue
                quotient, remainder = divmod(j, len(ascii_uppercase))
                note_name = ascii_uppercase[remainder]
                while quotient > 0:
                    quotient, remainder = divmod(quotient - 1, len(ascii_uppercase))
                    note_name = ascii_uppercase[remainder] + note_name
                note_name = note_name + str(i)
                scale.append({note_name: note})
            octaves.append(scale)
        return octaves

    @property
    def flat_chromatic_scale(self):
        return [note for single_octave_scale in self.chromatic_scale
                for note in single_octave_scale if note is not None]

    @property
    def flat_named_chromatic_scale(self):
        return [note for single_octave_scale in self.named_chromatic_scale
                for note in single_octave_scale if note is not None]


class TrueOctavedChromaticContext(ChromaticContext):

    def __init__(self, single_octave_note_count=None, octave_range=None, **kwargs):
        super().__init__(**kwargs)
        self.single_octave_note_count = single_octave_note_count or \
            choices(SINGLE_OCTAVE_NOTE_COUNTS.options, weights=SINGLE_OCTAVE_NOTE_COUNTS.probabilities)
        self.octave_range = octave_range or choices(OCTAVE_RANGES.options, weights=OCTAVE_RANGES.probabilities)

    def generate_single_octave_chromatic_scale_from_anchor_note(self, anchor_note): return []

    def generate_chromatic_scale(self):
        octaves = []
        current_note = self.anchor_hz
        while current_note <= self.maximum_hz:
            octaves.append(self.generate_single_octave_chromatic_scale_from_anchor_note(current_note))
            current_note *= (2 * self.octave_range)
        current_note = self.anchor_hz
        while True:
            current_note /= (2 * self.octave_range)
            scale = self.generate_single_octave_chromatic_scale_from_anchor_note(current_note)
            if scale.count(None) == self.single_octave_note_count:
                break
            octaves.insert(0, scale)
        return octaves


class EqualTemperedTrueOctavedChromaticContext(TrueOctavedChromaticContext):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.chromatic_scale = self.generate_chromatic_scale()
        self.named_chromatic_scale = self.generate_named_chromatic_scale()

    def generate_next_note(self, note):
        return note * pow(pow(2, self.octave_range), 1 / self.single_octave_note_count)

    def generate_previous_note(self, note):
        return note / pow(pow(2, self.octave_range), 1 / self.single_octave_note_count)

    def generate_single_octave_chromatic_scale_from_anchor_note(self, anchor_note):
        scale = []
        current_note = anchor_note
        for _ in range(self.single_octave_note_count):
            if self.minimum_hz <= current_note <= self.maximum_hz:
                scale.append(current_note)
            else:
                scale.append(None)
            current_note = self.generate_next_note(current_note)
        return scale


class UnequalTemperedTrueOctavedChromaticContext(TrueOctavedChromaticContext):
    NOTE_RATIO_STANDARD_DEVIATION_PERCENTAGE = 0.15

    def __init__(self, note_ratios=None, **kwargs):
        super().__init__(**kwargs)
        self.note_ratios = note_ratios or self.generate_note_ratios()
        self.chromatic_scale = self.generate_chromatic_scale()
        self.named_chromatic_scale = self.generate_named_chromatic_scale()

    @property
    def note_ratios(self):
        return self._note_ratios

    @note_ratios.setter
    def note_ratios(self, note_ratios):
        if len(note_ratios) != self.single_octave_note_count - 1:
            raise Exception('Number of elements in note ratios must be one less than the note count')
        self._note_ratios = note_ratios

    @property
    def standard_note_ratio(self):
        return pow(pow(2, self.octave_range), 1 / self.single_octave_note_count)

    def generate_next_ratio(self, current_ratio):
        iterations = 0
        possible_ratio = \
            current_ratio * gauss(self.standard_note_ratio,
                                  self.standard_note_ratio * UnequalTemperedTrueOctavedChromaticContext.NOTE_RATIO_STANDARD_DEVIATION_PERCENTAGE)
        while possible_ratio <= current_ratio or \
                possible_ratio >= (current_ratio * (self.standard_note_ratio * 2)) or \
                possible_ratio >= pow(2, self.octave_range):
            if iterations >= 5:
                break
            iterations += 1
            possible_ratio = \
                current_ratio * gauss(self.standard_note_ratio,
                                    self.standard_note_ratio * UnequalTemperedTrueOctavedChromaticContext.NOTE_RATIO_STANDARD_DEVIATION_PERCENTAGE)
        return possible_ratio

    def generate_note_ratios(self):
        note_ratios = [1.0]
        current_ratio = 1.0
        for _ in range(self.single_octave_note_count - 1):
            possible_ratio = self.generate_next_ratio(current_ratio)
            current_ratio *= possible_ratio
            note_ratios.append(current_ratio)
        return note_ratios

    def generate_single_octave_chromatic_scale_from_anchor_note(self, anchor_note):
        if anchor_note >= self.minimum_hz:
            scale = [anchor_note]
        else:
            scale = [None]
        for note_ratio in self.note_ratios:
            next_note = anchor_note * note_ratio
            if self.minimum_hz <= next_note <= self.maximum_hz:
                scale.append(next_note)
            else:
                scale.append(None)
        return scale
