from abc import ABC, abstractmethod


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
