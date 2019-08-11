class OctavedChordContext:

    def __init__(self, chord_degrees):
        self.chord_degrees = chord_degrees

    def render_symbol(self, note_name):
        return '{}({})'.format(note_name, '-'.join(['R'] + list(map(str, self.chord_degrees))))

    def render_symbol_with_inversion(self, note_name, inversion_note_name):
        return '{}\\{}'.format(self.render_symbol(note_name), inversion_note_name)
