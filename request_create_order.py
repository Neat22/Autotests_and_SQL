
from http.client import (responses)
import configuration
import data
import requests


# Создание заказа
def post_new_orders(body):
    return requests.post(configuration.URL_SERVICE + configuration.ORDERS,
                         json=body)

def get_order(track):
    ORDERS_TRACK = "/v1/orders/track?t=" + str(track)
    return requests.get(configuration.URL_SERVICE + ORDERS_TRACK)




