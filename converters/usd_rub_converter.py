import requests
from converters import CurrencyConverter

class UsdRubConverter(CurrencyConverter):
    def __init__(self):
        self.rates = self.get_rates()

    def get_rates(self):
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        return data['rates']
    
    def convert_usd_to(self, amount, type_currency):
        if type_currency != 'RUB':
            print('This is not USD to RUB converter')
            return

        return amount * self.rates['RUB']
