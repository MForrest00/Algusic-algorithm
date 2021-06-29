import unittest
import algorithm.pitch.western.western_abstract_chord as western_abstract_chord
import algorithm.pitch.western.western_abstract_scale as western_abstract_scale
import algorithm.pitch.western.western_chromatic_context as western_chromatic_context
from algorithm.pitch.western.western_applied_chord import WesternAppliedChord
from algorithm.pitch.western.western_applied_scale import WesternAppliedScale


class TestWesternAppliedChord(unittest.TestCase):
    def test_generate_wester_applied_chord(self):
        for chromatic_context in map(western_chromatic_context.__dict__.get, western_chromatic_context.__all__):
            for abstract_scale in map(western_abstract_scale.__dict__.get, western_abstract_scale.__all__):
                applied_scale = WesternAppliedScale(chromatic_context, abstract_scale)
                for abstract_chord in map(western_abstract_chord.__dict__.get, western_abstract_chord.__all__):
                    applied_chord = WesternAppliedChord(applied_scale, abstract_chord)
                    self.assertIsInstance(applied_chord.name, str)
