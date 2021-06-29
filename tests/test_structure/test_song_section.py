import unittest
from algorithm.structure.song_section import SongSection


class TestSongSection(unittest.TestCase):
    def test_generate_song_section(self):
        for s in range(100):
            song_section = SongSection()
            assert 0 <= song_section.pitched_density_adjustment_factor <= 1
            assert 0 <= song_section.rhythmic_density_adjustment_factor <= 1
            assert 0 <= song_section.line_repetition_factor <= 1
            assert 0 <= song_section.section_repetition_factor <= 1
            assert 0 <= song_section.volume_adjustment_factor <= 1
            assert 0 <= song_section.layering_factor <= 1
