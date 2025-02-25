from datetime import datetime, date


def get_next_friday():
    today = datetime.now()
    while today.weekday() != 4:
        today = today.replace(day=today.day + 1)
    return today

def get_second_friday():
    day = get_next_friday()
    return get_next_week(day)

def get_tomorrow(day: date):
    return day.replace(day=day.day + 1)

def get_next_week(starting_date: date):
    return starting_date.replace(day=starting_date.day + 7)

def get_next_bi_week(starting_date: date):
    return starting_date.replace(day=starting_date.day + 14)

def get_next_month(starting_date: date):
    return starting_date.replace(month=starting_date.month + 1)

def get_next_bi_month(starting_date: date):
    return starting_date.replace(month=starting_date.month + 2)

def get_next_year(starting_date: date):
    return starting_date.replace(year=starting_date.year + 1)

def iso_to_django_date(iso_date: str) -> date:
    normalized_iso_date: str = iso_date.replace("Z", "")
    return datetime.fromisoformat(normalized_iso_date).date()