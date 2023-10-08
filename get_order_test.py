#Шамсиева Ирина когорта- 8а Финальный проект. Инженер по тестированию плюс

import create_order

def positive_test(number_order):
    order_response = create_order.get_number_order(number_order)
    assert order_response.status_code == 200


def test_get_order():
    positive_test(create_order.number_order)