from math import ceil, floor
from random import choices, gauss, randint
from string import ascii_uppercase
from typing import Any, List, Optional, Tuple, Union
from algorithm.data.frequency_ranges import NORMAL_MUSIC_FREQUENCY_RANGE
from algorithm.tools.option_probabilities import OCTAVE_RANGES, SINGLE_OCTAVE_NOTE_COUNTS


class ChromaticContext:
    """Base class for all contexts creating chromatic notes in a frequency space

    Arguments:
        minimum_hz (int or float): minimum frequency for which notes will be generated
        maximum_hz (int or float): maximum frequency for which notes will be generated
        anchor_hz (int or float): frequency with which all other chromatic notes will be genereated
    """
    NOTE_NAMES = list(ascii_uppercase)

    def __init__(
        self,
        minimum_hz: Union[int, float] = NORMAL_MUSIC_FREQUENCY_RANGE.lower_hz,
        maximum_hz: Union[int, float] = NORMAL_MUSIC_FREQUENCY_RANGE.upper_hz - 1,
        anchor_hz: Optional[Union[int, float]] = None,
    ):
        self.minimum_hz = minimum_hz
        self.maximum_hz = maximum_hz
        self.anchor_hz = anchor_hz or self.create_anchor_hz()
        self.chromatic_scale: List[List[Optional[float]]] = list()
        self.note_names: List[List[Optional[str]]] = list()

    @property
    def minimum_hz(self) -> float:
        return self._minimum_hz

    @minimum_hz.setter
    def minimum_hz(self, minimum_hz):
        if not isinstance(minimum_hz, (int, float)):
            raise TypeError('Minimum hertz must be an integer or float')
        if minimum_hz <= 0:
            raise ValueError('Minimum hertz must be greater than 0')
        self._minimum_hz = float(minimum_hz)

    @property
    def maximum_hz(self) -> float:
        return self._maximum_hz

    @maximum_hz.setter
    def maximum_hz(self, maximum_hz):
        if not isinstance(maximum_hz, (int, float)):
            raise TypeError('Maximum hertz must be an integer or float')
        if maximum_hz < self.minimum_hz:
            raise ValueError('Maximum hertz must be greater than or equal to minimum hertz')
        self._maximum_hz = float(maximum_hz)

    @property
    def anchor_hz(self) -> float:
        return self._anchor_hz

    @anchor_hz.setter
    def anchor_hz(self, anchor_hz):
        if not isinstance(anchor_hz, (int, float)):
            raise TypeError('Anchor hertz must be an integer or float')
        if not self.minimum_hz <= anchor_hz <= self.maximum_hz:
            raise ValueError('Anchor hertz must be between minimum hertz and maximum hertz inclusive')
        self._anchor_hz = float(anchor_hz)

    def create_anchor_hz(self) -> float:
        ceil_minimum_hz = ceil(self.minimum_hz)
        floor_maximum_hz = floor(self.maximum_hz)
        if ceil_minimum_hz < floor_maximum_hz:
            return float(randint(ceil_minimum_hz, floor_maximum_hz))
        return self.minimum_hz

    def generate_note_names(self) -> List[List[Optional[str]]]:
        """Generate note names for frequency values in chromatic scale

        Returns:
            list: list of lists containing string note names, with None representing the absence of a note
        """
        octaves: List[List[Optional[str]]] = list()
        for i, single_octave_chromatic_scale in enumerate(self.chromatic_scale):
            scale: List[Optional[str]] = list()
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
    def named_chromatic_scale(self) -> List[List[Tuple[Optional[str], Optional[float]]]]:
        """List of all named notes in chromatic scale, with None notes removed"""
        if not hasattr(self, '_named_chromatic_scale'):
            self._named_chromatic_scale = [
                [(name, note) for note, name in zip(chromatic_scale, note_names)]
                for chromatic_scale, note_names in zip(self.chromatic_scale, self.note_names)
            ]
        return self._named_chromatic_scale

    @property
    def flat_chromatic_scale(self) -> List[float]:
        """List of all frequencies in chromatic scale, with None notes removed"""
        if not hasattr(self, '_flat_chromatic_scale'):
            self._flat_chromatic_scale = [
                note for single_octave_scale in self.chromatic_scale
                for note in single_octave_scale if note is not None
            ]
        return self._flat_chromatic_scale

    @property
    def flat_note_names(self) -> List[str]:
        """List of all note names in chromatic scale, with None notes removed"""
        if not hasattr(self, '_flat_note_names'):
            self._flat_note_names = [
                note for single_octave_scale in self.note_names
                for note in single_octave_scale if note is not None
            ]
        return self._flat_note_names

    @property
    def flat_named_chromatic_scale(self) -> List[Tuple[str, float]]:
        """List of all named notes in chromatic scale, with None notes removed"""
        if not hasattr(self, '_flat_named_chromatic_scale'):
            self._flat_named_chromatic_scale = [
                (name, note) for single_octave_scale in self.named_chromatic_scale
                for name, note in single_octave_scale if note is not None and name is not None
            ]
        return self._flat_named_chromatic_scale


