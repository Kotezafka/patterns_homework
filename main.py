import asyncio
from converters import *


def main():
    amount = int(input('Введите значение в USD: \n'))
    
    converters = {
        'EUR': UsdEurConverter(),
        'GBP': UsdGbpConverter(),
        'RUB': UsdRubConverter(),
        'CNY': UsdCnyConverter(),
    }

    for type_currency, conv in converters.items():
        print(f"{amount} USD to {type_currency}: {conv.convert_usd_to(amount, type_currency)}")
    

if __name__ == "__main__":
    main()

