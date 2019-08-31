import random
import unittest
from algorithm.pitch import OctavedAbstractScale
from algorithm.tools import SINGLE_OCTAVE_NOTE_COUNTS


class TestOctavedAbstractScale(unittest.TestCase):

    def test_generate_octaved_abstract_scale(self):
        for single_octave_note_count in SINGLE_OCTAVE_NOTE_COUNTS:
            for s in range(100):
                random.seed(s)
                abstract_scale = OctavedAbstractScale(single_octave_note_count.option)
                self.assertLess(max(abstract_scale.scale_degrees), abstract_scale.chromatic_single_octave_note_count)
