from ..abstractparrot import Parrot


class AfricanParrot(Parrot):
    def __init__(self, number_of_coconuts: float) -> None:
        self._number_of_coconuts = number_of_coconuts

    def speed(self) -> float:
        return max(0., self._base_speed() - self._load_factor() * self._number_of_coconuts)

    def cry(self) -> str:
        return "Sqaark!"
