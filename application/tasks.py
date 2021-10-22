import json

import requests
from celery import shared_task
from rest_framework import status
from rest_framework.response import Response

from CurrencyExchange.settings import url
from application.models import Currency
from application.serializers import CurrencySerializer


@shared_task(name="create_record_task")
def create_record_task(url):
    data = requests.get(url).json()

    model_fields = dict()
    model_fields['from_currency'] = data["Realtime Currency Exchange Rate"]["1. From_Currency Code"]
    model_fields['to_currency'] = data["Realtime Currency Exchange Rate"]["3. To_Currency Code"]
    model_fields['bid_price'] = data["Realtime Currency Exchange Rate"]["9. Ask Price"]
    model_fields['ask_price'] = data["Realtime Currency Exchange Rate"]["8. Bid Price"]
    model_fields['exchange_rate'] = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]

    serializer = CurrencySerializer(data=model_fields)
    if serializer.is_valid():
        s = Currency(**model_fields)
        s.save()
        # return {'exchange_record': json.dumps(model_fields)}, Response(status.HTTP_201_CREATED)
        d = Response(status.HTTP_200_OK)
        return Response(status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
