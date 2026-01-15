from enum import Enum

from .abstractparrot import Parrot
from .species.african import AfricanParrot
from .species.european import EuropeanParrot
from .species.norwegian import NorwegianBlue


class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


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
