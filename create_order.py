import configuration
import requests
import data

def create_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body,
                         headers=data.headers)
response = create_new_order(data.order_body)
number_order = response.json()["track"]

def get_number_order(number_order):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH, params={"t": number_order})
