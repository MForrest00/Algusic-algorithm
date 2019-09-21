import random
import unittest
from algorithm.structure import SectionedSongSkeleton, SongSkeleton


class TestSongSkeleton(unittest.TestCase):

    def test_generate_song_skeleton(self):
        for s in range(100):
            random.seed(s)
            song_skeleton = SongSkeleton()
            self.assertIsInstance(song_skeleton.bars, list)
            song_skeleton = SongSkeleton(bar_count_modulus=random.randint(2, 10))
            self.assertIsInstance(song_skeleton.bars, list)
            self.assertEqual(len(song_skeleton.bars) % song_skeleton.bar_count_modulus, 0)


class TestSectionedSongSkeleton(unittest.TestCase):

    def test_generate_sectioned_song_skeleton(self):
        for s in range(100):
            random.seed(s)
            sectioned_song_skeleton = SectionedSongSkeleton(minimum_section_length=None)
            self.assertGreaterEqual(sectioned_song_skeleton.section_count, sectioned_song_skeleton.MINIMUM_SECTIONS)
            self.assertLessEqual(sectioned_song_skeleton.section_count, sectioned_song_skeleton.MAXIMUM_SECTIONS)
            self.assertEqual(len(sectioned_song_skeleton.bars), sum(sectioned_song_skeleton.sectioned_bar_lengths))
        for s in range(100, 200):
            random.seed(s)
            sectioned_song_skeleton = SectionedSongSkeleton(minimum_section_length=None,
                                                            bar_count_modulus=random.randint(2, 10))
            self.assertGreaterEqual(sectioned_song_skeleton.section_count, sectioned_song_skeleton.MINIMUM_SECTIONS)
            self.assertLessEqual(sectioned_song_skeleton.section_count, sectioned_song_skeleton.MAXIMUM_SECTIONS)
            self.assertEqual(len(sectioned_song_skeleton.bars), sum(sectioned_song_skeleton.sectioned_bar_lengths))
            for sectioned_bar_length in sectioned_song_skeleton.sectioned_bar_lengths:
                self.assertEqual(sectioned_bar_length % sectioned_song_skeleton.bar_count_modulus, 0)
