import random
import unittest
from algorithm.pitch import AppliedOctavedChord, AppliedOctavedScale, EqualTemperedTrueOctavedChromaticContext, \
    OctavedAbstractScale, OctavedAbstractChord, UnequalTemperedTrueOctavedChromaticContext


class TestEqualTemperedAppliedOctavedChord(unittest.TestCase):

    def test_generate_equal_tempered_applied_octaved_chord(self):
        for s in range(100):
            random.seed(s)
            chromatic_context = EqualTemperedTrueOctavedChromaticContext()
            abstract_scale = OctavedAbstractScale(chromatic_context.single_octave_note_count)
            applied_scale = AppliedOctavedScale(chromatic_context, abstract_scale)
            abstract_chord = OctavedAbstractChord([d for d in abstract_scale.scale_degrees])
            applied_chord = AppliedOctavedChord(applied_scale, abstract_chord)
            self.assertTrue(applied_chord.chord_in_scale)
            self.assertTrue(applied_chord.chord_degrees_in_scale)
            self.assertIsInstance(applied_chord.symbol, str)
        for s in range(100, 200):
            random.seed(s)
            chromatic_context = EqualTemperedTrueOctavedChromaticContext()
            abstract_scale = OctavedAbstractScale(chromatic_context.single_octave_note_count)
            applied_scale = AppliedOctavedScale(chromatic_context, abstract_scale)
            abstract_chord = OctavedAbstractChord([d for d in range(1, chromatic_context.single_octave_note_count)
                                                   if d not in abstract_scale.scale_degrees])
            applied_chord = AppliedOctavedChord(applied_scale, abstract_chord)
            if len(applied_chord.chord) > 1:
                self.assertFalse(applied_chord.chord_in_scale)
            else:
                self.assertTrue(applied_chord.chord_in_scale)
            if len(abstract_chord.chord_degrees) > 0:
                self.assertFalse(applied_chord.chord_degrees_in_scale)
            else:
                self.assertTrue(applied_chord.chord_degrees_in_scale)
            self.assertIsInstance(applied_chord.symbol, str)


class TestUnequalTemperedAppliedOctavedChord(unittest.TestCase):

    def test_generate_unequal_tempered_applied_octaved_chord(self):
        for s in range(100):
            random.seed(s)
            chromatic_context = UnequalTemperedTrueOctavedChromaticContext()
            abstract_scale = OctavedAbstractScale(chromatic_context.single_octave_note_count)
            applied_scale = AppliedOctavedScale(chromatic_context, abstract_scale)
            abstract_chord = OctavedAbstractChord([d for d in abstract_scale.scale_degrees])
            applied_chord = AppliedOctavedChord(applied_scale, abstract_chord)
            self.assertTrue(applied_chord.chord_in_scale)
            self.assertTrue(applied_chord.chord_degrees_in_scale)
            self.assertIsInstance(applied_chord.symbol, str)
        for s in range(100, 200):
            random.seed(s)
            chromatic_context = EqualTemperedTrueOctavedChromaticContext()
            abstract_scale = OctavedAbstractScale(chromatic_context.single_octave_note_count)
            applied_scale = AppliedOctavedScale(chromatic_context, abstract_scale)
            abstract_chord = OctavedAbstractChord([d for d in range(1, chromatic_context.single_octave_note_count)
                                                   if d not in abstract_scale.scale_degrees])
            applied_chord = AppliedOctavedChord(applied_scale, abstract_chord)
            if len(applied_chord.chord) > 1:
                self.assertFalse(applied_chord.chord_in_scale)
            else:
                self.assertTrue(applied_chord.chord_in_scale)
            if len(abstract_chord.chord_degrees) > 0:
                self.assertFalse(applied_chord.chord_degrees_in_scale)
            else:
                self.assertTrue(applied_chord.chord_degrees_in_scale)
            self.assertIsInstance(applied_chord.symbol, str)
