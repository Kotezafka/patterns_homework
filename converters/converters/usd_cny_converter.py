from converters.currency_converter import CurrencyConverter
from converters.exchange_service import ExchangeRateService


class UsdCnyConverter(CurrencyConverter):
    def __init__(self, exchange_service: ExchangeRateService):
        self._exchange_service = exchange_service
        self._rates = None

    @property
    def target_currency(self) -> str:
        return "CNY"

    @property
    def rates(self):
        if self._rates is None:
            self._rates = self._exchange_service.get_rates()
        return self._rates

    def convert(self, amount: int) -> float:
        if not self.rates:
            raise ValueError("Failed to get CNY exchange rates")
        return amount * self.rates[self.target_currency]
