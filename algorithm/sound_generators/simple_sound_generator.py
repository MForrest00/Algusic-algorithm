from collections import deque
from pyo import Fader, Pattern, RCOsc, Server


class SimpleSoundGenerator:

    def __init__(self):
        self.server = Server()

    def play_sequence(self, sequence, descent=True):
        if descent:
            sequence = sequence[::-1] + sequence
        sequence = deque(sequence)
        reverse_sequence = deque()
        self.server.boot()
        amp = Fader(fadein=0.005, fadeout=0.05, mul=0.15)
        osc = RCOsc(freq=[100] * max([1] + [len(i) for i in sequence if isinstance(i, list)]), mul=amp).out()

        def get_next_note():
            nonlocal sequence
            nonlocal reverse_sequence
            play_length = 0.5
            amp.dur = play_length
            pat.time = play_length
            try:
                next_freq = sequence.pop()
            except IndexError:
                scale = reverse_sequence.copy()
                reverse_sequence.clear()
                next_freq = scale.pop()
            reverse_sequence.append(next_freq)
            osc.freq = next_freq
            amp.play()

        pat = Pattern(function=get_next_note, time=0.5).play()
        # self.server.gui(locals())
        self.server.start()
        input('Press enter to stop playback')
        self.server.stop()
        self.server.shutdown()


simple_sound_generator = SimpleSoundGenerator()
