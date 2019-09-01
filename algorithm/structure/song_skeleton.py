from math import ceil, floor
from random import choices, gauss, randint, shuffle
from algorithm.tools import BAR_BEATS, NORMAL_MUSIC_TEMPO_RANGE


class SongSkeleton:
    TEMPO_STANDARD_DEVIATION_PERCENTAGE = 0.5
    SONG_LENGTH_MEAN = 4 * 60
    SONG_LENGTH_STANDARD_DEVIATION = 60
    MINIMUM_SONG_LENGTH = 20

    def __init__(self, minimum_tempo=NORMAL_MUSIC_TEMPO_RANGE.lower_bpm,
                 maximum_tempo=NORMAL_MUSIC_TEMPO_RANGE.upper_bpm - 1, tempo=None, bar_beats=None,
                 song_length=None, bar_count_modulus=None):
        self.minimum_tempo = minimum_tempo
        self.maximum_tempo = maximum_tempo
        self.tempo = tempo or self.generate_tempo()
        self.bar_beats = bar_beats or choices(BAR_BEATS.options, weights=BAR_BEATS.probabilities)[0]
        self.song_length = song_length or self.generate_song_length()
        self.bar_count_modulus = bar_count_modulus
        self.bars = self.generate_bars()

    @property
    def bar_count_modulus(self):
        return self._bar_count_modulus

    @bar_count_modulus.setter
    def bar_count_modulus(self, bar_count_modulus):
        if bar_count_modulus is not None and (not isinstance(bar_count_modulus, int) or bar_count_modulus <= 1):
            raise TypeError('Bar count modulus must be None or an integer great than 1')
        self._bar_count_modulus = bar_count_modulus

    def generate_tempo(self):
        average_tempo = int(round((self.minimum_tempo + self.maximum_tempo) / 2, 0))
        tempo_range = self.maximum_tempo - self.minimum_tempo
        max_iterations = 5
        for _ in range(max_iterations):
            possible_tempo = gauss(average_tempo, tempo_range / 2 * SongSkeleton.TEMPO_STANDARD_DEVIATION_PERCENTAGE)
            if self.minimum_tempo <= possible_tempo <= self.maximum_tempo:
                int(round(possible_tempo, 0))
        return average_tempo

    def generate_song_length(self):
        max_iterations = 5
        for _ in range(max_iterations):
            possible_length = gauss(SongSkeleton.SONG_LENGTH_MEAN, SongSkeleton.SONG_LENGTH_STANDARD_DEVIATION)
            if possible_length > SongSkeleton.MINIMUM_SONG_LENGTH:
                return possible_length
        return SongSkeleton.SONG_LENGTH_MEAN

    def beats_to_seconds(self, beats):
        return beats / (self.tempo / 60)

    def bars_to_seconds(self, bars):
        return self.beats_to_seconds(bars * self.bar_beats)

    def seconds_to_beats(self, seconds):
        return seconds * (self.tempo / 60)

    def seconds_to_bars(self, seconds):
        return self.seconds_to_beats(seconds) / self.bar_beats

    def generate_bars(self):
        bars = list()
        while self.beats_to_seconds(sum(bars)) < self.song_length:
            bars.append(self.bar_beats)
        if self.bar_count_modulus is not None:
            while len(bars) % self.bar_count_modulus != 0:
                bars.append(self.bar_beats)
        return bars


