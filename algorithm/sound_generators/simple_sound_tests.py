from algorithm.music_elements.abstract_scale import OctavedAbstractScale
from algorithm.music_elements.applied_chord import AppliedOctavedChord
from algorithm.music_elements.applied_scale import AppliedOctavedScale
from algorithm.music_elements.chromatic_context import EqualTemperedTrueOctavedChromaticContext, \
    UnequalTemperedTrueOctavedChromaticContext
from algorithm.prepared_music_elements.western_abstract_chord import MajorAbstractChord
from algorithm.prepared_music_elements.western_abstract_scale import MajorAbstractScale, PhrygianAbstractScale
from algorithm.prepared_music_elements.western_chromatic_context import WesternEqualTempered440ChromaticContext, \
    WesternJustTemperedA440ChromaticContext
from algorithm.sound_generators.simple_sound_generator import simple_sound_generator


def generate_sequence_from_scale(nested_scale, flat_scale, start_index=None):
    if start_index:
        target_end_index = start_index + max(len(single_octave_scale) for single_octave_scale in nested_scale) + 1
        end_index = min(target_end_index, len(flat_scale))
        return flat_scale[start_index:end_index]
    else:
        scales_range = len(nested_scale)
        scale = nested_scale[scales_range // 2]
        if scales_range > 1:
            scale += nested_scale[scales_range // 2 + 1][:1]
        return scale


def test_1(start_index=None):
    sequence = generate_sequence_from_scale(WesternEqualTempered440ChromaticContext.chromatic_scale,
                                            WesternEqualTempered440ChromaticContext.flat_chromatic_scale)
    print('Playing western equal tempered 440 chromatic scale')
    print('Chromatic sequence:', sequence)
    simple_sound_generator.play_sequence(list(reversed(sequence)))


def test_2():
    sequence = generate_sequence_from_scale(WesternJustTemperedA440ChromaticContext.chromatic_scale,
                                            WesternJustTemperedA440ChromaticContext.flat_chromatic_scale)
    print('Playing western just tempered chromatic scale with A at 440')
    print('Chromatic sequence:', sequence)
    simple_sound_generator.play_sequence(list(reversed(sequence)))


def test_3():
    scale = EqualTemperedTrueOctavedChromaticContext()
    sequence = generate_sequence_from_scale(scale.chromatic_scale, scale.flat_chromatic_scale)
    print('Playing random equal tempered true octaved chromatic scale')
    print('Chromatic sequence:', sequence)
    simple_sound_generator.play_sequence(list(reversed(sequence)))


def test_4():
    scale = UnequalTemperedTrueOctavedChromaticContext()
    sequence = generate_sequence_from_scale(scale.chromatic_scale, scale.flat_chromatic_scale)
    print('Playing random unequal tempered true octaved chromatic scale')
    print('Chromatic sequence:', sequence)
    simple_sound_generator.play_sequence(list(reversed(sequence)))


def test_5():
    scale = AppliedOctavedScale(WesternEqualTempered440ChromaticContext, MajorAbstractScale)
    chromatic_sequence = generate_sequence_from_scale(scale.chromatic_context.chromatic_scale,
                                                      scale.chromatic_context.flat_chromatic_scale)
    sequence = generate_sequence_from_scale(scale.scale, scale.flat_scale)
    print('Playing western equal tempered 440 Major scale with chromatic context scale')
    print('Chromatic sequence:', chromatic_sequence)
    print('Scale sequence:', sequence)
    simple_sound_generator.play_sequence(list(reversed(chromatic_sequence)) + list(reversed(sequence)))


def test_6():
    scale = AppliedOctavedScale(WesternEqualTempered440ChromaticContext, PhrygianAbstractScale)
    chromatic_sequence = generate_sequence_from_scale(scale.chromatic_context.chromatic_scale,
                                                      scale.chromatic_context.flat_chromatic_scale)
    sequence = generate_sequence_from_scale(scale.scale, scale.flat_scale)
    print('Playing western equal tempered 440 Phrygian scale with chromatic context scale')
    print('Chromatic sequence:', chromatic_sequence)
    print('Scale sequence:', sequence)
    simple_sound_generator.play_sequence(list(reversed(chromatic_sequence)) + list(reversed(sequence)))


def test_7():
    chromatic_context = EqualTemperedTrueOctavedChromaticContext()
    abstract_scale = OctavedAbstractScale(chromatic_single_octave_note_count=chromatic_context.single_octave_note_count)
    scale = AppliedOctavedScale(chromatic_context, abstract_scale)
    chromatic_sequence = generate_sequence_from_scale(scale.chromatic_context.chromatic_scale,
                                                      scale.chromatic_context.flat_chromatic_scale)
    sequence = generate_sequence_from_scale(scale.scale, scale.flat_scale)
    print('Playing random scale with random equal tempered true octaved chromatic context scale')
    print('Chromatic sequence:', chromatic_sequence)
    print('Scale sequence:', sequence)
    simple_sound_generator.play_sequence(list(reversed(chromatic_sequence)) + list(reversed(sequence)))


def test_8():
    scale = AppliedOctavedScale(WesternEqualTempered440ChromaticContext, MajorAbstractScale)
    chord = AppliedOctavedChord(scale, MajorAbstractChord, chord_anchor='D4')
    sequence = [chord.chord]
    print('Playing western equal tempered 440 Major chord on D4')
    print('Chord sequence:', sequence)
    simple_sound_generator.play_sequence(sequence)
