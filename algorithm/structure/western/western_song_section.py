from algorithm.structure.song_section import SongSection


class WesternSongSection(SongSection):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


IntroSongSection = WesternSongSection()
VerseSongSection = WesternSongSection()
ChorusSongSection = WesternSongSection()
BridgeSongSection = WesternSongSection()
Middle8SongSection = WesternSongSection()
LiftSongSection = WesternSongSection()
