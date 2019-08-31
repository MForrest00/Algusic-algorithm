import unittest
from algorithm.pitch import OctavedAbstractChord


class TestOctavedAbstractChord(unittest.TestCase):

    def test_generate_octaved_abstract_chord(self):
        abstract_chord = OctavedAbstractChord([1, 3, 5])
        self.assertIsInstance(abstract_chord.render_symbol('A'), str)
        self.assertIsInstance(abstract_chord.render_symbol_with_inversion('A', 'B'), str)
