from datetime import datetime


def get_next_friday():
    today = datetime.now()
    while today.weekday() != 4:
        today = today.replace(day=today.day + 1)
    return today

def get_second_friday():
    day = get_next_friday()
    return get_next_week(day)

def get_next_week(day):
    return day.replace(day=day.day + 7)

def get_next_bi_week(day):
    return day.replace(day=day.day + 14)