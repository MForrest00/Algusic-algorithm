from dataclasses import dataclass


@dataclass
class TempoRange:
    lower_bpm: int
    upper_bpm: int


GRAVE_RANGE = TempoRange(lower_bpm=25, upper_bpm=45)
LARGO_RANGE = TempoRange(lower_bpm=40, upper_bpm=60)
LENTO_RANGE = TempoRange(lower_bpm=45, upper_bpm=60)
LARGHETTO_RANGE = TempoRange(lower_bpm=60, upper_bpm=66)
ADAGIO_RANGE = TempoRange(lower_bpm=66, upper_bpm=76)
ADAGIETTO_RANGE = TempoRange(lower_bpm=70, upper_bpm=80)
MARCIA_MODERATO_RANGE = TempoRange(lower_bpm=83, upper_bpm=85)
ANDANTE_RANGE = TempoRange(lower_bpm=76, upper_bpm=108)
ANDANTINO_RANGE = TempoRange(lower_bpm=80, upper_bpm=108)
ANDANTE_MODERATO_RANGE = TempoRange(lower_bpm=92, upper_bpm=112)
MODERATO_RANGE = TempoRange(lower_bpm=108, upper_bpm=120)
ALLEGRETTO_RANGE = TempoRange(lower_bpm=112, upper_bpm=120)
ALLEGRETTO_MODERATO_RANGE = TempoRange(lower_bpm=116, upper_bpm=120)
ALLEGRO_RANGE = TempoRange(lower_bpm=120, upper_bpm=156)
VIVACE_RANGE = TempoRange(lower_bpm=156, upper_bpm=176)
VIVACISSIMO_RANGE = TempoRange(lower_bpm=172, upper_bpm=176)
ALLEGRISSIMO_RANGE = TempoRange(lower_bpm=172, upper_bpm=176)
ALLEGRO_VIVACE_RANGE = TempoRange(lower_bpm=172, upper_bpm=176)
PRESTO_RANGE = TempoRange(lower_bpm=168, upper_bpm=200)
PRESTISSIMO_RANGE = TempoRange(lower_bpm=200, upper_bpm=240)

NORMAL_MUSIC_TEMPO_RANGE = TempoRange(LARGHETTO_RANGE.lower_bpm, PRESTO_RANGE.upper_bpm)
