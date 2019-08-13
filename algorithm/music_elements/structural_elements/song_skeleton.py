from random import choices, gauss
from algorithm.general_tools.option_probabilities import BAR_BEAT_LENGTHS
from algorithm.general_tools.tempo_ranges import NORMAL_MUSIC_TEMPO_RANGE


class SongSkeleton:
    TEMPO_STANDARD_DEVIATION_PERCENTAGE = 0.5

    def __init__(self, minimum_tempo=NORMAL_MUSIC_TEMPO_RANGE.lower_bpm,
                 maximum_tempo=NORMAL_MUSIC_TEMPO_RANGE.upper_bpm - 1, tempo=None, bar_beats_length=None):
        self.minimum_tempo = minimum_tempo
        self.maximum_tempo = maximum_tempo
        self.tempo = tempo or self.generate_tempo()
        self.bar_beats_length = bar_beats_length or \
            choices(BAR_BEAT_LENGTHS.options, weights=BAR_BEAT_LENGTHS.probabilities)

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

    def calculate_elapsed_seconds(self, elapsed_beats):
        return elapsed_beats / (self.starting_tempo / 60)
