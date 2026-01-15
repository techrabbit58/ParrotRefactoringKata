from ..abstractparrot import Parrot


class EuropeanParrot(Parrot):

    def speed(self) -> float:
        return self.BASE_SPEED

    def cry(self) -> str:
        return "Sqoork!"
