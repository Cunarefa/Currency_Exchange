from celery import shared_task

from application.handlers.alphavantage_model_fields import ModelFieldsHandler
from application.handlers.alphavantage_url_creation import URLCreateHandler


@shared_task(name="get_exchange_rate_task")
def get_exchange_rate_task(domain):
    try:
        full_url = URLCreateHandler(domain).get_full_url()
        result = ModelFieldsHandler(full_url).fill_model_fields()
        return result
    except Exception as err:
        return err.args[0]
