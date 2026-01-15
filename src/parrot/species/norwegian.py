from ..abstractparrot import Parrot


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
