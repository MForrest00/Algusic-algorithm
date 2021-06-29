from __future__ import annotations
from typing import Any, Optional, Union


class Sinusoid:
    """A simple representation of a sinusoid

    Sinusoids can be added if they have the same frequency. The returned Sinusoid has the same frequency and an
    amplitude that is the sum of the amplitudes.
    Sinusoids can be subtracted if they have the same frequency. The return is None if the difference of the amplitudes
    is less than or equal to 0. Otherwise, the returned Sinusoid has the same frequency and an amplitude that is the
    difference of the amplitudes.
    Sinusoids can be multiplied or divided by an integer or float greater than 0. The returned Sinusoid has the same
    frequency and an amplitude that is the product or quotient of the amplitude and the integer or float.

    Arguments:
        frequency (int or float): frequency of the sinusoid
        amplitude (int or float): amplitude of the sinusoid
    """

    def __init__(self, frequency: Union[int, float], amplitude: Union[int, float]):
        self.frequency = frequency
        self.amplitude = amplitude

    def __check_valid_number_argument(self, argument: Any) -> None:
        """Checks if the argument is an int or a float and is greater than 0

        Raises:
            TypeError: if argument is not an int or a float
            ValueError: if argument is not greater than 0
        """
        if not isinstance(argument, (int, float)):
            raise TypeError("Frequency and amplitude values must be integers or floats")
        if argument <= 0:
            raise ValueError("Frequency and amplitude values must be greater than 0")

    @property
    def frequency(self) -> float:
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        self.__check_valid_number_argument(frequency)
        self._frequency = float(frequency)

    @property
    def amplitude(self) -> float:
        return self._amplitude

    @amplitude.setter
    def amplitude(self, amplitude):
        self.__check_valid_number_argument(amplitude)
        self._amplitude = float(amplitude)

    def __str__(self):
        return "Sinusoid with frequency of {} and amplitude of {}".format(self.frequency, self.amplitude)

    def __repr__(self):
        return "Sinusoid({}, {})".format(self.frequency, self.amplitude)

    def __add__(self, other: Sinusoid) -> Sinusoid:
        if self.frequency != other.frequency:
            raise ValueError("Only Sinusoids with the same frequency can be added")
        return self.__class__(self.frequency, self.amplitude + other.amplitude)

    def __sub__(self, other: Sinusoid) -> Optional[Sinusoid]:
        if self.frequency != other.frequency:
            raise ValueError("Only Sinusoids with the same frequency can be subtracted")
        if self.amplitude > other.amplitude:
            return self.__class__(self.frequency, self.amplitude - other.amplitude)
        return None

    def __mul__(self, other: Union[int, float]) -> Sinusoid:
        if not isinstance(other, (int, float)) or other <= 0:
            raise ValueError("Sinusoids can only be multiplied by an integer or a float greater than 0")
        return self.__class__(self.frequency, self.amplitude * other)

    def __truediv__(self, other: Union[int, float]) -> Sinusoid:
        if not isinstance(other, (int, float)) or other <= 0:
            raise ValueError("Sinusoids can only be divided by an integer or a float greater than 0")
        return self.__class__(self.frequency, self.amplitude / other)

    def __lt__(self, other: Sinusoid) -> bool:
        return self.frequency < other.frequency

    def __gt__(self, other: Sinusoid) -> bool:
        return self.frequency > other.frequency

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Sinusoid):
            return NotImplemented
        return self.frequency == other.frequency and self.amplitude == other.amplitude

    def __ne__(self, other: Any) -> bool:
        return not self == other

    def __le__(self, other: Sinusoid) -> bool:
        return self < other or self == other

    def __ge__(self, other: Sinusoid) -> bool:
        return self > other or self == other

    def __bool__(self):
        return True

    def __hash__(self):
        return hash((self.frequency, self.amplitude))
