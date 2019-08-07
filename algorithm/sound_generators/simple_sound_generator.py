from collections import deque
from pyo import Fader, Pattern, RCOsc, Server


class SimpleSoundGenerator:

    def __init__(self):
        self.server = Server()

    def play_octaved_chromatic_scale(self, chromatic_context, start_index=None):
        if start_index:
            end_index = start_index + chromatic_context.single_octave_note_count + 1
            scale = chromatic_context.flat_chromatic_scale[start_index:min(end_index, len(chromatic_context.flat_chromatic_scale))]
        else:
            scales_range = len(chromatic_context.chromatic_scale)
            scale = chromatic_context.chromatic_scale[scales_range // 2]
            if scales_range > 1:
                scale += chromatic_context.chromatic_scale[scales_range // 2 + 1][:1]
        scale = deque(reversed(scale))
        print(len(scale), scale)
        self.server.boot()
        amp = Fader(fadein=0.005, fadeout=0.05, mul=.15)
        osc = RCOsc(freq=100, mul=amp).out()

        def get_next_note():
            play_length = 0.5
            amp.dur = play_length
            pat.time = play_length
            next_freq = scale.pop()
            scale.appendleft(next_freq)
            osc.freq = next_freq
            amp.play()

        pat = Pattern(function=get_next_note, time=0.5).play()
        self.server.start()
        input('Press enter to stop playback')
        self.server.stop()
        self.server.shutdown()


simple_sound_generator = SimpleSoundGenerator()
