from random import choices, gauss, randint
from string import ascii_uppercase
from algorithm.general_tools.frequency_ranges import NORMAL_MUSIC_FREQUENCY_RANGE
from algorithm.general_tools.option_probabilities import OCTAVE_RANGES, SINGLE_OCTAVE_NOTE_COUNTS


class ChromaticContext:
    NOTE_NAMES = list(ascii_uppercase)

    def __init__(self, minimum_hz=NORMAL_MUSIC_FREQUENCY_RANGE.lower_hz,
                 maximum_hz=NORMAL_MUSIC_FREQUENCY_RANGE.upper_hz - 1, anchor_hz=None):
        self.minimum_hz = minimum_hz
        self.maximum_hz = maximum_hz
        self.anchor_hz = anchor_hz or float(randint(self.minimum_hz, self.maximum_hz))
        self.chromatic_scale = list()
        self.note_names = list()

    @property
    def anchor_hz(self):
        return self._anchor_hz

    @anchor_hz.setter
    def anchor_hz(self, anchor_hz):
        if not self.minimum_hz <= anchor_hz <= self.maximum_hz:
            return Exception('Anchor hz must be between minimum hz and maximum hz inclusive')
        self._anchor_hz = anchor_hz

    def generate_note_names(self):
        octaves = list()
        for i, single_octave_chromatic_scale in enumerate(self.chromatic_scale):
            scale = list()
            for j, note in enumerate(single_octave_chromatic_scale):
                if note is None:
                    scale.append(None)
                    continue
                quotient, remainder = divmod(j, len(ChromaticContext.NOTE_NAMES))
                note_name = ascii_uppercase[remainder]
                while quotient > 0:
                    quotient, remainder = divmod(quotient - 1, len(ChromaticContext.NOTE_NAMES))
                    note_name = ascii_uppercase[remainder] + note_name
                note_name = note_name + str(i)
                scale.append(note_name)
            octaves.append(scale)
        return octaves

    @property
    def named_chromatic_scale(self):
        if not hasattr(self, '_named_chromatic_scale'):
            self._named_chromatic_scale = \
                [[(name, note) for note, name in zip(chromatic_scale, note_names)]
                 for chromatic_scale, note_names in zip(self.chromatic_scale, self.note_names)]
        return self._named_chromatic_scale

    @property
    def flat_chromatic_scale(self):
        if not hasattr(self, '_flat_chromatic_scale'):
            self._flat_chromatic_scale = [note for single_octave_scale in self.chromatic_scale
                                          for note in single_octave_scale if note is not None]
        return self._flat_chromatic_scale

    @property
    def flat_note_names(self):
        if not hasattr(self, '_flat_note_names'):
            self._flat_note_names = [note for single_octave_scale in self.note_names
                                     for note in single_octave_scale if note is not None]
        return self._flat_note_names

    @property
    def flat_named_chromatic_scale(self):
        if not hasattr(self, '_flat_named_chromatic_scale'):
            self._flat_named_chromatic_scale = [(name, note) for single_octave_scale in self.named_chromatic_scale
                                                for name, note in single_octave_scale
                                                if note is not None and name is not None]
        return self._flat_named_chromatic_scale


class TrueOctavedChromaticContext(ChromaticContext):

    def __init__(self, single_octave_note_count=None, octave_range=None, **kwargs):
        super().__init__(**kwargs)
        self.single_octave_note_count = single_octave_note_count or \
            choices(SINGLE_OCTAVE_NOTE_COUNTS.options, weights=SINGLE_OCTAVE_NOTE_COUNTS.probabilities)[0]
        self.octave_range = octave_range or choices(OCTAVE_RANGES.options, weights=OCTAVE_RANGES.probabilities)[0]

    def generate_single_octave_chromatic_scale_from_anchor_note(self, anchor_note): return []

    def generate_chromatic_scale(self):
        octaves = list()
        current_note = self.anchor_hz
        while current_note <= self.maximum_hz:
            octaves.append(self.generate_single_octave_chromatic_scale_from_anchor_note(current_note))
            current_note *= pow(2, self.octave_range)
        current_note = self.anchor_hz
        while True:
            current_note /= pow(2, self.octave_range)
            scale = self.generate_single_octave_chromatic_scale_from_anchor_note(current_note)
            if scale.count(None) == self.single_octave_note_count:
                break
            octaves.insert(0, scale)
        return octaves


class EqualTemperedTrueOctavedChromaticContext(TrueOctavedChromaticContext):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.chromatic_scale = self.generate_chromatic_scale()
        self.note_names = self.generate_note_names()

    def generate_next_note(self, note):
        return note * pow(pow(2, self.octave_range), 1 / self.single_octave_note_count)

    def generate_previous_note(self, note):
        return note / pow(pow(2, self.octave_range), 1 / self.single_octave_note_count)

    def generate_single_octave_chromatic_scale_from_anchor_note(self, anchor_note):
        scale = list()
        current_note = anchor_note
        for _ in range(self.single_octave_note_count):
            if self.minimum_hz <= current_note <= self.maximum_hz:
                scale.append(current_note)
            else:
                scale.append(None)
            current_note = self.generate_next_note(current_note)
        return scale


class UnequalTemperedTrueOctavedChromaticContext(TrueOctavedChromaticContext):
    NOTE_RATIO_STANDARD_DEVIATION_PERCENTAGE = 0.25

    def __init__(self, note_ratios=None, **kwargs):
        super().__init__(**kwargs)
        self.note_ratios = note_ratios or self.generate_note_ratios()
        self.chromatic_scale = self.generate_chromatic_scale()
        self.note_names = self.generate_note_names()

    @property
    def standard_note_ratio(self):
        return pow(pow(2, self.octave_range), 1 / self.single_octave_note_count)

    def generate_next_ratio(self, index):
        max_iterations = 5
        following_ratio_diff = pow(self.standard_note_ratio, index + 2) - pow(self.standard_note_ratio, (index + 1))
        for _ in range(max_iterations):
            possible_ratio = pow(self.standard_note_ratio, (index + 1)) + \
                gauss(0, following_ratio_diff *
                      UnequalTemperedTrueOctavedChromaticContext.NOTE_RATIO_STANDARD_DEVIATION_PERCENTAGE)
            if possible_ratio <= pow(self.standard_note_ratio, index) or \
                    possible_ratio >= pow(self.standard_note_ratio, index + 2):
                continue
            return possible_ratio
        return pow(self.standard_note_ratio, (index + 1))

    def generate_note_ratios(self):
        note_ratios = [self.generate_next_ratio(i) for i in range(self.single_octave_note_count - 1)]
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
