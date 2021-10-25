import json

from celery import shared_task
from rest_framework import status
from rest_framework.response import Response

from application.handlers.alphavantage_model_fields import ModelFieldsHandler
from application.models import Currency
from application.serializers import CurrencySerializer


@shared_task(name="create_record_task")
def create_record_task(url):
    try:
        model_fields = ModelFieldsHandler(url).fill_model_fields()
        serializer = CurrencySerializer(data=model_fields)
        if serializer.is_valid():
            s = Currency(**model_fields)
            s.save()
            return {'exchange_record': json.dumps(model_fields), 'status': status.HTTP_201_CREATED}
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        return {'message': err}
