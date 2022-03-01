from abc import ABC, abstractmethod


class Donations(ABC):

    @abstractmethod
    def get_value_in_dollars() -> float:
        pass
