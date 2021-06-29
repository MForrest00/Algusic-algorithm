from algorithm.tools.factor_generator import FactorGenerator


class SongSection:
    def __init__(self, **kwargs):
        """Section of a song

        Possible arguments:
            pitched_density_adjustment_factor (float or int or None): influences likelihood to add more pitched elements
                to the section
            pitched_density_adjustment_probability (float or int or None): base probability of pitched density
                adjustment factor
            pitched_density_adjustment_standard_deviation (float or int or None): base standard deviation of pitched
                density adjustment factor
            rhythmic_density_adjustment_factor (float or int or None): influences likelihood to add more rhythmic
                elements to the section
            rhythmic_density_adjustment_probability (float or int or None): base probability of rhythmic density
                adjustment factor
            rhythmic_density_adjustment_standard_deviation (float or int or None): base standard deviation of rhythmic
                density adjustment factor
            line_repetition_factor (float or int or None): influences likelihood to repeat earlier lines from the same
                section
            line_repetition_probability (float or int or None): base probability of line repetition factor
            line_repetition_standard_deviation (float or int or None): base standard deviation of line repetition factor
            section_repetition_factor (float or int or None): influences likelihood to repeat lines from an earlier
                section of the same type
            section_repetition_probability (float or int or None): base probability of section repetition factor
            section_repetition_standard_deviation (float or int or None): base standard deviation of section repetition
                factor
            volume_adjustment_factor (float or int or None): influences volumes generated in the section
            volume_adjustment_probability (float or int or None): base probability of volume adjustment factor
            volume_adjustment_standard_deviation (float or int or None): base standard deviation of volume adjustment
                factor
            layering_factor (float or int or None): influences likelihood to layer lines throughout the section
            layering_probability (float or int or None): base probability of layering factor
            layering_standard_deviation (float or int or None): base standard deviation of layering factor
        """
        self.fg = FactorGenerator()
        self.pitched_density_adjustment_factor = self.fg.generate_factor(
            factor=kwargs.get("pitched_density_adjustment_factor"),
            probability=kwargs.get("pitched_density_adjustment_probability"),
            standard_deviation=kwargs.get("pitched_density_adjustment_standard_deviation"),
        )
        self.rhythmic_density_adjustment_factor = self.fg.generate_factor(
            factor=kwargs.get("rhythmic_density_adjustment_factor"),
            probability=kwargs.get("rhythmic_density_adjustment_probability"),
            standard_deviation=kwargs.get("rhythmic_density_adjustment_standard_deviation"),
        )
        self.line_repetition_factor = self.fg.generate_factor(
            factor=kwargs.get("line_repetition_factor"),
            probability=kwargs.get("line_repetition_probability"),
            standard_deviation=kwargs.get("line_repetition_standard_deviation"),
        )
        self.section_repetition_factor = self.fg.generate_factor(
            factor=kwargs.get("section_repetition_factor"),
            probability=kwargs.get("section_repetition_probability"),
            standard_deviation=kwargs.get("section_repetition_standard_deviation"),
        )
        self.volume_adjustment_factor = self.fg.generate_factor(
            factor=kwargs.get("volume_adjustment_factor"),
            probability=kwargs.get("volume_adjustment_probability"),
            standard_deviation=kwargs.get("volume_adjustment_standard_deviation"),
        )
        self.layering_factor = self.fg.generate_factor(
            factor=kwargs.get("layering_factor"),
            probability=kwargs.get("layering_probability"),
            standard_deviation=kwargs.get("layering_standard_deviation"),
        )
