import json

import requests
from rest_framework import status
from rest_framework.response import Response

from application.models import Currency
from application.serializers import CurrencySerializer


class ModelFieldsHandler:
    def __init__(self, full_url):
        self.serializer = CurrencySerializer
        self.full_url = full_url

    def fill_model_fields(self):
        try:
            data = requests.get(self.full_url).json()
            model_fields = dict()
            realtime_data = data["Realtime Currency Exchange Rate"]

            model_fields['from_currency'] = realtime_data["1. From_Currency Code"]
            model_fields['to_currency'] = realtime_data["3. To_Currency Code"]
            model_fields['bid_price'] = realtime_data["8. Bid Price"]
            model_fields['ask_price'] = realtime_data["9. Ask Price"]
            model_fields['exchange_rate'] = realtime_data["5. Exchange Rate"]
            serializer = self.serializer(data=model_fields)
            if serializer.is_valid():
                record = Currency(**model_fields)
                record.save()
                return {'exchange_record': json.dumps(model_fields), 'status': status.HTTP_201_CREATED}
            else:
                return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return 'Wrong currency codes or your API Key is invalid or has expired.'
        except AttributeError:
            return 'Invalid domain.'
