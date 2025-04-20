import logging
from calendar import monthrange
from datetime import datetime, date, timedelta

#----------------------------Get-Weeks-Before-Date----------------------------
def get_weeks_before_date(start_date: date, num_weeks: int) -> date:
    return start_date - timedelta(weeks=num_weeks)

#----------------------------Get-Weeks-After-Date-----------------------------
def get_weeks_after_date(start_date: date, num_weeks: int) -> date:
    return start_date + timedelta(weeks=num_weeks)

#---------------------------Get-Bi-Weeks-After-Date---------------------------
def get_bi_weeks_after_date(start_date: date, num_bi_weeks: int) -> date:
    return start_date + timedelta(weeks=num_bi_weeks * 2)

#--------------------------Get-Bi-Weeks-Before-Date---------------------------
def get_bi_weeks_before_date(start_date: date, num_bi_weeks: int) -> date:
    return start_date - timedelta(weeks=num_bi_weeks * 2)

#----------------------------Get-Months-After-Date----------------------------
def get_months_after_date(start_date: date, num_months: int) -> date:
    year: int = start_date.year
    month: int = start_date.month + num_months
    if month > 12:
        month = month % 12
        year += month // 12
    valid_day: int = min(get_days_in_month(month, year), start_date.day)
    return date(year, month, valid_day)
#-------------------------Get-Num-Weeks-Between-Dates-------------------------
def get_num_weeks_between_dates(start_date: date, end_date: date) -> int:
    return abs((end_date - start_date).days) // 7

#-----------------------Get-Num-Bi-Weeks-Between-Dates------------------------
def get_num_bi_weeks_between_dates(start_date: date, end_date: date) -> int:
    return abs((end_date - start_date).days) // 14

# ------------------------Get-Num-Months-Between-Dates-------------------------
def get_num_months_between_dates(start_date: date, end_date: date) -> int:
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    num_months = end_date.month - start_date.month
    if start_date.year == end_date.year:
        if end_date.day < start_date.day:
            num_months -= 1
        return num_months
    else:
        num_years: int = end_date.year - start_date.year
        months_difference = num_years * 12 + num_months
        if end_date.day < start_date.day:
            months_difference -= 1
        return months_difference
#--------------------------Get-Next-Friday-From-Now---------------------------
def get_next_friday_from_now() -> date:
    today = date.today()
    while today.weekday() != 4:
        today = today.replace(day=today.day + 1)
    return today

#-------------------------Get-Second-Friday-From-Now--------------------------
def get_second_friday_from_now() -> date:
    day: date = get_next_friday_from_now()
    return get_next_week(day)

#--------------------------------Get-Tomorrow---------------------------------
def get_tomorrow(day: date) -> date:
    tomorrow: date = day + timedelta(days=1)
    return tomorrow

#--------------------------------Get-Next-Week--------------------------------
def get_next_week(starting_date: date) -> date:
    next_week_date = starting_date + timedelta(days=7)
    return next_week_date

#------------------------------Get-Next-Bi-Week-------------------------------
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

#-------------------------------Get-Next-Month--------------------------------
def get_days_in_month(month: int, year: int) -> int:
    return monthrange(year, month)[1]

#------------------------------Get-Next-Bi-Month------------------------------
def get_next_bi_month(starting_date: date) -> date:
    next_month: int = starting_date.month + 1
    year: int = starting_date.year
    if next_month > 12:
        next_month = 2
        year += 1
    valid_day: int = min(get_days_in_month(next_month, year),
                         starting_date.day)
    return date(year, next_month, valid_day)

#--------------------------------Get-Next-Year--------------------------------
def get_next_year(starting_date: date) -> date:
    return starting_date.replace(year=starting_date.year + 1)

#-----------------------------Iso-To-Django-Date------------------------------
def iso_to_django_date(iso_date: str) -> date:
    normalized_iso_date: str = iso_date.replace("Z", "")
    return datetime.fromisoformat(normalized_iso_date).date()