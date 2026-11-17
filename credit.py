MIN_AGE = 18


def calculate_risk(income, debt, age):
    if income <= 0 or age < MIN_AGE:
        return -1

    ratio = debt / income

    if ratio > 0.6:
        return "HIGH"
    if ratio > 0.3:
        return "MEDIUM"
    return "LOW"
