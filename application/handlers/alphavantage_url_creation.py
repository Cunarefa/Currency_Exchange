import os
import requests
from dotenv import load_dotenv
from application.handlers import DEFAULT_VALUES

load_dotenv()


class URLCreateHandler:
    """ Class receive arguments for requesting URL from user. It also process and create requesting URL """

    def __init__(self, domain):
        self.__DOMAIN = domain
        self._function = 'CURRENCY_EXCHANGE_RATE'
        self.args_dict = dict(function=self._function)

    def get_full_url(self):
        args = self.get_args()
        url = self.create_url(args)
        return url

    def get_args(self):
        self.args_dict['from_currency'] = DEFAULT_VALUES['from_currency']
        self.args_dict['to_currency'] = DEFAULT_VALUES['to_currency']
        self.args_dict['apikey'] = os.getenv('API_KEY')
        return self.args_dict

    def create_url(self, args_dict):
        try:
            request = requests.get(self.__DOMAIN, params=args_dict)
            return request.url
        except ValueError as err:
            return err
        except Exception as err:
            return err



