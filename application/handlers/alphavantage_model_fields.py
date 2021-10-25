from application.handlers import url_handler


class ModelFieldsHandler():
    def __init__(self, url):
        self.url = url

    def fill_model_fields(self):
        try:
            row_data = url_handler(self.url)
            data = row_data.json()
            model_fields = dict()
            realtime_data = data["Realtime Currency Exchange Rate"]

            model_fields['from_currency'] = realtime_data["1. From_Currency Code"]
            model_fields['to_currency'] = realtime_data["3. To_Currency Code"]
            model_fields['bid_price'] = realtime_data["9. Ask Price"]
            model_fields['ask_price'] = realtime_data["8. Bid Price"]
            model_fields['exchange_rate'] = realtime_data["5. Exchange Rate"]
            return model_fields
        except Exception as err:
            return err
