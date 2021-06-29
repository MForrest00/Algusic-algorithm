import unittest
from algorithm.pitch.western import western_abstract_chord


class TestWesternAbstractChord(unittest.TestCase):
    def test_western_abstract_scale(self):
        for abstract_chord in map(western_abstract_chord.__dict__.get, western_abstract_chord.__all__):
            self.assertIsInstance(abstract_chord.render_name("A"), str)
            self.assertIsInstance(abstract_chord.render_name_with_inversion("A", "B"), str)
            self.assertIsInstance(abstract_chord.render_symbol("A"), str)
            self.assertIsInstance(abstract_chord.render_symbol_with_inversion("A", "B"), str)
            for alternative_symbol in abstract_chord.alternative_symbols:
                self.assertIsInstance(abstract_chord.render_symbol("A", symbol=alternative_symbol), str)
                self.assertIsInstance(
                    abstract_chord.render_symbol_with_inversion("A", "B", symbol=alternative_symbol), str
                )
