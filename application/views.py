from rest_framework import viewsets, permissions

from application.models import Currency
from application.serializers import CurrencySerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [
        permissions.AllowAny
    ]


