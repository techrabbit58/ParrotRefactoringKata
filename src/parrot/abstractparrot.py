from abc import ABC, abstractmethod


class Parrot(ABC):
    LOAD_FACTOR = 9.0
    BASE_SPEED = 12.0

    @abstractmethod
    def speed(self) -> str: pass

    @abstractmethod
    def cry(self) -> str: pass
