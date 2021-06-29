from dataclasses import dataclass


@dataclass
class FrequencyRange:
    lower_hz: int
    upper_hz: int


SUB_BASS_RANGE = FrequencyRange(lower_hz=20, upper_hz=60)
BASS_RANGE = FrequencyRange(lower_hz=60, upper_hz=250)
LOW_MIDRANGE_RANGE = FrequencyRange(lower_hz=250, upper_hz=500)
MIDRANGE_RANGE = FrequencyRange(lower_hz=500, upper_hz=2000)
UPPER_MIDRANGE_RANGE = FrequencyRange(lower_hz=2000, upper_hz=4000)
PRESENCE_RANGE = FrequencyRange(lower_hz=4000, upper_hz=6000)
BRILLIANCE_RANGE = FrequencyRange(lower_hz=6000, upper_hz=20000)

NORMAL_MUSIC_FREQUENCY_RANGE = FrequencyRange(lower_hz=SUB_BASS_RANGE.lower_hz, upper_hz=PRESENCE_RANGE.upper_hz)
