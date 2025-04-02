from abc import ABC, abstractmethod


class CurrencyConverter(ABC):
    @property
    @abstractmethod
    def target_currency(self) -> str:
        pass

    @abstractmethod
    def convert(self, amount: int) -> float:
        pass
