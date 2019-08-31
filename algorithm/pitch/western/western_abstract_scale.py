from algorithm.pitch.abstract_scale import OctavedAbstractScale


__all__ = ['MajorAbstractScale', 'MelodicMinorAbstractScale', 'HarmonicMinorAbstractScale', 'NaturalMinorAbstractScale',
           'DorianAbstractScale', 'PhrygianAbstractScale', 'LydianAbstractScale', 'MixolydianAbstractScale',
           'LocrianAbstractScale', 'BluesAbstractScale', 'DiminishedHalftoneWholetoneAbstractScale',
           'DiminishedWholetoneHalftoneAbstractScale', 'WholeToneAbstractScale', 'MajorPentatonicAbstractScale',
           'MinorPentatonicAbstractScale', 'AugmentedAbstractScale', 'LeadingWholeToneAbstractScale',
           'DoubleHarmonicAbstractScale', 'OvertoneAbstractScale', 'SixToneSymmetricalAbstractScale',
           'AlteredAbstractScale', 'AlteredDoubleFlat7AbstractScale', 'EngimaticAbstractScale',
           'DorianFlat2AbstractScale', 'AugmentedLydianAbstractScale', 'MixolydianFlatSixAbstractScale',
           'Locrian2AbstractScale', 'Locrian6AbstractScale', 'AugmentedIonianAbstractScale',
           'DorianSharp4AbstractScale', 'MajorPhrygianAbstractScale', 'LydianSharp9AbstractScale',
           'DiminishedLydianAbstractScale', 'MinorLydianAbstractScale', 'ArabianAbstractScale', 'BalineseAbstractScale',
           'ChineseAbstractScale', 'EgyptianAbstractScale', 'EightToneSpanishAbstractScale', 'HirajoshiAbstractScale',
           'HungarianMajorAbstractScale', 'HungarianMinorAbstractScale', 'IchikosuchoAbstractScale',
           'KumoiAbstractScale', 'NeopolitanAbstractScale', 'NeopolitanMajorAbstractScale', 'PelogAbstractScale',
           'PersianAbstractScale', 'PrometheusAbstractScale', 'PrometheusNeopolitanAbstractScale',
           'PurviThetaAbstractScale', 'TodiThetaAbstractScale']


class WesternOctavedAbstractScale(OctavedAbstractScale):

    def __init__(self, scale_degrees=None, primary_name=None, alternative_names=None):
        super().__init__(chromatic_single_octave_note_count=12, scale_degrees=scale_degrees)
        self.interval_short_names = ['m2', 'M2', 'm3', 'M3', 'P4', 'A4/d5', 'P5', 'm6', 'M6', 'm7', 'M7']
        self.interval_long_names = ['Minor Second', 'Major Second', 'Minor Third', 'Major Third', 'Perfect Fourth',
                                    'Augmented Fourth/Diminished Fifth', 'Perfect Fifth', 'Minor Sixth', 'Major Sixth',
                                    'Minor Seventh', 'Major Seventh']
        self.primary_name = primary_name
        self.alternative_names = alternative_names


MajorAbstractScale = \
    WesternOctavedAbstractScale(scale_degrees=[2, 4, 5, 7, 9, 11], primary_name='Major', alternative_names=['Ionian'])
MelodicMinorAbstractScale = WesternOctavedAbstractScale(scale_degrees=[2, 3, 5, 7, 9, 11], primary_name='Melodic Minor')
HarmonicMinorAbstractScale = \
    WesternOctavedAbstractScale(scale_degrees=[2, 3, 5, 7, 8, 11], primary_name='Harmonic Minor',
                                alternative_names=['Mohammedan'])
NaturalMinorAbstractScale = \
    WesternOctavedAbstractScale(scale_degrees=[2, 3, 5, 7, 8, 10], primary_name='Natural Minor',
                                alternative_names=['Aeolian'])
DorianAbstractScale = WesternOctavedAbstractScale(scale_degrees=[2, 3, 5, 7, 9, 10], primary_name='Dorian')
PhrygianAbstractScale = \
    WesternOctavedAbstractScale(scale_degrees=[1, 3, 5, 7, 8, 10], primary_name='Phrygian',
                                alternative_names=['Neopolitan Minor'])
