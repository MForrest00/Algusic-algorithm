from random import gauss


class SongSection:
    FACTOR_STANDARD_DEVIATION = 0.15

    def __init__(self, line_repetition_factor=None, section_repetition_factor=None,
                 density_factor=None, volume_intensity_factor=None, layering_factor=None):
        """Instantiate a song section.

        Keyword arguments:
        line_repetition_factor -- influences likelihood to repeat earlier lines from the same section
        section_repetition_factor -- influences likelihood to repeat lines from an earlier section of the same type
        density_factor -- influences likelihood to add more elements to the section
        volume_intensity_factor -- influences volumes generated in the section
        layering_factor -- influences likelihood to layer lines throughout the section
        """
        self.line_repetition_factor = line_repetition_factor or self.generate_random_factor()
        self.section_repetition_factor = section_repetition_factor or self.generate_random_factor()
        self.density_factor = density_factor or self.generate_random_factor()
        self.volume_intensity_factor = volume_intensity_factor or self.generate_random_factor()
        self.layering_factor = layering_factor or self.generate_random_factor()

    def generate_random_factor(self):
        max_iterations = 5
        for _ in range(max_iterations):
            possible_factor = gauss(1.0, SongSection.FACTOR_STANDARD_DEVIATION)
            if possible_factor <= 0:
                continue
            return possible_factor
        return 1.0
