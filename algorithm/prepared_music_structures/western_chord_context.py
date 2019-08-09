from algorithm.music_structures.chord_context import TrueOctavedChordContext


class WesternTrueOctavedChordContext(TrueOctavedChordContext):

    def __init__(self, chord_degrees, name=None, primary_symbol=None, alternative_symbols=None):
        super().__init__(chord_degrees)
        self.name = name
        self.primary_symbol = primary_symbol
        self.alternative_symbols = alternative_symbols


MajorChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[4, 7], name='Major', primary_symbol='_', alternative_names=['_M'])
MinorChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[3, 7], name='Minor', primary_symbol='_m',
                                   alternative_names=['_min', '_-'])
SixthChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[4, 7, 9], name='Sixth', primary_symbol='_6',
                                   alternative_names=['_major6', '_Maj6', '_M6'])
MinorSixthChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[3, 7, 9], name='Minor Sixth', primary_symbol='_m6',
                                   alternative_names=['_minor6', '_min6', '_-6'])
SixthNinthChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[4, 7, 9, 14], name='Sixth Ninth', primary_symbol='_6/9',
                                   alternative_names=['_6(add9)', '_Maj6(add9)', '_M6(add9)'])
MajorSeventhChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[4, 7, 11], name='Major Seventh', primary_symbol='_maj7',
                                   alternative_names=['_major7', '_M7', '_Maj7'])
DominantSeventhChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[4, 7, 10], name='Dominant Seventh', primary_symbol='_7',
                                   alternative_names=['_dom', '_dom7'])
SeventhFlatFifthChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[4, 6, 10], name='Seventh Flat Fifth', primary_symbol='_7♭5',
                                   alternative_names=['_7(♭5)', '_7(-5)'])
SeventhSharpFifthChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[4, 8, 10], name='Seventh Sharp Fifth', primary_symbol='_7♯5',
                                   alternative_names=['_7(+5)', '_aug7', '_+7'])
MinorSeventhChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[3, 7, 10], name='Minor Seventh', primary_symbol='_m7',
                                   alternative_names=['_min7', '_-7'])
MinorMajorSeventhChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[3, 7, 11], name='Minor With Major Seventh',
                                   primary_symbol='_m(maj7)', alternative_names=['_m(M7)', '_min(Maj7)', '_m(+7)',
                                                                                 '_-(M7)', '_m(addM7)', '_m(add7)',
                                                                                 '_min(addM7)', '_min(+7)',
                                                                                 '_min(add7)'])
MinorSeventhFlatFifthChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[3, 6, 10], name='Minor Seventh Flat Fifth', primary_symbol='_m7♭5',
                                   alternative_names=['_1/2dim', '_1/2dim7', '_m7(♭5)', '_m7(-5)'])
DiminishedSeventhChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[3, 6, 9], name='Diminished Seventh', primary_symbol='_dim7',
                                   alternative_names=['_dim', '_dim7', '_dim/6', '_dim(add6)'])
NinthChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[4, 7, 10, 14], name='Ninth', primary_symbol='_9',
                                   alternative_names=['_7(add9)', '_7/9'])
NinthFlatFifthChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[4, 6, 10, 14], name='Ninth Flat Fifth', primary_symbol='_9♭5',
                                   alternative_names=['_9(♭5)', '_9(-5)', '_7/9(♭5)'])
NinthSharpFifthChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[4, 8, 10, 14], name='Ninth Sharp Fifth', primary_symbol='_9♯5',
                                   alternative_names=['_9(♯5)', '_+9', '_aug9', '_7♯5(add9)'])
MajorNinthChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[4, 7, 11, 14], name='Major Ninth', primary_symbol='_maj9',
                                   alternative_names=['_M9', '_Maj7(add9)', '_M7(add9)', '_major7(add9)', '_M7/9',
                                                      '_Maj7/9'])
MinorNinthChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[3, 7, 10, 14], name='Minor Ninth', primary_symbol='_m9',
                                   alternative_names=['_minor9', '_min9', '_m7/9', '_m7(add9)', '_-7/9', '_-7(add9)',
                                                      '_min7/9', '_min7(add9)'])
MinorEleventhChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[3, 7, 10, 17], name='Minor Eleventh', primary_symbol='_m11',
                                   alternative_names=['_minor11', '_min11', '_m7/11', '_m7(add11)', '_-7(add11)',
                                                      '_-7/11', '_min7/11', '_min7(add11)', '_m7/4', '_m7(add4)',
                                                      '_-7(add4)', '_-7/4', '_min7/4', '_min7(add4)'])
ThirteenthChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[4, 7, 10, 21], name='Thirteenth', primary_symbol='_13',
                                   alternative_names=['_7(add13)', '_7/6', '_7/13', '_7(add6)', '_dom7/6', '_dom7/13',
                                                      '_dom6', '_dom13', '_dom7(add6)', '_dom7(add13)'])
MajorThirteenthChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[4, 7, 11, 21], name='Major Thirteenth', primary_symbol='_maj13',
                                   alternative_names=['_M13', '_Maj7(add13)', '_M7(add13)', '_major7(add13)', '_M7/13',
                                                      '_Maj7/13', '_M6', '_Maj7(add6)', '_M7(add6)', '_major7(add6)',
                                                      '_M7/6', '_Maj7/6'])
MinorThirteenthChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[3, 7, 10, 21], name='Minor Thirteenth', primary_symbol='_m13',
                                   alternative_names=['_minor13', '_min13', '_m7/13', '_m7(add13)', '_-7(add13)',
                                                      '_-7/13', '_min7/13', '_min7(add13)', '_m7/6', '_m7(add6)',
                                                      '_-7(add6)', '_-7/6', '_min7/6', '_min7(add6)'])
SuspendedFourthChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[5, 7], name='Suspended Fourth', primary_symbol='_sus4',
                                   alternative_names=['_4', '_♯3'])
SuspendedSecondChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[2, 7], name='Suspended Second', primary_symbol='_sus2',
                                   alternative_names=['_2'])
DominantSeventhSuspendedFourthChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[5, 7, 10], name='Dominant Seventh Suspended Fourth',
                                   primary_symbol='_7sus4')
DominantSeventhSuspendedSecondChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[2, 7, 10], name='Dominant Seventh Suspended Second',
                                   primary_symbol='_7sus2')
NinthSuspendedFourthChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[5, 7, 10, 14], name='Ninth Suspended Fourth',
                                   primary_symbol='_9sus4')
NinthSuspendedSecondChordContext = \
    WesternTrueOctavedChordContext(chord_degrees=[2, 7, 10, 14], name='Ninth Suspended Second',
                                   primary_symbol='_9sus2')
AugmentedChordContext = WesternTrueOctavedChordContext(chord_degrees=[4, 8], name='Augmented', primary_symbol='_aug')
DiminishedChordContext = WesternTrueOctavedChordContext(chord_degrees=[3, 6], name='Diminished', primary_symbol='_dim')
PowerChordChordContext = WesternTrueOctavedChordContext(chord_degrees=[7], name='Power Chord', primary_symbol='_5')
