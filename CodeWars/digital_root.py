def digital_root(n):
    number_to_string = str(n)
    if len(number_to_string) == 1:
        return n
    summation = 0
    for index in range(0, len(number_to_string)):
        summation += int(number_to_string[index])
    return digital_root(summation)


def digital_root_two(n):
    return n if n < 10 else digital_root(sum([int(c) for c in str(n)]))


def digital_root_three(n):
    return n % 9 or n and 9


import datetime as dt

import pytz


def get_now():
    return dt.datetime.now(dt.timezone.utc)


day1 = "2022-03-28 00:00:00"
date_time_obj = dt.datetime.fromisoformat(day1)
day2 = today = get_now()


def get_number_of_weeks(d1, d2):
    monday1 = d1 - dt.timedelta(days=d1.weekday())
    monday2 = d2 - dt.timedelta(days=d2.weekday())

    print(
        "Weeks:",
        (monday2.tz_convert(tz=pytz.UTC) - monday1.tz_localize(tz=pytz.UTC)).days / 7,
    )


get_number_of_weeks(date_time_obj, day2)
