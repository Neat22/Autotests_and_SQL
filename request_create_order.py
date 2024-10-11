# Лебедева Анна, 22А когорта - Финальный проект. Инженер по тестированию плюс.
from http.client import (responses)
import configuration
import data
import requests


# Создание заказа
def post_new_orders(body):
    return requests.post(configuration.URL_SERVICE + configuration.ORDERS,
                         json=body)

def get_order(track):
    url = "/v1/orders/track?t=" + str(track)
    return requests.get(configuration.URL_SERVICE + url)



response = post_new_orders(data.zakaz_body)
track = response.json()["track"]
print(track)
get_order_response = get_order(track)
print(get_order_response.status_code)
assert get_order_response.status_code == 200
