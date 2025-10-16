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


import re

def normalize_phone(phone_number):
    cleaned = re.sub(r"[^\d+]", "", phone_number.strip())
    if cleaned.startswith("+"):
        return cleaned
    elif cleaned.startswith("380"):
        return "+" + cleaned
    else:
        return "+38" + cleaned
    
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    result = []
    for user in users:
        try:
            bdate = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        except ValueError:
            continue
        
        birthday_this_year = bdate.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_diff = (birthday_this_year - today).days
        if 0 <= days_diff <= 7:
            congratulation_date = birthday_this_year
        
            wd = congratulation_date.weekday()
            if wd == 5:
                congratulation_date += timedelta(days=2)
            elif wd == 6:
                congratulation_date += timedelta(days=1)

            result.append({
                "name": user.get("name", ""),
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return result

users = [
    {"name": "John Doe", "birthday": "1985.10.17"},
    {"name": "Jane Smith", "birthday": "1990.10.18"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

