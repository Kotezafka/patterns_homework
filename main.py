from converters.exchange_service import ExchangeRateService
from converters.converters.usd_eur_converter import UsdEurConverter
from converters.converters.usd_gbp_converter import UsdGbpConverter
from converters.converters.usd_rub_converter import UsdRubConverter
from converters.converters.usd_cny_converter import UsdCnyConverter


def main():
    exchange_service = ExchangeRateService()

    converters = {
        "EUR": UsdEurConverter(exchange_service),
        "GBP": UsdGbpConverter(exchange_service),
        "RUB": UsdRubConverter(exchange_service),
        "CNY": UsdCnyConverter(exchange_service),
    }

    try:
        amount = int(input("Введите значение в USD: "))

        if amount < 0:
            print("Ошибка: введите целое положительное число")
            return

        for currency, converter in converters.items():
            result = converter.convert(amount)
            print(f"{amount} USD to {currency}: {result}")
    except ValueError:
        print("Ошибка: введите целое число")
    except Exception as e:
        print(f"Ошибка конвертации: {e}")


if __name__ == "__main__":
    main()
