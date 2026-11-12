import pytest
from orders import OrderError, calculate_order, order_status


def test_local_order():
    assert calculate_order({"rice": 2}) == {
        "subtotal": 2400,
        "discount": 0,
        "delivery": 500,
        "total": 2900,
    }


def test_remote_order():
    assert calculate_order({"beans": 1}, zone="remote")["total"] == 2400


def test_free_local_delivery():
    assert calculate_order({"chicken": 2})["delivery"] == 0


def test_coupon():
    assert calculate_order({"rice": 2}, coupon="SAVE10")["total"] == 2660


@pytest.mark.parametrize(
    "items",
    [{}, [], {"unknown": 1}, {"rice": 0}, {"rice": -2}, {"rice": 1.5}, {"rice": True}],
)
def test_invalid_items(items):
    with pytest.raises(OrderError):
        calculate_order(items)


def test_invalid_zone():
    with pytest.raises(OrderError):
        calculate_order({"rice": 1}, zone="international")


def test_invalid_coupon():
    with pytest.raises(OrderError):
        calculate_order({"rice": 1}, coupon="INVALID")


@pytest.mark.parametrize(
    "paid, inventory_ready, expected",
    [
        (False, False, "awaiting_payment"),
        (True, False, "awaiting_stock"),
        (True, True, "ready_for_dispatch"),
    ],
)
def test_order_status(paid, inventory_ready, expected):
    assert order_status(paid, inventory_ready) == expected
