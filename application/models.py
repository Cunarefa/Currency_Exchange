from django.db import models


class Currency(models.Model):
    from_currency = models.CharField(max_length=5)
    to_currency = models.CharField(max_length=5)
    bid_price = models.FloatField()
    ask_price = models.FloatField()
    exchange_rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.bid_price} / {self.ask_price} at {self.created_at.strftime('%H:%M')}"
