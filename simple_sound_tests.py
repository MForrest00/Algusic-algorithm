from math import ceil
from random import choice
from algorithm.pitch import (
    AppliedOctavedChord,
    AppliedOctavedScale,
    EqualTemperedTrueOctavedChromaticContext,
    OctavedAbstractScale,
    UnequalTemperedTrueOctavedChromaticContext,
)
from algorithm.pitch.western import (
    MajorAbstractChord,
    MajorAbstractScale,
    PhrygianAbstractScale,
    WesternEqualTempered440ChromaticContext,
    WesternJustTemperedA440ChromaticContext,
)
from algorithm.rhythm import PercussiveContext
from algorithm.sound.simple_sound_generator import simple_sound_generator


def generate_sequence_from_scale(nested_scale, flat_scale, start_index=None, descent=True):
    if start_index:
        target_end_index = start_index + max(len(single_octave_scale) for single_octave_scale in nested_scale) + 1
        end_index = min(target_end_index, len(flat_scale))
        scale = flat_scale[start_index:end_index]
    else:
        scales_range = len(nested_scale)
        scale = nested_scale[scales_range // 2][:]
        if scales_range > 1:
            scale += nested_scale[scales_range // 2 + 1][:1]
    if descent:
        return scale + scale[::-1]
    return scale


def test_1():
    sequence = generate_sequence_from_scale(
        WesternEqualTempered440ChromaticContext.chromatic_scale,
        WesternEqualTempered440ChromaticContext.flat_chromatic_scale,
    )
    print("Playing western equal tempered 440 chromatic scale")
    print("Chromatic sequence:", sequence[: ceil(len(sequence) / 2)])
    simple_sound_generator.play_pitch_sequences(sequence)


def test_2():
    sequence = generate_sequence_from_scale(
        WesternJustTemperedA440ChromaticContext.chromatic_scale,
        WesternJustTemperedA440ChromaticContext.flat_chromatic_scale,
    )
    print("Playing western just tempered chromatic scale with A at 440")
    print("Chromatic sequence:", sequence[: ceil(len(sequence) / 2)])
    simple_sound_generator.play_pitch_sequences(sequence)


def test_3():
    chromatic_context = EqualTemperedTrueOctavedChromaticContext()
    sequence = generate_sequence_from_scale(chromatic_context.chromatic_scale, chromatic_context.flat_chromatic_scale)
    print("Playing random equal tempered true octaved chromatic scale")
    print("Single octave note count:", chromatic_context.single_octave_note_count)
    print("Octave range:", chromatic_context.octave_range)
    print("Chromatic sequence:", sequence[: ceil(len(sequence) / 2)])
    simple_sound_generator.play_pitch_sequences(sequence)


def test_4():
    chromatic_context = UnequalTemperedTrueOctavedChromaticContext()
    sequence = generate_sequence_from_scale(chromatic_context.chromatic_scale, chromatic_context.flat_chromatic_scale)
    print("Playing random unequal tempered true octaved chromatic scale")
    print("Single octave note count:", chromatic_context.single_octave_note_count)
    print("Octave range:", chromatic_context.octave_range)
    print("Chromatic sequence:", sequence[: ceil(len(sequence) / 2)])
    simple_sound_generator.play_pitch_sequences(sequence)


def test_5():
    applied_scale = AppliedOctavedScale(WesternEqualTempered440ChromaticContext, MajorAbstractScale)
    chromatic_sequence = generate_sequence_from_scale(
        applied_scale.chromatic_context.chromatic_scale,
        applied_scale.chromatic_context.flat_chromatic_scale,
    )
    scale_sequence = generate_sequence_from_scale(applied_scale.scale, applied_scale.flat_scale)
    print("Playing western equal tempered 440 Major scale with chromatic context scale")
    print("Chromatic sequence:", chromatic_sequence[: ceil(len(chromatic_sequence) / 2)])
    print("Scale sequence:", scale_sequence[: ceil(len(scale_sequence) / 2)])
    simple_sound_generator.play_pitch_sequences(scale_sequence, chromatic_sequence)


def test_6():
    applied_scale = AppliedOctavedScale(WesternEqualTempered440ChromaticContext, PhrygianAbstractScale)
    chromatic_sequence = generate_sequence_from_scale(
        applied_scale.chromatic_context.chromatic_scale,
        applied_scale.chromatic_context.flat_chromatic_scale,
    )
    scale_sequence = generate_sequence_from_scale(applied_scale.scale, applied_scale.flat_scale)
    print("Playing western equal tempered 440 Phrygian scale with chromatic context scale")
    print("Chromatic sequence:", chromatic_sequence[: ceil(len(chromatic_sequence) / 2)])
    print("Scale sequence:", scale_sequence[: ceil(len(scale_sequence) / 2)])
    simple_sound_generator.play_pitch_sequences(scale_sequence, chromatic_sequence)


def test_7():
    chromatic_context = EqualTemperedTrueOctavedChromaticContext()
    abstract_scale = OctavedAbstractScale(chromatic_single_octave_note_count=chromatic_context.single_octave_note_count)
    applied_scale = AppliedOctavedScale(chromatic_context, abstract_scale)
    chromatic_sequence = generate_sequence_from_scale(
        applied_scale.chromatic_context.chromatic_scale,
        applied_scale.chromatic_context.flat_chromatic_scale,
    )
    scale_sequence = generate_sequence_from_scale(applied_scale.scale, applied_scale.flat_scale)
    print("Playing random scale with random equal tempered true octaved chromatic context scale")
    print("Chromatic single octave note count:", chromatic_context.single_octave_note_count)
    print("Chromatic octave range:", chromatic_context.octave_range)
    print("Scale single octave note count:", len(applied_scale.abstract_scale.scale_degrees) + 1)
    print("Chromatic sequence:", chromatic_sequence[: ceil(len(chromatic_sequence) / 2)])
    print("Scale sequence:", scale_sequence[: ceil(len(scale_sequence) / 2)])
    simple_sound_generator.play_pitch_sequences(scale_sequence, chromatic_sequence)


def test_8(chord_anchor="D4"):
    applied_scale = AppliedOctavedScale(WesternEqualTempered440ChromaticContext, MajorAbstractScale)
    applied_chord = AppliedOctavedChord(applied_scale, MajorAbstractChord, chord_anchor=chord_anchor)
    sequence = [applied_chord.chord]
    print(f"Playing western equal tempered 440 Major chord on {chord_anchor}")
    print("Chord sequence:", sequence)
    simple_sound_generator.play_pitch_sequences(sequence)


def test_9():
    percussive_context = PercussiveContext()
    random_samples = [choice(percussive_context.samples) for _ in range(10)]
    simple_sound_generator.play_sample_sequence(random_samples)


if __name__ == "__main__":
    test_3()
