from typing import List


class OctavedAbstractChord:
    def __init__(self, chord_degrees: List[int]):
        self.chord_degrees = chord_degrees

    def render_symbol(self, note_name: str) -> str:
        return "{}({})".format(note_name, "-".join(["R"] + list(map(str, self.chord_degrees))))

    def render_symbol_with_inversion(self, note_name: str, inversion_note_name: str) -> str:
        return f"{self.render_symbol(note_name)}\\{inversion_note_name}"
