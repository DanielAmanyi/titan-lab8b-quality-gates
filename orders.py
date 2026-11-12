"""Minimal order-pricing service. All prices are integer naira amounts."""

CATALOG = {
    "rice": 1200,
    "beans": 900,
    "stew": 600,
    "chicken": 2500,
}
DELIVERY_FEES = {"local": 500, "remote": 1500}


class OrderError(ValueError):
    """Invalid order request."""


def calculate_order(items, zone="local", coupon=None):
    """Calculate a deterministic receipt with validation."""
    if not isinstance(items, dict) or not items:
        raise OrderError("Order must contain item quantities")
    if zone not in DELIVERY_FEES:
        raise OrderError("Unsupported delivery zone")

    subtotal = 0
    for product, quantity in items.items():
        if product not in CATALOG:
            raise OrderError(f"Unknown product: {product}")
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise OrderError("Quantity must be an integer")
        if quantity <= 0:
            raise OrderError("Quantity must be positive")
        subtotal += CATALOG[product] * quantity

    if coupon is None:
        discount = 0
    elif coupon == "SAVE10":
        discount = subtotal // 10
    else:
        raise OrderError("Invalid coupon")

    delivery = DELIVERY_FEES[zone]
    if zone == "local" and subtotal >= 5000:
        delivery = 0

    return {
        "subtotal": subtotal,
        "discount": discount,
        "delivery": delivery,
        "total": subtotal - discount + delivery,
    }


def order_status(paid, inventory_ready):
    if not paid:
        return "awaiting_payment"
    if not inventory_ready:
        return "awaiting_stock"
    return "ready_for_dispatch"

