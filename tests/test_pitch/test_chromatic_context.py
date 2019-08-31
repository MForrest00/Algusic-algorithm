import random
import unittest
from algorithm.pitch import EqualTemperedTrueOctavedChromaticContext, UnequalTemperedTrueOctavedChromaticContext


class TestEqualTemperedTrueOctavedChromaticContext(unittest.TestCase):

    def test_generate_equal_tempered_true_octaved_chromatic_context(self):
        for s in range(100):
            random.seed(s)
            chromatic_context = EqualTemperedTrueOctavedChromaticContext()
            assert len(chromatic_context.note_names) == len(chromatic_context.chromatic_scale) == \
                   len(chromatic_context.named_chromatic_scale)
            assert len(chromatic_context.flat_note_names) == len(chromatic_context.flat_chromatic_scale) == \
                   len(chromatic_context.flat_named_chromatic_scale)
            self.assertIn(chromatic_context.anchor_hz, chromatic_context.flat_chromatic_scale)
            self.assertGreaterEqual(chromatic_context.flat_chromatic_scale[0], chromatic_context.minimum_hz)
            self.assertLessEqual(chromatic_context.flat_chromatic_scale[-1], chromatic_context.maximum_hz)
            for chromatic_scale in chromatic_context.chromatic_scale:
                self.assertEqual(chromatic_context.single_octave_note_count, len(chromatic_scale))
            for i, chromatic_scale in enumerate(chromatic_context.chromatic_scale[1:], 1):
                for j, note in enumerate(chromatic_scale):
                    if note is None:
                        break
                    previous_scale_note = chromatic_context.chromatic_scale[i-1][j]
                    if previous_scale_note is None:
                        continue
                    self.assertAlmostEqual(note % previous_scale_note, 0)


class TestUnequalTemperedTrueOctavedChromaticContext(unittest.TestCase):

    def test_generate_unequal_tempered_true_octaved_chromatic_context(self):
        for s in range(100):
            random.seed(s)
            chromatic_context = UnequalTemperedTrueOctavedChromaticContext()
            assert len(chromatic_context.note_names) == len(chromatic_context.chromatic_scale) == \
                   len(chromatic_context.named_chromatic_scale)
            assert len(chromatic_context.flat_note_names) == len(chromatic_context.flat_chromatic_scale) == \
                   len(chromatic_context.flat_named_chromatic_scale)
            self.assertIn(chromatic_context.anchor_hz, chromatic_context.flat_chromatic_scale)
            self.assertGreaterEqual(chromatic_context.flat_chromatic_scale[0], chromatic_context.minimum_hz)
            self.assertLessEqual(chromatic_context.flat_chromatic_scale[-1], chromatic_context.maximum_hz)
            for chromatic_scale in chromatic_context.chromatic_scale:
                self.assertEqual(chromatic_context.single_octave_note_count, len(chromatic_scale))
                self.assertEqual(len(chromatic_context.note_ratios), len(chromatic_scale) - 1)
            for i, chromatic_scale in enumerate(chromatic_context.chromatic_scale[1:], 1):
                for j, note in enumerate(chromatic_scale):
                    if note is None:
                        break
                    previous_scale_note = chromatic_context.chromatic_scale[i-1][j]
                    if previous_scale_note is None:
                        continue
                    self.assertAlmostEqual(note % previous_scale_note, 0)
