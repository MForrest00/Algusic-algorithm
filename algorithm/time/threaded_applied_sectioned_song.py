from algorithm.pitch.western.western_applied_scale import WesternAppliedScale
from algorithm.pitch.western.western_abstract_scale import MajorAbstractScale
from algorithm.pitch.western.western_chromatic_context import WesternEqualTempered440ChromaticContext
from algorithm.structure.applied_sectioned_song import AppliedSectionedSong
from algorithm.rhythm import PercussiveContext
from algorithm.time.percussive_thread import PercussiveThread


class ThreadedAppliedSectionedSong:

    def __init__(self, applied_sectioned_song, percussive_context=None, pitched_context=None):
        self.applied_sectioned_song = applied_sectioned_song
        self.percussive_context = percussive_context or PercussiveContext()
        self.pitched_context = pitched_context or WesternAppliedScale(WesternEqualTempered440ChromaticContext(),
                                                                      MajorAbstractScale())
        self.percussive_threads = self.generate_percussive_threads()

    @property
    def applied_sectioned_song(self):
        return self._applied_sectioned_song

    @applied_sectioned_song.setter
    def applied_sectioned_song(self, applied_sectioned_song):
        if not isinstance(applied_sectioned_song, AppliedSectionedSong):
            raise TypeError('Applied sectioned song must be of type AppliedSectionedSong')
        self._applied_sectioned_song = applied_sectioned_song

    @property
    def percussive_context(self):
        return self._percussive_context

    @percussive_context.setter
    def percussive_context(self, percussive_context):
        if not isinstance(percussive_context, PercussiveContext):
            raise TypeError('Percussive context must be of type PercussiveContext')
        self._percussive_context = percussive_context

    def generate_percussive_threads(self):
        for song_section in self.applied_sectioned_song.song_sections:
            pass
