import requests
import json
from config import TOKEN_CURRENCY, keys


class APIException(Exception):
    pass


class Exchanger:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        symbols = Exchanger.get_symbols()
        if quote in keys:
            quote = keys[quote]
        if base in keys:
            base = keys[base]
        quote = quote.upper()
        base = base.upper()
        if quote not in symbols:
            raise APIException(f'Не удалось обработать валюту {quote}')
        if base not in symbols:
            raise APIException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except KeyError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key={TOKEN_CURRENCY}&symbols={quote},{base}&format=1')
        if 'error' in json.loads(r.content):
            raise Exception(f'Не удалось получить даннные валют!')
        exchange_in_quote = json.loads(r.content)['rates'][quote]
        exchange_in_base = json.loads(r.content)['rates'][base]
        price = round((exchange_in_base * amount) / exchange_in_quote, 4)
        return [price, quote, base]

    @staticmethod
    def get_symbols():
        r = requests.get(f'http://api.exchangeratesapi.io/v1/symbols?access_key={TOKEN_CURRENCY}')
        if 'error' in json.loads(r.content):
            raise Exception(f'Не удалось получить даннные валют!')
        symbols = json.loads(r.content)['symbols']
        return symbols

    @staticmethod
    def get_text_help():
        return 'Для перевода валют необходимо ввести две валюты и количество, например:\n*USD EUR 10*\n\
Для просмотра списка доступных валют введите команду: /values'
