from abc import ABC, abstractmethod
from enum import Enum


class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


class Parrot(ABC):

    @abstractmethod
    def speed(self):
        raise NotImplementedError()

    @abstractmethod
    def cry(self):
        raise NotImplementedError()

    @staticmethod
    def _load_factor():
        return 9.0

    @staticmethod
    def _base_speed():
        return 12.0


class EuropeanParrot(Parrot):

    def speed(self):
        return self._base_speed()

    def cry(self):
        return "Sqoork!"


class AfricanParrot(Parrot):
    def __init__(self, number_of_coconuts: int) -> None:
        self._number_of_coconuts = number_of_coconuts

    def speed(self):
        return max(0, self._base_speed() - self._load_factor() * self._number_of_coconuts)

    def cry(self) -> str:
        return "Sqaark!"


class NorwegianBlue(Parrot):
    def __init__(self, voltage: float, nailed: bool) -> None:
        self._voltage = voltage
        self._nailed = nailed

    def speed(self) -> None:
        return 0 if self._nailed else self._compute_base_speed_for_voltage(self._voltage)

    def cry(self):
        return "Bzzzzzz" if self._voltage > 0 else "..."

    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed()])


def new_parrot(
        parrot_type: ParrotType,
        num_coconuts: int = 0,
        voltage: float = 0,
        nailed: bool = False) -> Parrot:
    parrot = None
    match parrot_type:
        case ParrotType.EUROPEAN:
            parrot = EuropeanParrot()
        case ParrotType.AFRICAN:
            parrot = AfricanParrot(num_coconuts)
        case ParrotType.NORWEGIAN_BLUE:
            parrot = NorwegianBlue(voltage, nailed)
        case _:
            raise ValueError(f"Unknown parrot type: {parrot_type}")
    return parrot
