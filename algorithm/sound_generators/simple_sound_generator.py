from collections import deque
from pyo import Fader, Pattern, RCOsc, Server


class SimpleSoundGenerator:

    def __init__(self):
        self.server = Server()

    def play_sequences(self, *sequences):
        max_frequency_list_length = max([1] + [len(i) for sequence in sequences
                                               for i in sequence if isinstance(i, list)])
        sequences = deque([deque(sequence) for sequence in sequences])
        sequence = sequences.pop()
        sequences.appendleft(sequence.copy())
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
                sequence = sequences.pop()
                sequences.appendleft(sequence.copy())
                next_freq = sequence.pop()
            osc.freq = next_freq
            amp.play()

        pat = Pattern(function=get_next_note, time=0.5).play()
        # self.server.gui(locals())
        self.server.start()
        input('Press enter to stop playback')
        self.server.stop()
        self.server.shutdown()


simple_sound_generator = SimpleSoundGenerator()
