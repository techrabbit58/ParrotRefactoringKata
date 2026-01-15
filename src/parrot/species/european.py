from ..abstractparrot import Parrot


class EuropeanParrot(Parrot):

    def speed(self) -> float:
        return self._base_speed()

    def cry(self) -> str:
        return "Sqoork!"
