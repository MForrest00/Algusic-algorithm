from collections import defaultdict
from random import choice, uniform
from algorithm.structure.song_section import SongSection
from algorithm.structure.song_skeleton import SectionedSongSkeleton
from algorithm.tools.factor_generator import FactorGenerator


class AppliedSectionedSong:
    def __init__(self, song_skeleton, song_sections=None, **kwargs):
        self.fg = FactorGenerator()
        self.section_reoccurrence_factor = self.fg.generate_factor(
            factor=kwargs.get("section_reoccurrence_factor"),
            probability=kwargs.get("section_reoccurrence_probability", 0.7),
            standard_deviation=kwargs.get("section_reoccurrence_standard_deviation"),
        )
        self.song_skeleton = song_skeleton
        self.song_sections = self.generate_song_sections(
            song_sections or [None] * len(self.song_skeleton.sectioned_bar_lengths)
        )

    @property
    def song_skeleton(self):
        return self._song_skeleton

    @song_skeleton.setter
    def song_skeleton(self, song_skeleton):
        if not isinstance(song_skeleton, SectionedSongSkeleton):
            raise TypeError("Sectioned song skeleton must be of type SectionedSongSkeleton")
        self._song_skeleton = song_skeleton

    @property
    def song_sections(self):
        return self._song_sections

    @song_sections.setter
    def song_sections(self, song_sections):
        if not isinstance(song_sections, list) or not all(
            i is None or isinstance(i, SongSection) for i in song_sections
        ):
            raise TypeError("Song sections must be a list of None or SongSection instances")
        if len(song_sections) != len(self.song_skeleton.sectioned_bar_lengths):
            raise ValueError(
                "Length of song sections must be equal to the length of sectioned bar lengths in the song skeleton"
            )
        self._song_sections = song_sections

    def generate_song_sections(self, current_song_sections):
        song_sections = []
        bar_length_sections = defaultdict(list)
        for song_section, sectioned_bar_length in zip(current_song_sections, self.song_skeleton.sectioned_bar_lengths):
            if song_section is None:
                section_repeat = uniform(0.0, 1.0) < self.section_reoccurrence_factor
                if section_repeat:
                    possible_sections = bar_length_sections.get(sectioned_bar_length)
                    if possible_sections:
                        song_sections.append(choice(possible_sections))
                        continue
                created_song_section = SongSection()
                song_sections.append(created_song_section)
                bar_length_sections[sectioned_bar_length].append(created_song_section)
            else:
                song_sections.append(song_section)
        return song_sections
