from datetime import datetime

def get_days_from_today(date):
    datetime_object = datetime.strptime(date, "%Y-%m-%d").date()
    today = datetime.today().date()
    delta = today - datetime_object
    return delta.days

print(get_days_from_today("2021-10-10"))

import random

def get_numbers_ticket(min_value, max_value, quantity):
    if (
        (max_value - min_value + 1) < quantity
        or quantity <=0
        or min_value >= max_value
        or min_value < 1
        or max_value > 1000
        ):
        return []
    numbers = random.sample(range(min_value, max_value + 1), quantity)
    return sorted(numbers)

lottery_numbers = get_numbers_ticket(1, 1000, 8)
print("Ваші лотерейні числа:", lottery_numbers)
