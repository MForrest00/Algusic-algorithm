from random import choices, gauss
from algorithm.general_tools.option_probabilities import BAR_BEATS
from algorithm.general_tools.tempo_ranges import NORMAL_MUSIC_TEMPO_RANGE


class SongSkeleton:
    TEMPO_STANDARD_DEVIATION_PERCENTAGE = 0.5
    SONG_LENGTH_MEAN = 4 * 60
    SONG_LENGTH_STANDARD_DEVIATION = 1 * 60
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
            raise TypeError('Bar count modulus must be an integer great than 1')
        self._bar_count_modulus = bar_count_modulus

    def generate_tempo(self):
        average_tempo = int(round((self.minimum_tempo + self.maximum_tempo) / 2, 0))
        tempo_range = self.maximum_tempo - self.minimum_tempo
        max_iterations = 5
        for _ in range(max_iterations):
            possible_tempo = gauss(average_tempo, tempo_range / 2 * SongSkeleton.TEMPO_STANDARD_DEVIATION_PERCENTAGE)
            if not self.minimum_tempo <= possible_tempo <= self.maximum_tempo:
                continue
            return int(round(possible_tempo, 0))
        return average_tempo

    def generate_song_length(self):
        max_iterations = 5
        for _ in range(max_iterations):
            possible_length = gauss(SongSkeleton.SONG_LENGTH_MEAN, SongSkeleton.SONG_LENGTH_STANDARD_DEVIATION)
            if possible_length <= SongSkeleton.MINIMUM_SONG_LENGTH:
                continue
            return possible_length
        return SongSkeleton.SONG_LENGTH_MEAN

    def calculate_elapsed_seconds(self, elapsed_beats):
        return elapsed_beats / (self.tempo / 60)

    def generate_bars(self):
        bars = []
        while self.calculate_elapsed_seconds(sum(bars)) < self.song_length:
            bars.append(self.bar_beats)
        if self.bar_count_modulus is not None:
            while len(bars) % self.bar_count_modulus != 0:
                bars.append(self.bar_beats)
        return bars