class SectionedSongSkeleton(SongSkeleton):
    MINIMUM_SECTIONS = 1
    MAXIMUM_SECTIONS = 20
    MINIMUM_SECTION_LENGTH = 10

    def __init__(self, minimum_sections=None, maximum_sections=None, maximum_section_length=None,
                 minimum_section_length=None, section_count=None, **kwargs):
        super().__init__(**kwargs)
        self.minimum_sections = minimum_sections or SectionedSongSkeleton.MINIMUM_SECTIONS
        self.maximum_sections = maximum_sections or SectionedSongSkeleton.MAXIMUM_SECTIONS
        self.maximum_section_length = maximum_section_length
        self.minimum_section_length = minimum_section_length or SectionedSongSkeleton.MINIMUM_SECTION_LENGTH
        self.section_count = section_count or self.generate_section_count()
        self.sectioned_bar_lengths = self.generate_sectioned_bar_lengths()

    @property
    def minimum_sections(self):
        return self._minimum_sections

    @minimum_sections.setter
    def minimum_sections(self, minimum_sections):
        if minimum_sections is not None and (not isinstance(minimum_sections, int) or minimum_sections <= 0):
            raise TypeError('Minimum section count must be None or an integer greater than 0')
        self._minimum_sections = minimum_sections

    @property
    def maximum_sections(self):
        return self._maximum_sections

    @maximum_sections.setter
    def maximum_sections(self, maximum_sections):
        if maximum_sections is not None:
            if not isinstance(maximum_sections, int) or maximum_sections <= 0:
                raise TypeError('Maximum section count must be None or an integer greater than 0')
            if self.minimum_sections is not None and maximum_sections < self.minimum_sections:
                raise ValueError('Maximum section count must be greater than or equal to the minimum section count')
        self._maximum_sections = maximum_sections

    @property
    def maximum_section_length(self):
        return self._maximum_section_length

    @maximum_section_length.setter
    def maximum_section_length(self, maximum_section_length):
        if maximum_section_length is not None and \
                ((not isinstance(maximum_section_length, int) and not isinstance(maximum_section_length, float))
                 or maximum_section_length <= 0):
            raise TypeError('Maximum section length must be None or an integer or float greater than 0')
        self._maximum_section_length = maximum_section_length

    @property
    def minimum_section_length(self):
        return self._minimum_section_length

    @minimum_section_length.setter
    def minimum_section_length(self, minimum_section_length):
        if minimum_section_length is not None:
            if (not isinstance(minimum_section_length, int) and not isinstance(minimum_section_length, float)) \
                    or minimum_section_length <= 0:
                raise TypeError('Minimum section length must be None or an integer or float greater than 0')
            if self.maximum_section_length is not None and minimum_section_length > self.maximum_section_length:
                raise ValueError('Minimum section length must be less than or equal to the maximum section length')
        self._minimum_section_length = minimum_section_length

    @property
    def minimum_beats(self):
        return ceil(self.seconds_to_beats(self.minimum_section_length)) if self.minimum_section_length and \
               ceil(self.seconds_to_bars(self.minimum_section_length)) * self.section_count <= len(self.bars) else None

    def maximum_beats(self):
        return floor(self.seconds_to_beats(self.maximum_section_length)) if self.maximum_section_length and \
               floor(self.seconds_to_bars(self.maximum_section_length)) * self.section_count >= len(self.bars) else None

    def generate_section_count(self):
        minimum_sections = 1
        maximum_sections = len(self.bars) // (self.bar_count_modulus or 1)
        if self.minimum_sections is not None and self.minimum_sections <= maximum_sections:
            minimum_sections = max(minimum_sections, self.minimum_sections)
        if self.maximum_sections is not None and self.maximum_sections >= minimum_sections:
            maximum_sections = min(maximum_sections, self.maximum_sections)
        if self.maximum_section_length is not None:
            required_bars = floor(self.seconds_to_bars(self.maximum_section_length))
            section_count = ceil(len(self.bars) / required_bars)
            if section_count <= maximum_sections:
                minimum_sections = max(minimum_sections, section_count)
        if self.minimum_section_length is not None:
            required_bars = ceil(self.seconds_to_bars(self.minimum_section_length))
            section_count = len(self.bars) // required_bars
            if section_count >= minimum_sections:
                maximum_sections = min(maximum_sections, section_count)
        return randint(minimum_sections, maximum_sections)

    def generate_sectioned_bar_lengths(self):
        average_bar_length = len(self.bars) / self.section_count
        sectioned_bar_lengths = []
        for i in range(self.section_count):
            if (self.section_count - i) * ceil(average_bar_length) > len(self.bars) - sum(sectioned_bar_lengths):
                sectioned_bar_lengths.append(floor(average_bar_length))
            else:
                sectioned_bar_lengths.append(ceil(average_bar_length))
        shuffle(sectioned_bar_lengths)
        return sectioned_bar_lengths
