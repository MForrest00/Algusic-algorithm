from algorithm.music_elements.scale_context import OctavedScaleContext


class WesternOctavedScaleContext(OctavedScaleContext):

    def __init__(self, scale_degrees=None, primary_name=None, alternative_names=None):
        super().__init__(chromatic_single_octave_note_count=12, scale_degrees=scale_degrees)
        self.interval_short_names = ['m2', 'M2', 'm3', 'M3', 'P4', 'A4/d5', 'P5', 'm6', 'M6', 'm7', 'M7']
        self.interval_long_names = ['Minor Second', 'Major Second', 'Minor Third', 'Major Third', 'Perfect Fourth',
                                    'Augmented Fourth/Diminished Fifth', 'Perfect Fifth', 'Minor Sixth', 'Major Sixth',
                                    'Minor Seventh', 'Major Seventh']
        self.primary_name = primary_name
        self.alternative_names = alternative_names


MajorScaleContext = \
    WesternOctavedScaleContext(scale_degrees=[2, 4, 5, 7, 9, 11], primary_name='Major', alternative_names=['Ionian'])
MelodicMinorScaleContext = WesternOctavedScaleContext(scale_degrees=[2, 3, 5, 7, 9, 11], primary_name='Melodic Minor')
HarmonicMinorScaleContext = \
    WesternOctavedScaleContext(scale_degrees=[2, 3, 5, 7, 8, 11], primary_name='Harmonic Minor',
                               alternative_names=['Mohammedan'])
NaturalMinorScaleContext = \
    WesternOctavedScaleContext(scale_degrees=[2, 3, 5, 7, 8, 10], primary_name='Natural Minor',
                               alternative_names=['Aeolian'])
DorianScaleContext = WesternOctavedScaleContext(scale_degrees=[2, 3, 5, 7, 9, 10], primary_name='Dorian')
PhrygianScaleContext = \
    WesternOctavedScaleContext(scale_degrees=[1, 3, 5, 7, 8, 10], primary_name='Phrygian',
                               alternative_names=['Neopolitan Minor'])
LydianScaleContext = WesternOctavedScaleContext(scale_degrees=[2, 4, 6, 7, 9, 11], primary_name='Lydian')
MixolydianScaleContext = WesternOctavedScaleContext(scale_degrees=[2, 4, 5, 7, 9, 10], primary_name='Mixolydian')
LocrianScaleContext = WesternOctavedScaleContext(scale_degrees=[1, 3, 5, 6, 8, 10], primary_name='Locrian')
BluesScaleContext = WesternOctavedScaleContext(scale_degrees=[3, 5, 6, 7, 10], primary_name='Blues')
DiminishedHalftoneWholetoneScaleContext = \
    WesternOctavedScaleContext(scale_degrees=[1, 3, 4, 6, 7, 9, 10], primary_name='Diminished (Halftone - Wholetone)')
DiminishedWholetoneHalftoneScaleContext = \
    WesternOctavedScaleContext(scale_degrees=[2, 3, 5, 6, 8, 9, 11], primary_name='Diminished (Wholetone - Halftone)')
WholeToneScaleContext = WesternOctavedScaleContext(scale_degrees=[2, 4, 6, 8, 10], primary_name='Whole Tone')
MajorPentatonicScaleContext = \
    WesternOctavedScaleContext(scale_degrees=[2, 4, 7, 9], primary_name='Major Pentatonic',
                               alternative_names=['Mongolian'])
MinorPentatonicScaleContext = WesternOctavedScaleContext(scale_degrees=[3, 5, 7, 10], primary_name='Minor Pentatonic')
AugmentedScaleContext = WesternOctavedScaleContext(scale_degrees=[3, 4, 7, 8, 11], primary_name='Augmented')
LeadingWholeToneScaleContext = \
    WesternOctavedScaleContext(scale_degrees=[2, 4, 6, 8, 10, 11], primary_name='Leading Whole Tone')
DoubleHarmonicScaleContext = \
    WesternOctavedScaleContext(scale_degrees=[1, 4, 5, 7, 8, 11], primary_name='Double Harmonic',
                               alternative_names=['Byzantine'])
OvertoneScaleContext = \
    WesternOctavedScaleContext(scale_degrees=[2, 4, 6, 7, 9, 10], primary_name='Overtone',
                               alternative_names=['Lydian ♭7'])
SixToneSymmetricalScaleContext = \
    WesternOctavedScaleContext(scale_degrees=[1, 4, 5, 8, 9], primary_name='Six Tone Symmetrical')
AlteredScaleContext = WesternOctavedScaleContext(scale_degrees=[1, 3, 4, 6, 8, 10], primary_name='Altered')
AlteredDoubleFlat7ScaleContext = \
    WesternOctavedScaleContext(scale_degrees=[1, 3, 4, 6, 8, 9], primary_name='Altered ♭♭7')
