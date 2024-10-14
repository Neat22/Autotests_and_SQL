# Лебедева Анна, 22А когорта - Финальный проект. Инженер по тестированию плюс.
import data
import configuration
import requests
from request_create_order import post_new_orders
from request_create_order import get_order

def test_ordering_by_track():
    response = post_new_orders(data.zakaz_body)
    track = response.json()["track"]
    get_order_response = get_order(track)

    assert get_order_response.status_code == 200