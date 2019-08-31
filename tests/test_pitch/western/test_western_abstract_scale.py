import unittest
from algorithm.pitch.western import western_abstract_scale


class TestWesternAbstractScale(unittest.TestCase):

    def test_western_abstract_scale(self):
        for abstract_scale in map(western_abstract_scale.__dict__.get, western_abstract_scale.__all__):
            self.assertLess(max(abstract_scale.scale_degrees), abstract_scale.chromatic_single_octave_note_count)
            self.assertIsInstance(abstract_scale.render_name('A'), str)
            for alternative_name in abstract_scale.alternative_names:
                self.assertIsInstance(abstract_scale.render_name('A', name=alternative_name), str)
