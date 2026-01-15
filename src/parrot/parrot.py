from abc import ABC, abstractmethod
from enum import Enum


class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


class Parrot(ABC):

    @abstractmethod
    def speed(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def cry(self) -> str:
        raise NotImplementedError()

    @staticmethod
    def _load_factor() -> float:
        return 9.0

    @staticmethod
    def _base_speed() -> float:
        return 12.0


class EuropeanParrot(Parrot):

    def speed(self) -> float:
        return self._base_speed()

    def cry(self) -> str:
        return "Sqoork!"


class AfricanParrot(Parrot):
    def __init__(self, number_of_coconuts: float) -> None:
        self._number_of_coconuts = number_of_coconuts

    def speed(self) -> float:
        return max(0., self._base_speed() - self._load_factor() * self._number_of_coconuts)

    def cry(self) -> str:
        return "Sqaark!"


class NorwegianBlue(Parrot):
    def __init__(self, voltage: float, nailed: bool) -> None:
        self._voltage = voltage
        self._nailed = nailed

    def speed(self) -> float:
        return 0 if self._nailed else self._compute_base_speed_for_voltage(self._voltage)

    def cry(self) -> str:
        return "Bzzzzzz" if self._voltage > 0 else "..."

    def _compute_base_speed_for_voltage(self, voltage) -> float:
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
