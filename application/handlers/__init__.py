import requests


def url_handler(url):
    try:
        data = requests.get(url)
        return data
    except Exception as err:
        return err


DEFAULT_VALUES = dict(from_currency='BTC', to_currency='USD')
