import re


def timeConversion(s):
    timeSplit = s.split(":")
    hour = timeSplit[0]
    minutes = timeSplit[1]
    seconds = timeSplit[2][:2]
    day_time = timeSplit[2][2:]
    if day_time == "AM":
        if hour == "12":
            hour = "00"
    else:
        if hour != "12":
            hour = str(int(hour) + 12)

    return f"{hour}:{minutes}:{seconds}"


print(timeConversion("00:05:45AM"))
