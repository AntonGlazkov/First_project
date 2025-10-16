from datetime import datetime

def get_days_from_today(date):
    datetime_object = datetime.strptime(date, "%Y-%m-%d").date()
    today = datetime.today().date()
    delta = today - datetime_object
    return delta.days

print(get_days_from_today("2021-10-10"))