import logging
from calendar import monthrange
from datetime import datetime, date, timedelta

def get_weeks_before_date(start_date: date, num_weeks: int) -> date:
    return start_date - timedelta(weeks=num_weeks)

def get_weeks_after_date(start_date: date, num_weeks: int) -> date:
    return start_date + timedelta(weeks=num_weeks)

def get_next_friday_from_now() -> date:
    today = date.today()
    while today.weekday() != 4:
        today = today.replace(day=today.day + 1)
    return today

def get_second_friday_from_now() -> date:
    day: date = get_next_friday_from_now()
    return get_next_week(day)

def get_tomorrow(day: date) -> date:
    tomorrow: date = day + timedelta(days=1)
    return tomorrow

def get_next_week(starting_date: date) -> date:
    next_week_date = starting_date + timedelta(days=7)
    return next_week_date

def get_next_bi_week(starting_date: date) -> date:
    next_bi_week_date: date = starting_date + timedelta(days=14)
    return next_bi_week_date

def get_next_month(starting_date: date) -> date:
    next_month: int = starting_date.month + 1
    year: int = starting_date.year
    if next_month > 12:
        next_month = 1
        year += 1
    valid_day: int = min(get_days_in_month(next_month, year),
                         starting_date.day)
    return date(year, next_month, valid_day)

def get_days_in_month(month: int, year: int) -> int:
    return monthrange(year, month)[1]

def get_next_bi_month(starting_date: date) -> date:
    next_month: int = starting_date.month + 1
    year: int = starting_date.year
    if next_month > 12:
        next_month = 2
        year += 1
    valid_day: int = min(get_days_in_month(next_month, year),
                         starting_date.day)
    return date(year, next_month, valid_day)

def get_next_year(starting_date: date) -> date:
    return starting_date.replace(year=starting_date.year + 1)

def iso_to_django_date(iso_date: str) -> date:
    normalized_iso_date: str = iso_date.replace("Z", "")
    return datetime.fromisoformat(normalized_iso_date).date()