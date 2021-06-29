import random
import unittest
from algorithm.structure.applied_sectioned_song import AppliedSectionedSong
from algorithm.structure.song_section import SongSection
from algorithm.structure.song_skeleton import SectionedSongSkeleton


class TestAppliedSectonedSong(unittest.TestCase):
    def test_generate_applied_sectioned_song(self):
        for s in range(100):
            random.seed(s)
            song_skeleton = SectionedSongSkeleton()
            applied_sectioned_song = AppliedSectionedSong(song_skeleton)
            self.assertEqual(
                len(applied_sectioned_song.song_sections),
                len(applied_sectioned_song.song_skeleton.sectioned_bar_lengths),
            )
            self.assertTrue(all(isinstance(s, SongSection) for s in applied_sectioned_song.song_sections))
