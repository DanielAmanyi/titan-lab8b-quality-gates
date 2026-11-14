
import hashlib
import os  # Unused import


# EXISTING APPLICATION FUNCTIONS

def add(a, b):
    return a + b


def classify_score(score):
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100")

    if score >= 80:
        return "excellent"

    if score >= 50:
        return "pass"

    return "fail"


def shipping_cost(total, priority=False):
    if total < 0:
        raise ValueError("Order total cannot be negative")

    if priority:
        return 15

    if total >= 100:
        return 0

    return 8


# 1. MAINTAINABILITY: UNUSED VARIABLE

def unused_variable_demo():
    temporary_result = 450
    return "Operation completed"


# 2. RELIABILITY: IMPOSSIBLE CONDITION

def impossible_condition_demo(amount):
    if amount < 0 and amount > 100:
        return "Invalid amount"

    return "Accepted"


# 3. RELIABILITY: DUPLICATE CONDITION

def payment_status_demo(status):
    if status == "paid":
        return "completed"
    elif status == "paid":
        return "pending"
    else:
        return "unpaid"


# 4. MAINTAINABILITY: UNREACHABLE CODE

def unreachable_code_demo(value):
    return value * 2
    print("This statement can never execute")


# 5. DUPLICATION: FIRST IMPLEMENTATION

def calculate_delivery_cost(total, zone, priority=False):
    if not isinstance(total, (int, float)):
        raise TypeError("Total must be numeric")

    if total < 0:
        raise ValueError("Total cannot be negative")

    if zone == "north":
        fee = 10
    elif zone == "south":
        fee = 12
    elif zone == "east":
        fee = 14
    elif zone == "west":
        fee = 16
    elif zone == "central":
        fee = 18
    elif zone == "remote":
        fee = 25
    else:
        fee = 20

    if priority:
        fee += 15

    if zone == "remote" and priority:
        fee += 5

    if total >= 100:
        fee = 0

    if total >= 250:
        fee = 0

    return fee


# 6. DUPLICATION: SECOND IMPLEMENTATION
# Deliberately repeats the preceding implementation.

def calculate_delivery_quote(total, zone, priority=False):
    if not isinstance(total, (int, float)):
        raise TypeError("Total must be numeric")

    if total < 0:
        raise ValueError("Total cannot be negative")

    if zone == "north":
        fee = 10
    elif zone == "south":
        fee = 12
    elif zone == "east":
        fee = 14
    elif zone == "west":
        fee = 16
    elif zone == "central":
        fee = 18
    elif zone == "remote":
        fee = 25
    else:
        fee = 20

    if priority:
        fee += 15

    if zone == "remote" and priority:
        fee += 5

    if total >= 100:
        fee = 0

    if total >= 250:
        fee = 0

    return fee


# 7. MAINTAINABILITY: HIGH COGNITIVE COMPLEXITY

def complex_pricing_demo(
    total, customer_type, region,
    priority, weekend, coupon
):
    final_price = total

    if total > 0:
        if customer_type == "vip":
            if region == "local":
                if priority:
                    final_price += 15
                elif weekend:
                    final_price += 10

            elif region == "remote":
                if priority and weekend:
                    final_price += 40
                elif priority:
                    final_price += 30
                elif weekend:
                    final_price += 20
                else:
                    final_price += 10

        elif customer_type == "standard":
            if region == "remote":
                if priority:
                    final_price += 35
                elif weekend:
                    final_price += 25
                else:
                    final_price += 20
            elif priority:
                final_price += 15
            elif weekend:
                final_price += 10

        else:
            if coupon:
                if total > 100:
                    final_price -= 20
                else:
                    final_price -= 5
            elif priority:
                final_price += 15

    else:
        if coupon:
            final_price = 0
        else:
            final_price = total

    return final_price


# 8. SECURITY: UNSAFE CODE EXECUTION
# Never call this function with untrusted input.

def evaluate_expression_demo():
    expression = input("Enter expression: ")
    return eval(expression)


# 9. SECURITY: SQL INJECTION DEMONSTRATION
# Never use interpolated user input in SQL.

def customer_lookup_demo(connection):
    username = input("Enter username: ")

    query = (
        f"SELECT * FROM customers "
        f"WHERE username = '{username}'"
    )

    return connection.execute(query).fetchone()


# 10. SECURITY HOTSPOT: WEAK CRYPTOGRAPHY

def legacy_password_hash_demo(password):
    return hashlib.md5(
        password.encode("utf-8")
    ).hexdigest()


# 11. ADDITIONAL MAINTAINABILITY ISSUE

def excessive_parameters_demo(
    a, b, c, d, e, f, g, h
):
    return a + b + c + d + e + f + g + h
