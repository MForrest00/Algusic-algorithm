from algorithm.rhythm.percussive_context import PercussiveContext
from algorithm.structure.applied_sectioned_song import AppliedSectionedSong


class PercussiveThread:

    def __init__(self, applied_sectioned_song: AppliedSectionedSong, percussive_context: PercussiveContext):
        self.applied_sectioned_song = applied_sectioned_song
        self.percussive_context = percussive_context