class TrueOctavedChromaticContext(ChromaticContext):
    """Base class for all chromatic contexts which are divided into true octaves (relative notes are multiples of each
        other)

    Arguments:
        single_octave_note_count (int): number of notes in a single octave
        octave_range (int): number of true octaves an octave spans
    """

    def __init__(
        self,
        single_octave_note_count: Optional[int] = None,
        octave_range: Optional[int] = None,
        **kwargs: Any,
    ):
        super().__init__(**kwargs)
        self.single_octave_note_count = single_octave_note_count or \
            choices(SINGLE_OCTAVE_NOTE_COUNTS.options, weights=SINGLE_OCTAVE_NOTE_COUNTS.probabilities)[0]
        self.octave_range = octave_range or choices(OCTAVE_RANGES.options, weights=OCTAVE_RANGES.probabilities)[0]

    @property
    def single_octave_note_count(self) -> int:
        return self._single_octave_note_count

    @single_octave_note_count.setter
    def single_octave_note_count(self, single_octave_note_count):
        if not isinstance(single_octave_note_count, int):
            raise TypeError('Single octave note count must be an integer')
        if single_octave_note_count < 1:
            raise ValueError('Single octave note count must be greater than or equal to 1')
        self._single_octave_note_count = single_octave_note_count

    @property
    def octave_range(self) -> int:
        return self._octave_range

    @octave_range.setter
    def octave_range(self, octave_range):
        if not isinstance(octave_range, int):
            raise TypeError('Octave range must be an integer')
        if octave_range < 1:
            raise ValueError('Octave range must be greater than or equal to 1')
        self._octave_range = octave_range

    def generate_single_octave_chromatic_scale_from_anchor_note(self, anchor_note: float) -> List[Optional[float]]:
        return []

    def generate_chromatic_scale(self) -> List[List[Optional[float]]]:
        """Generate the chromatic scale

        Returns:
            list: list of lists containing frequencies, with None representing the absence of a note
        """
        octaves: List[List[Optional[float]]] = list()
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
    """True octaved chromatic context, where notes are evenly divided within the octave"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.chromatic_scale = self.generate_chromatic_scale()
        self.note_names = self.generate_note_names()

    def generate_next_note(self, note: float) -> float:
        """Generate next note within the chromatic context

        Arguments:
            note (float): note against which to generate the next note

        Returns:
            float: next note
        """
        return note * pow(pow(2, self.octave_range), 1 / self.single_octave_note_count)

    def generate_previous_note(self, note: float) -> float:
        """Generate previous note within the chromatic context

        Arguments:
            note (float): note against which to generate the previous note

        Returns:
            float: previous note
        """
        return note / pow(pow(2, self.octave_range), 1 / self.single_octave_note_count)

    def generate_single_octave_chromatic_scale_from_anchor_note(self, anchor_note: float) -> List[Optional[float]]:
        """Generate a single octave chromatic scale from the first note in the scale

        Arguments:
            anchor_note (int or float): frequency of the first note in the scale

        Returns:
            list: floats representing each note in the scale, with None representing the absence of a Note
        """
        scale: List[Optional[float]] = list()
        current_note = anchor_note
        for _ in range(self.single_octave_note_count):
            if self.minimum_hz <= current_note <= self.maximum_hz:
                scale.append(current_note)
            else:
                scale.append(None)
            current_note = self.generate_next_note(current_note)
        return scale


class UnequalTemperedTrueOctavedChromaticContext(TrueOctavedChromaticContext):
    """True octaved chromatic context, where notes are set as ratios to the anchor note

    Arguments:
        note_ratios (list): floats representing the ratios between notes and the anchor in the chromatic scale
    """
    NOTE_RATIO_STANDARD_DEVIATION_PERCENTAGE = 0.25

    def __init__(
        self,
        note_ratios=None,
        **kwargs: Any,
    ):
        super().__init__(**kwargs)
        self.note_ratios = note_ratios or self.generate_note_ratios()
        self.chromatic_scale = self.generate_chromatic_scale()
        self.note_names = self.generate_note_names()

    @property
    def note_ratios(self):
        return self._note_ratios

    @note_ratios.setter
    def note_ratios(self, note_ratios):
        if not isinstance(note_ratios, list) or any(not isinstance(r, (int, float)) for r in note_ratios):
            raise TypeError('Note ratios must be a list of integers or floats')
        if len(note_ratios) != self.single_octave_note_count - 1:
            raise ValueError('Length of note ratios must be equal to the single octave note count minus 1')
        if len(note_ratios) > 0 and any(not 1 < r < pow(2, self.octave_range) for r in note_ratios):
            raise ValueError(
                'Note ratios must be between 1 and 2 raised to the power of the octave range, non-inclusive'
            )
        self._note_ratios = sorted(note_ratios)

    @property
    def standard_note_ratio(self):
        """Standard ratio between notes in an equal tempered scale"""
        return pow(pow(2, self.octave_range), 1 / self.single_octave_note_count)

    def generate_ratio_by_index(self, index):
        """Randomly generate note ratio by index using standard note ratio and standard deviation percentage

        Arguments:
            index (int): note index in the chromatic scale to generate the ratio for

        Returns:
            float: note ratio
        """
        max_iterations = 5
        following_ratio_diff = pow(self.standard_note_ratio, index + 1) - pow(self.standard_note_ratio, (index))
        for _ in range(max_iterations):
            possible_ratio = pow(self.standard_note_ratio, (index)) + \
                gauss(0, following_ratio_diff *
                      UnequalTemperedTrueOctavedChromaticContext.NOTE_RATIO_STANDARD_DEVIATION_PERCENTAGE)
            if pow(self.standard_note_ratio, index - 1) < possible_ratio < pow(self.standard_note_ratio, index + 1):
                return possible_ratio
        return pow(self.standard_note_ratio, (index))

    def generate_note_ratios(self):
        """Randomly generate intern-note ratios for chromatic scale"""
        note_ratios = [self.generate_ratio_by_index(i) for i in range(1, self.single_octave_note_count)]
        return note_ratios

    def generate_single_octave_chromatic_scale_from_anchor_note(self, anchor_note):
        """Generate a single octave chromatic scale from the first note in the scale

        Arguments:
            anchor_note (int or float): frequency of the first note in the scale

        Returns:
            list: floats representing each note in the scale, with None representing the absence of a Note
        """
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
