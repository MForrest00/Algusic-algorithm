from collections import deque
from pyo import Fader, Pattern, RCOsc, Server


class SimpleSoundGenerator:

    def __init__(self):
        self.server = Server()

    def generate_ranged_scale(self, scale_list):
        scales_range = len(scale_list)
        scale = scale_list[scales_range // 2]
        if scales_range > 1:
            scale += scale_list[scales_range // 2 + 1][:1]
        return scale

    def play_scale(self, scale):
        scale = deque(reversed(scale))
        reverse_scale = deque()
        self.server.boot()
        amp = Fader(fadein=0.005, fadeout=0.05, mul=.15)
        osc = RCOsc(freq=100, mul=amp).out()

        def get_next_note():
            nonlocal scale
            nonlocal reverse_scale
            play_length = 0.5
            amp.dur = play_length
            pat.time = play_length
            try:
                next_freq = scale.pop()
            except IndexError:
                scale = reverse_scale.copy()
                reverse_scale.clear()
                next_freq = scale.pop()
            reverse_scale.append(next_freq)
            osc.freq = next_freq
            amp.play()

        pat = Pattern(function=get_next_note, time=0.5).play()
        self.server.start()
        input('Press enter to stop playback')
        self.server.stop()
        self.server.shutdown()

    def play_octaved_chromatic_scale(self, chromatic_context, start_index=None):
        if start_index:
            target_end_index = start_index + chromatic_context.single_octave_note_count + 1
            end_index = min(target_end_index, len(chromatic_context.flat_chromatic_scale))
            scale = chromatic_context.flat_chromatic_scale[start_index:end_index]
        else:
            scale = self.generate_ranged_scale(chromatic_context.chromatic_scale)
        print('{} note scale over {} true octaves:'.format(chromatic_context.single_octave_note_count,
                                                           chromatic_context.octave_range), scale)
        self.play_scale(scale)

    def play_applied_octaved_scale(self, applied_scale):
        scale = self.generate_ranged_scale(applied_scale.scale)
        print('{} note scale over {} true octaves:'.format(len(applied_scale.scale_context.scale_degrees) + 1,
                                                           applied_scale.chromatic_context.octave_range), scale)
        self.play_scale(scale)


simple_sound_generator = SimpleSoundGenerator()