LydianAbstractScale = WesternOctavedAbstractScale(scale_degrees=[2, 4, 6, 7, 9, 11], primary_name='Lydian')
MixolydianAbstractScale = WesternOctavedAbstractScale(scale_degrees=[2, 4, 5, 7, 9, 10], primary_name='Mixolydian')
LocrianAbstractScale = WesternOctavedAbstractScale(scale_degrees=[1, 3, 5, 6, 8, 10], primary_name='Locrian')
BluesAbstractScale = WesternOctavedAbstractScale(scale_degrees=[3, 5, 6, 7, 10], primary_name='Blues')
DiminishedHalftoneWholetoneAbstractScale = \
    WesternOctavedAbstractScale(scale_degrees=[1, 3, 4, 6, 7, 9, 10], primary_name='Diminished (Halftone - Wholetone)')
DiminishedWholetoneHalftoneAbstractScale = \
    WesternOctavedAbstractScale(scale_degrees=[2, 3, 5, 6, 8, 9, 11], primary_name='Diminished (Wholetone - Halftone)')
WholeToneAbstractScale = WesternOctavedAbstractScale(scale_degrees=[2, 4, 6, 8, 10], primary_name='Whole Tone')
MajorPentatonicAbstractScale = \
    WesternOctavedAbstractScale(scale_degrees=[2, 4, 7, 9], primary_name='Major Pentatonic',
                                alternative_names=['Mongolian'])
MinorPentatonicAbstractScale = WesternOctavedAbstractScale(scale_degrees=[3, 5, 7, 10], primary_name='Minor Pentatonic')
AugmentedAbstractScale = WesternOctavedAbstractScale(scale_degrees=[3, 4, 7, 8, 11], primary_name='Augmented')
LeadingWholeToneAbstractScale = \
    WesternOctavedAbstractScale(scale_degrees=[2, 4, 6, 8, 10, 11], primary_name='Leading Whole Tone')
DoubleHarmonicAbstractScale = \
    WesternOctavedAbstractScale(scale_degrees=[1, 4, 5, 7, 8, 11], primary_name='Double Harmonic',
                                alternative_names=['Byzantine'])
OvertoneAbstractScale = \
    WesternOctavedAbstractScale(scale_degrees=[2, 4, 6, 7, 9, 10], primary_name='Overtone',
                                alternative_names=['Lydian ♭7'])
SixToneSymmetricalAbstractScale = \
    WesternOctavedAbstractScale(scale_degrees=[1, 4, 5, 8, 9], primary_name='Six Tone Symmetrical')
AlteredAbstractScale = WesternOctavedAbstractScale(scale_degrees=[1, 3, 4, 6, 8, 10], primary_name='Altered')
AlteredDoubleFlat7AbstractScale = \
    WesternOctavedAbstractScale(scale_degrees=[1, 3, 4, 6, 8, 9], primary_name='Altered ♭♭7')
EngimaticAbstractScale = WesternOctavedAbstractScale(scale_degrees=[1, 4, 6, 8, 10, 11], primary_name='Enigmatic')
DorianFlat2AbstractScale = WesternOctavedAbstractScale(scale_degrees=[1, 3, 5, 6, 8, 9], primary_name='Dorian ♭2')
AugmentedLydianAbstractScale = \
    WesternOctavedAbstractScale(scale_degrees=[2, 4, 6, 8, 9, 11], primary_name='Augmented Lydian')
MixolydianFlatSixAbstractScale = \
    WesternOctavedAbstractScale(scale_degrees=[2, 4, 5, 7, 8, 10], primary_name='Mixolydian ♭6',
                                alternative_names=['Hindu'])
