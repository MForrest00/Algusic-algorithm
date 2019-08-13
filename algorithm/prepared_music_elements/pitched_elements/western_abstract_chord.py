from algorithm.music_elements.pitched_elements.abstract_chord import OctavedAbstractChord


class WesternOctavedAbstractChord(OctavedAbstractChord):

    def __init__(self, chord_degrees, name=None, primary_symbol=None, alternative_symbols=None):
        super().__init__(chord_degrees)
        self.name = name
        self.primary_symbol = primary_symbol
        self.alternative_symbols = alternative_symbols

    def render_symbol(self, note_name, symbol=None):
        if symbol is None:
            symbol = self.primary_symbol
        return symbol.replace('_', note_name)

    def render_symbol_with_inversion(self, note_name, inversion_note_name, symbol=None):
        return f'{self.render_symbol(note_name, symbol=symbol)}\\{inversion_note_name}'


MajorAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[4, 7], name='Major', primary_symbol='_', alternative_symbols=['_M'])
MinorAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[3, 7], name='Minor', primary_symbol='_m',
                                alternative_symbols=['_min', '_-'])
SixthAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[4, 7, 9], name='Sixth', primary_symbol='_6',
                                alternative_symbols=['_major6', '_Maj6', '_M6'])
MinorSixthAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[3, 7, 9], name='Minor Sixth', primary_symbol='_m6',
                                alternative_symbols=['_minor6', '_min6', '_-6'])
SixthNinthAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[4, 7, 9, 14], name='Sixth Ninth', primary_symbol='_6/9',
                                alternative_symbols=['_6(add9)', '_Maj6(add9)', '_M6(add9)'])
MajorSeventhAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[4, 7, 11], name='Major Seventh', primary_symbol='_maj7',
                                alternative_symbols=['_major7', '_M7', '_Maj7'])
DominantSeventhAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[4, 7, 10], name='Dominant Seventh', primary_symbol='_7',
                                alternative_symbols=['_dom', '_dom7'])
SeventhFlatFifthAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[4, 6, 10], name='Seventh Flat Fifth', primary_symbol='_7♭5',
                                alternative_symbols=['_7(♭5)', '_7(-5)'])
SeventhSharpFifthAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[4, 8, 10], name='Seventh Sharp Fifth', primary_symbol='_7♯5',
                                alternative_symbols=['_7(+5)', '_aug7', '_+7'])
MinorSeventhAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[3, 7, 10], name='Minor Seventh', primary_symbol='_m7',
                                alternative_symbols=['_min7', '_-7'])
MinorMajorSeventhAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[3, 7, 11], name='Minor With Major Seventh', primary_symbol='_m(maj7)',
                                alternative_symbols=['_m(M7)', '_min(Maj7)', '_m(+7)', '_-(M7)', '_m(addM7)',
                                                     '_m(add7)', '_min(addM7)', '_min(+7)', '_min(add7)'])
MinorSeventhFlatFifthAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[3, 6, 10], name='Minor Seventh Flat Fifth', primary_symbol='_m7♭5',
                                alternative_symbols=['_1/2dim', '_1/2dim7', '_m7(♭5)', '_m7(-5)'])
DiminishedSeventhAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[3, 6, 9], name='Diminished Seventh', primary_symbol='_dim7',
                                alternative_symbols=['_dim', '_dim7', '_dim/6', '_dim(add6)'])
NinthAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[4, 7, 10, 14], name='Ninth', primary_symbol='_9',
                                alternative_symbols=['_7(add9)', '_7/9'])
NinthFlatFifthAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[4, 6, 10, 14], name='Ninth Flat Fifth', primary_symbol='_9♭5',
                                alternative_symbols=['_9(♭5)', '_9(-5)', '_7/9(♭5)'])
NinthSharpFifthAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[4, 8, 10, 14], name='Ninth Sharp Fifth', primary_symbol='_9♯5',
                                alternative_symbols=['_9(♯5)', '_+9', '_aug9', '_7♯5(add9)'])
MajorNinthAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[4, 7, 11, 14], name='Major Ninth', primary_symbol='_maj9',
                                alternative_symbols=['_M9', '_Maj7(add9)', '_M7(add9)', '_major7(add9)', '_M7/9',
                                                     '_Maj7/9'])
MinorNinthAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[3, 7, 10, 14], name='Minor Ninth', primary_symbol='_m9',
                                alternative_symbols=['_minor9', '_min9', '_m7/9', '_m7(add9)', '_-7/9', '_-7(add9)',
                                                     '_min7/9', '_min7(add9)'])
MinorEleventhAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[3, 7, 10, 17], name='Minor Eleventh', primary_symbol='_m11',
                                alternative_symbols=['_minor11', '_min11', '_m7/11', '_m7(add11)', '_-7(add11)',
                                                     '_-7/11', '_min7/11', '_min7(add11)', '_m7/4', '_m7(add4)',
                                                     '_-7(add4)', '_-7/4', '_min7/4', '_min7(add4)'])
ThirteenthAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[4, 7, 10, 21], name='Thirteenth', primary_symbol='_13',
                                alternative_symbols=['_7(add13)', '_7/6', '_7/13', '_7(add6)', '_dom7/6', '_dom7/13',
                                                     '_dom6', '_dom13', '_dom7(add6)', '_dom7(add13)'])
MajorThirteenthAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[4, 7, 11, 21], name='Major Thirteenth', primary_symbol='_maj13',
                                alternative_symbols=['_M13', '_Maj7(add13)', '_M7(add13)', '_major7(add13)', '_M7/13',
                                                     '_Maj7/13', '_M6', '_Maj7(add6)', '_M7(add6)', '_major7(add6)',
                                                     '_M7/6', '_Maj7/6'])
MinorThirteenthAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[3, 7, 10, 21], name='Minor Thirteenth', primary_symbol='_m13',
                                alternative_symbols=['_minor13', '_min13', '_m7/13', '_m7(add13)', '_-7(add13)',
                                                     '_-7/13', '_min7/13', '_min7(add13)', '_m7/6', '_m7(add6)',
                                                     '_-7(add6)', '_-7/6', '_min7/6', '_min7(add6)'])
SuspendedFourthAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[5, 7], name='Suspended Fourth', primary_symbol='_sus4',
                                alternative_symbols=['_4', '_♯3'])
SuspendedSecondAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[2, 7], name='Suspended Second', primary_symbol='_sus2',
                                alternative_symbols=['_2'])
DominantSeventhSuspendedFourthAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[5, 7, 10], name='Dominant Seventh Suspended Fourth',
                                primary_symbol='_7sus4')
DominantSeventhSuspendedSecondAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[2, 7, 10], name='Dominant Seventh Suspended Second',
                                primary_symbol='_7sus2')
NinthSuspendedFourthAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[5, 7, 10, 14], name='Ninth Suspended Fourth', primary_symbol='_9sus4')
NinthSuspendedSecondAbstractChord = \
    WesternOctavedAbstractChord(chord_degrees=[2, 7, 10, 14], name='Ninth Suspended Second', primary_symbol='_9sus2')
AugmentedAbstractChord = WesternOctavedAbstractChord(chord_degrees=[4, 8], name='Augmented', primary_symbol='_aug')
DiminishedAbstractChord = WesternOctavedAbstractChord(chord_degrees=[3, 6], name='Diminished', primary_symbol='_dim')
PowerChordAbstractChord = WesternOctavedAbstractChord(chord_degrees=[7], name='Power Chord', primary_symbol='_5')
