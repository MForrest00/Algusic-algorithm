from algorithm.music_structures.scale_context import TrueOctavedScaleContext


class WesternTrueOctavedScaleContext(TrueOctavedScaleContext):

    def __init__(self, scale_degrees=None, primary_name=None, alternative_names=None):
        super().__init__(chromatic_single_octave_note_count=12, scale_degrees=scale_degrees)
        self.interval_short_names = ['m2', 'M2', 'm3', 'M3', 'P4', 'A4/d5', 'P5', 'm6', 'M6', 'm7', 'M7']
        self.interval_long_names = ['Minor Second', 'Major Second', 'Minor Third', 'Major Third', 'Perfect Fourth',
                                    'Augmented Fourth/Diminished Fifth', 'Perfect Fifth', 'Minor Sixth', 'Major Sixth',
                                    'Minor Seventh', 'Major Seventh']
        self.primary_name = primary_name
        self.alternative_names = alternative_names


MajorScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[2, 4, 5, 7, 9, 11], primary_name='Major',
                                   alternative_names=['Ionian'])
MelodicMinorScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[2, 3, 5, 7, 9, 11], primary_name='Melodic Minor')
HarmonicMinorScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[2, 3, 5, 7, 8, 11], primary_name='Harmonic Minor',
                                   alternative_names=['Mohammedan'])
NaturalMinorScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[2, 3, 5, 7, 8, 10], primary_name='Natural Minor',
                                   alternative_names=['Aeolian'])
DorianScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[2, 3, 5, 7, 9, 10], primary_name='Dorian')
PhrygianScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[1, 3, 5, 7, 8, 10], primary_name='Phrygian',
                                   alternative_names=['Neopolitan Minor'])
LydianScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[2, 4, 6, 7, 9, 11], primary_name='Lydian')
MixolydianScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[2, 4, 5, 7, 9, 10], primary_name='Mixolydian')
LocrianScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[1, 3, 5, 6, 8, 10], primary_name='Locrian')
BluesScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[3, 5, 6, 7, 10], primary_name='Blues')
DiminishedHalftoneWholetoneScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[1, 3, 4, 6, 7, 9, 10],
                                   primary_name='Diminished (Halftone - Wholetone)')
DiminishedWholetoneHalftoneScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[2, 3, 5, 6, 8, 9, 11],
                                   primary_name='Diminished (Wholetone - Halftone)')
WholeToneScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[2, 4, 6, 8, 10], primary_name='Whole Tone')
MajorPentatonicScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[2, 4, 7, 9], primary_name='Major Pentatonic',
                                   alternative_names=['Mongolian'])
MinorPentatonicScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[3, 5, 7, 10], primary_name='Minor Pentatonic')
AugmentedScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[3, 4, 7, 8, 11], primary_name='Augmented')
LeadingWholeToneScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[2, 4, 6, 8, 10, 11], primary_name='Leading Whole Tone')
DoubleHarmonicScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[1, 4, 5, 7, 8, 11], primary_name='Double Harmonic',
                                   alternative_names=['Byzantine'])
OvertoneScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[2, 4, 6, 7, 9, 10], primary_name='Overtone',
                                   alternative_names=['Lydian ♭7'])
SixToneSymmetricalScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[1, 4, 5, 8, 9], primary_name='Six Tone Symmetrical')
AlteredScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[1, 3, 4, 6, 8, 10], primary_name='Altered')
AlteredDoubleFlat7ScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[1, 3, 4, 6, 8, 9], primary_name='Altered ♭♭7')
EngimaticScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[1, 4, 6, 8, 10, 11], primary_name='Enigmatic')
DorianFlat2ScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[1, 3, 5, 6, 8, 9], primary_name='Dorian ♭2')
AugmentedLydianScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[2, 4, 6, 8, 9, 11], primary_name='Augmented Lydian')
MixolydianFlatSixScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[2, 4, 5, 7, 8, 10], primary_name='Mixolydian ♭6',
                                   alternative_names=['Hindu'])
Locrian2ScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[2, 3, 5, 6, 8, 10], primary_name='Locrian 2')
Locrian6ScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[1, 3, 5, 6, 9, 10], primary_name='Locrian 6')
AugmentedIonianScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[2, 4, 5, 8, 9, 11], primary_name='Augmented Ionian')
DorianSharp4ScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[2, 3, 6, 7, 9, 10], primary_name='Dorian ♯4')
MajorPhrygianScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[1, 4, 5, 7, 8, 10], primary_name='Major Phrygian')
LydianSharp9ScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[3, 4, 6, 7, 9, 11], primary_name='Lydian ♯9')
DiminishedLydianScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[2, 3, 6, 7, 9, 11], primary_name='Diminished Lydian')
MinorLydianScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[2, 4, 6, 7, 8, 10], primary_name='Minor Lydian')
ArabianScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[2, 4, 5, 6, 8, 10], primary_name='Arabian')
BalineseScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[1, 3, 6, 8], primary_name='Balinese')
ChineseScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[4, 6, 7, 11], primary_name='Chinese')
EgyptianScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[2, 5, 7, 10], primary_name='Egyptian')
EightToneSpanishScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[1, 3, 4, 5, 6, 8, 10], primary_name='Eight Tone Spanish')
HirajoshiScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[2, 3, 7, 8], primary_name='Hirajoshi')
HungarianMajorScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[3, 4, 6, 7, 9, 10], primary_name='Hungarian Major')
HungarianMinorScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[2, 3, 6, 7, 8, 11], primary_name='Hungarian Minor',
                                   alternative_names=['Gypsy'])
IchikosuchoScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[2, 4, 5, 6, 7, 9, 11], primary_name='Ichikosucho')
KumoiScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[2, 3, 7, 9], primary_name='Kumoi')
NeopolitanScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[1, 3, 5, 7, 8, 11], primary_name='Neopolitan')
NeopolitanMajorScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[1, 3, 5, 7, 9, 11], primary_name='Neopolitan Major')
PelogScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[1, 3, 7, 8], primary_name='Pelog')
PersianScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[1, 4, 5, 6, 8, 11], primary_name='Persian')
PrometheusScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[2, 4, 6, 9, 10], primary_name='Prometheus')
PrometheusNeopolitanScaleContext = \
    WesternTrueOctavedScaleContext(scale_degrees=[1, 4, 6, 9, 10], primary_name='Prometheus Neopolitan')
PurviThetaScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[1, 4, 6, 7, 8, 11], primary_name='Purvi Theta')
TodiThetaScaleContext = WesternTrueOctavedScaleContext(scale_degrees=[1, 3, 6, 7, 8, 11], primary_name='Todi Theta')
