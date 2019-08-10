from algorithm.music_elements.applied_scale_context import AppliedOctavedScaleContext
from algorithm.music_elements.chromatic_context import EqualTemperedTrueOctavedChromaticContext, \
    UnequalTemperedTrueOctavedChromaticContext
from algorithm.music_elements.scale_context import OctavedScaleContext
from algorithm.prepared_music_elements.western_chromatic_context import WesternEqualTempered440ChromaticContext, \
    WesternJustTemperedA440ChromaticContext
from algorithm.prepared_music_elements.western_scale_context import MajorScaleContext, PhrygianScaleContext
from algorithm.sound_generators.simple_sound_generator import simple_sound_generator


def test_1():
    simple_sound_generator.play_octaved_chromatic_scale(WesternEqualTempered440ChromaticContext)


def test_2():
    simple_sound_generator.play_octaved_chromatic_scale(WesternJustTemperedA440ChromaticContext)


def test_3():
    scale = EqualTemperedTrueOctavedChromaticContext()
    simple_sound_generator.play_octaved_chromatic_scale(scale)


def test_4():
    scale = UnequalTemperedTrueOctavedChromaticContext()
    simple_sound_generator.play_octaved_chromatic_scale(scale)


def test_5():
    scale = AppliedOctavedScaleContext(WesternEqualTempered440ChromaticContext, MajorScaleContext)
    simple_sound_generator.play_applied_octaved_scale_with_chromatic(scale)


def test_6():
    scale = AppliedOctavedScaleContext(WesternEqualTempered440ChromaticContext, PhrygianScaleContext)
    simple_sound_generator.play_applied_octaved_scale_with_chromatic(scale)


def test_7():
    chromatic_scale = EqualTemperedTrueOctavedChromaticContext()
    scale = OctavedScaleContext(chromatic_single_octave_note_count=chromatic_scale.single_octave_note_count)
    applied_scale = AppliedOctavedScaleContext(chromatic_scale, scale)
    simple_sound_generator.play_applied_octaved_scale_with_chromatic(applied_scale)
