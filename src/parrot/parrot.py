from abc import ABC, abstractmethod
from enum import Enum


class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


class Parrot(ABC):
    def __init__(self, type_of_parrot, number_of_coconuts, voltage, nailed):
        self._type = type_of_parrot
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed

    def speed(self):
        match self._type:
            case ParrotType.EUROPEAN:
                return self._base_speed()
            case ParrotType.AFRICAN:
                return max(0, self._base_speed() - self._load_factor() * self._number_of_coconuts)
            case ParrotType.NORWEGIAN_BLUE:
                return 0 if self._nailed else self._compute_base_speed_for_voltage(self._voltage)
            case _:
                raise ValueError(f"Unknown parrot type: {self._type}")

    @abstractmethod
    def cry(self):
        raise NotImplementedError()

    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed()])

    @staticmethod
    def _load_factor():
        return 9.0

    @staticmethod
    def _base_speed():
        return 12.0


class EuropeanParrot(Parrot):
    def __init__(self, number_of_coconuts: int, voltage: float, nailed: bool) -> None:
        super().__init__(ParrotType.EUROPEAN, number_of_coconuts, voltage, nailed)

    def cry(self):
        return "Sqoork!"


class AfricanParrot(Parrot):
    def __init__(self, number_of_coconuts: int, voltage: float, nailed: bool) -> None:
        super().__init__(ParrotType.AFRICAN, number_of_coconuts, voltage, nailed)

    def cry(self):
        return "Sqaark!"


class NorwegianBlue(Parrot):
    def __init__(self, number_of_coconuts: int, voltage: float, nailed: bool) -> None:
        super().__init__(ParrotType.NORWEGIAN_BLUE, number_of_coconuts, voltage, nailed)

    def cry(self):
        return "Bzzzzzz" if self._voltage > 0 else "..."


def new_parrot(parrot_type: ParrotType, num_coconuts: int, voltage: float, nailed: bool) -> Parrot:
    parrot = None
    match parrot_type:
        case ParrotType.AFRICAN:
            parrot = AfricanParrot(num_coconuts, voltage, nailed)
        case ParrotType.EUROPEAN:
            parrot = EuropeanParrot(num_coconuts, voltage, nailed)
        case ParrotType.NORWEGIAN_BLUE:
            parrot = NorwegianBlue(num_coconuts, voltage, nailed)
        case _:
            raise ValueError(f"Unknown parrot type: {parrot_type}")
    return parrot
