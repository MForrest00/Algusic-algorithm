from algorithm.music_structures.chromatic_context import EqualTemperedTrueOctavedChromaticContext, \
    UnequalTemperedTrueOctavedChromaticContext
from algorithm.prepared_music_structures.prepared_chromatic_context import WesternEqualTempered440ChromaticContext, \
    WesternJustTemperedA440ChromaticContext
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
