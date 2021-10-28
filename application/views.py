from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from CurrencyExchange.settings import DOMAIN
from application.models import Currency
from application.serializers import CurrencySerializer
from application.tasks import get_exchange_rate_task


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        currency = get_exchange_rate_task.delay(DOMAIN)
        return Response(currency.get())
