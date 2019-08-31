import unittest
from algorithm.pitch.western import western_chromatic_context


class TestWesternChromaticContext(unittest.TestCase):

    def test_western_chromatic_context(self):
        for chromatic_context in map(western_chromatic_context.__dict__.get, western_chromatic_context.__all__):
            self.assertEqual(len(chromatic_context.flat_chromatic_scale), 108)
            self.assertEqual(dict(chromatic_context.flat_named_chromatic_scale).get('A4'), chromatic_context.anchor_hz)
            self.assertIsInstance(str(chromatic_context), str)
