from abc import ABC, abstractmethod

class CurrencyConverter(ABC):
    @abstractmethod
    def convert_usd_to(self, amount, type_currency):
        pass
