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
            sectioned_song_skeleton = SectionedSongSkeleton()
            self.assertGreaterEqual(sectioned_song_skeleton.section_count, sectioned_song_skeleton.MINIMUM_SECTIONS)
            self.assertLessEqual(sectioned_song_skeleton.section_count, sectioned_song_skeleton.MAXIMUM_SECTIONS)