EngimaticScaleContext = WesternOctavedScaleContext(scale_degrees=[1, 4, 6, 8, 10, 11], primary_name='Enigmatic')
DorianFlat2ScaleContext = WesternOctavedScaleContext(scale_degrees=[1, 3, 5, 6, 8, 9], primary_name='Dorian ♭2')
AugmentedLydianScaleContext = \
    WesternOctavedScaleContext(scale_degrees=[2, 4, 6, 8, 9, 11], primary_name='Augmented Lydian')
MixolydianFlatSixScaleContext = \
    WesternOctavedScaleContext(scale_degrees=[2, 4, 5, 7, 8, 10], primary_name='Mixolydian ♭6',
                               alternative_names=['Hindu'])
Locrian2ScaleContext = WesternOctavedScaleContext(scale_degrees=[2, 3, 5, 6, 8, 10], primary_name='Locrian 2')
Locrian6ScaleContext = WesternOctavedScaleContext(scale_degrees=[1, 3, 5, 6, 9, 10], primary_name='Locrian 6')
AugmentedIonianScaleContext = \
    WesternOctavedScaleContext(scale_degrees=[2, 4, 5, 8, 9, 11], primary_name='Augmented Ionian')
DorianSharp4ScaleContext = WesternOctavedScaleContext(scale_degrees=[2, 3, 6, 7, 9, 10], primary_name='Dorian ♯4')
MajorPhrygianScaleContext = \
    WesternOctavedScaleContext(scale_degrees=[1, 4, 5, 7, 8, 10], primary_name='Major Phrygian')
LydianSharp9ScaleContext = WesternOctavedScaleContext(scale_degrees=[3, 4, 6, 7, 9, 11], primary_name='Lydian ♯9')
DiminishedLydianScaleContext = \
    WesternOctavedScaleContext(scale_degrees=[2, 3, 6, 7, 9, 11], primary_name='Diminished Lydian')
MinorLydianScaleContext = WesternOctavedScaleContext(scale_degrees=[2, 4, 6, 7, 8, 10], primary_name='Minor Lydian')
ArabianScaleContext = WesternOctavedScaleContext(scale_degrees=[2, 4, 5, 6, 8, 10], primary_name='Arabian')
BalineseScaleContext = WesternOctavedScaleContext(scale_degrees=[1, 3, 6, 8], primary_name='Balinese')
ChineseScaleContext = WesternOctavedScaleContext(scale_degrees=[4, 6, 7, 11], primary_name='Chinese')
EgyptianScaleContext = WesternOctavedScaleContext(scale_degrees=[2, 5, 7, 10], primary_name='Egyptian')
EightToneSpanishScaleContext = \
    WesternOctavedScaleContext(scale_degrees=[1, 3, 4, 5, 6, 8, 10], primary_name='Eight Tone Spanish')
HirajoshiScaleContext = WesternOctavedScaleContext(scale_degrees=[2, 3, 7, 8], primary_name='Hirajoshi')
HungarianMajorScaleContext = \
    WesternOctavedScaleContext(scale_degrees=[3, 4, 6, 7, 9, 10], primary_name='Hungarian Major')
HungarianMinorScaleContext = \
    WesternOctavedScaleContext(scale_degrees=[2, 3, 6, 7, 8, 11], primary_name='Hungarian Minor',
                               alternative_names=['Gypsy'])
IchikosuchoScaleContext = WesternOctavedScaleContext(scale_degrees=[2, 4, 5, 6, 7, 9, 11], primary_name='Ichikosucho')
KumoiScaleContext = WesternOctavedScaleContext(scale_degrees=[2, 3, 7, 9], primary_name='Kumoi')
NeopolitanScaleContext = WesternOctavedScaleContext(scale_degrees=[1, 3, 5, 7, 8, 11], primary_name='Neopolitan')
NeopolitanMajorScaleContext = \
    WesternOctavedScaleContext(scale_degrees=[1, 3, 5, 7, 9, 11], primary_name='Neopolitan Major')
PelogScaleContext = WesternOctavedScaleContext(scale_degrees=[1, 3, 7, 8], primary_name='Pelog')
PersianScaleContext = WesternOctavedScaleContext(scale_degrees=[1, 4, 5, 6, 8, 11], primary_name='Persian')
PrometheusScaleContext = WesternOctavedScaleContext(scale_degrees=[2, 4, 6, 9, 10], primary_name='Prometheus')
PrometheusNeopolitanScaleContext = \
    WesternOctavedScaleContext(scale_degrees=[1, 4, 6, 9, 10], primary_name='Prometheus Neopolitan')
PurviThetaScaleContext = WesternOctavedScaleContext(scale_degrees=[1, 4, 6, 7, 8, 11], primary_name='Purvi Theta')
TodiThetaScaleContext = WesternOctavedScaleContext(scale_degrees=[1, 3, 6, 7, 8, 11], primary_name='Todi Theta')