Locrian2AbstractScale = WesternOctavedAbstractScale(scale_degrees=[2, 3, 5, 6, 8, 10], primary_name='Locrian 2')
Locrian6AbstractScale = WesternOctavedAbstractScale(scale_degrees=[1, 3, 5, 6, 9, 10], primary_name='Locrian 6')
AugmentedIonianAbstractScale = \
    WesternOctavedAbstractScale(scale_degrees=[2, 4, 5, 8, 9, 11], primary_name='Augmented Ionian')
DorianSharp4AbstractScale = WesternOctavedAbstractScale(scale_degrees=[2, 3, 6, 7, 9, 10], primary_name='Dorian ♯4')
MajorPhrygianAbstractScale = \
    WesternOctavedAbstractScale(scale_degrees=[1, 4, 5, 7, 8, 10], primary_name='Major Phrygian')
LydianSharp9AbstractScale = WesternOctavedAbstractScale(scale_degrees=[3, 4, 6, 7, 9, 11], primary_name='Lydian ♯9')
DiminishedLydianAbstractScale = \
    WesternOctavedAbstractScale(scale_degrees=[2, 3, 6, 7, 9, 11], primary_name='Diminished Lydian')
MinorLydianAbstractScale = WesternOctavedAbstractScale(scale_degrees=[2, 4, 6, 7, 8, 10], primary_name='Minor Lydian')
ArabianAbstractScale = WesternOctavedAbstractScale(scale_degrees=[2, 4, 5, 6, 8, 10], primary_name='Arabian')
BalineseAbstractScale = WesternOctavedAbstractScale(scale_degrees=[1, 3, 6, 8], primary_name='Balinese')
ChineseAbstractScale = WesternOctavedAbstractScale(scale_degrees=[4, 6, 7, 11], primary_name='Chinese')
EgyptianAbstractScale = WesternOctavedAbstractScale(scale_degrees=[2, 5, 7, 10], primary_name='Egyptian')
EightToneSpanishAbstractScale = \
    WesternOctavedAbstractScale(scale_degrees=[1, 3, 4, 5, 6, 8, 10], primary_name='Eight Tone Spanish')
HirajoshiAbstractScale = WesternOctavedAbstractScale(scale_degrees=[2, 3, 7, 8], primary_name='Hirajoshi')
HungarianMajorAbstractScale = \
    WesternOctavedAbstractScale(scale_degrees=[3, 4, 6, 7, 9, 10], primary_name='Hungarian Major')
HungarianMinorAbstractScale = \
    WesternOctavedAbstractScale(scale_degrees=[2, 3, 6, 7, 8, 11], primary_name='Hungarian Minor',
                                alternative_names=['Gypsy'])
IchikosuchoAbstractScale = WesternOctavedAbstractScale(scale_degrees=[2, 4, 5, 6, 7, 9, 11], primary_name='Ichikosucho')
KumoiAbstractScale = WesternOctavedAbstractScale(scale_degrees=[2, 3, 7, 9], primary_name='Kumoi')
NeopolitanAbstractScale = WesternOctavedAbstractScale(scale_degrees=[1, 3, 5, 7, 8, 11], primary_name='Neopolitan')
NeopolitanMajorAbstractScale = \
    WesternOctavedAbstractScale(scale_degrees=[1, 3, 5, 7, 9, 11], primary_name='Neopolitan Major')
PelogAbstractScale = WesternOctavedAbstractScale(scale_degrees=[1, 3, 7, 8], primary_name='Pelog')
PersianAbstractScale = WesternOctavedAbstractScale(scale_degrees=[1, 4, 5, 6, 8, 11], primary_name='Persian')
PrometheusAbstractScale = WesternOctavedAbstractScale(scale_degrees=[2, 4, 6, 9, 10], primary_name='Prometheus')
PrometheusNeopolitanAbstractScale = \
    WesternOctavedAbstractScale(scale_degrees=[1, 4, 6, 9, 10], primary_name='Prometheus Neopolitan')
PurviThetaAbstractScale = WesternOctavedAbstractScale(scale_degrees=[1, 4, 6, 7, 8, 11], primary_name='Purvi Theta')
TodiThetaAbstractScale = WesternOctavedAbstractScale(scale_degrees=[1, 3, 6, 7, 8, 11], primary_name='Todi Theta')
