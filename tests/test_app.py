import pytest
from app import add, classify_score, shipping_cost


def test_add():
    assert add(4, 6) == 10


@pytest.mark.parametrize(
    "score, expected",
    [(0, "fail"), (49, "fail"), (50, "pass"), (79, "pass"), (80, "excellent"), (100, "excellent")],
)
def test_score_categories(score, expected):
    assert classify_score(score) == expected


@pytest.mark.parametrize("score", [-1, 101])
def test_invalid_score(score):
    with pytest.raises(ValueError):
        classify_score(score)


@pytest.mark.parametrize(
    "total, priority, expected",
    [(50, False, 8), (100, False, 0), (50, True, 15)],
)
def test_shipping(total, priority, expected):
    assert shipping_cost(total, priority) == expected


def test_negative_order_total():
    with pytest.raises(ValueError):
        shipping_cost(-1, False)
