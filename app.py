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