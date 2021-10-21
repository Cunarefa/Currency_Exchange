import requests
from celery import shared_task
from rest_framework.response import Response

from CurrencyExchange.settings import url
from application.models import Currency


@shared_task(name="create_record_task")
def create_record_task(url):
    data = requests.get(url).json()
    Currency.objects.create(
        from_currency=data["Realtime Currency Exchange Rate"]["1. From_Currency Code"],
        to_currency=data["Realtime Currency Exchange Rate"]["3. To_Currency Code"],
        bid_price=data["Realtime Currency Exchange Rate"]["9. Ask Price"],
        ask_price=data["Realtime Currency Exchange Rate"]["8. Bid Price"],
        exchange_rate=data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    )
    Response(status=201)
