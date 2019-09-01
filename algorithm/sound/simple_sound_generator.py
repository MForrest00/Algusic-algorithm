from collections import deque
from pyo import Fader, Pattern, RCOsc, Server, SfPlayer


class SimpleSoundGenerator:

    def __init__(self):
        self.server = Server()

    def play_pitch_sequences(self, *sequences):
        max_frequency_list_length = max([1] + [len(i) for sequence in sequences
                                               for i in sequence if isinstance(i, list)])
        sequences = deque([deque(sequence) for sequence in sequences])
        sequence = sequences[0].copy()
        self.server.boot()
        amp = Fader(fadein=0.005, fadeout=0.05, mul=0.15)
        osc = RCOsc(freq=[100] * max_frequency_list_length, mul=amp).out()

        def get_next_note():
            nonlocal sequences
            nonlocal sequence
            play_length = 0.5
            amp.dur = play_length
            pat.time = play_length
            try:
                next_freq = sequence.pop()
            except IndexError:
                sequences.rotate(1)
                sequence = sequences[0].copy()
                next_freq = sequence.pop()
            osc.freq = next_freq
            amp.play()

        pat = Pattern(function=get_next_note, time=0.5).play()
        # self.server.gui(locals())
        self.server.start()
        input('Press enter to stop playback')
        self.server.stop()
        self.server.shutdown()

    def play_sample_sequence(self, sequence):
        sample_sequence = sequence.copy()
        self.server.boot()
        sample = sample_sequence.pop()
        sf = SfPlayer(sample.file_path, mul=.3).out()

        def get_next_sample():
            nonlocal sequence
            nonlocal sample_sequence
            nonlocal sf
            try:
                sample = sample_sequence.pop()
            except IndexError:
                sample_sequence = sequence.copy()
                sample = sample_sequence.pop()
            sf = SfPlayer(sample.file_path, mul=.3).out()
            pat.time = sample.length + 0.5

        pat = Pattern(function=get_next_sample, time=sample.length + 0.5).play()
        # self.server.gui(locals())
        self.server.start()
        input('Press enter to stop playback')
        self.server.stop()
        self.server.shutdown()


simple_sound_generator = SimpleSoundGenerator()
