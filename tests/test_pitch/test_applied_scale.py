import random
import unittest
from algorithm.pitch.abstract_scale import OctavedAbstractScale
from algorithm.pitch.applied_scale import AppliedOctavedScale
from algorithm.pitch.chromatic_context import (
    EqualTemperedTrueOctavedChromaticContext,
    UnequalTemperedTrueOctavedChromaticContext,
)


class TestEqualTemperedAppliedOctavedScale(unittest.TestCase):
    def test_generate_equal_tempered_applied_octaved_scale(self):
        for s in range(100):
            random.seed(s)
            chromatic_context = EqualTemperedTrueOctavedChromaticContext()
            abstract_scale = OctavedAbstractScale(chromatic_context.single_octave_note_count)
            applied_scale = AppliedOctavedScale(chromatic_context, abstract_scale)
            assert (
                len(applied_scale.note_names)
                == len(applied_scale.scale)
                == len(applied_scale.named_scale)
                == len(applied_scale.altered_note_names)
                == len(applied_scale.altered_scale)
                == len(applied_scale.altered_named_scale)
                == len(chromatic_context.note_names)
                == len(chromatic_context.chromatic_scale)
                == len(chromatic_context.named_chromatic_scale)
            )
            assert (
                len(applied_scale.flat_note_names)
                == len(applied_scale.flat_scale)
                == len(applied_scale.flat_named_scale)
            )
            assert (
                len(applied_scale.flat_altered_note_names)
                == len(applied_scale.flat_altered_scale)
                == len(applied_scale.flat_altered_named_scale)
            )
            self.assertEqual(
                len(applied_scale.flat_scale) + len(applied_scale.flat_altered_scale),
                len(chromatic_context.flat_chromatic_scale),
            )


class TestUnequalTemperedAppliedOctavedScale(unittest.TestCase):
    def test_generate_unequal_tempered_applied_octaved_scale(self):
        for s in range(100):
            random.seed(s)
            chromatic_context = UnequalTemperedTrueOctavedChromaticContext()
            abstract_scale = OctavedAbstractScale(chromatic_context.single_octave_note_count)
            applied_scale = AppliedOctavedScale(chromatic_context, abstract_scale)
            assert (
                len(applied_scale.note_names)
                == len(applied_scale.scale)
                == len(applied_scale.named_scale)
                == len(applied_scale.altered_note_names)
                == len(applied_scale.altered_scale)
                == len(applied_scale.altered_named_scale)
                == len(chromatic_context.note_names)
                == len(chromatic_context.chromatic_scale)
                == len(chromatic_context.named_chromatic_scale)
            )
            assert (
                len(applied_scale.flat_note_names)
                == len(applied_scale.flat_scale)
                == len(applied_scale.flat_named_scale)
            )
            assert (
                len(applied_scale.flat_altered_note_names)
                == len(applied_scale.flat_altered_scale)
                == len(applied_scale.flat_altered_named_scale)
            )
            self.assertEqual(
                len(applied_scale.flat_scale) + len(applied_scale.flat_altered_scale),
                len(chromatic_context.flat_chromatic_scale),
            )
