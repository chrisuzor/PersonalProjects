def make_readable(seconds):
    seconds_ = str(seconds % 60)
    hour = str(seconds // 3600)
    minutes = str((seconds - ((int(hour) * 3600) + int(seconds_))) // 60)
    seconds_ = "0" + seconds_ if len(seconds_) == 1 else seconds_
    hour = "0" + hour if len(hour) == 1 else hour
    minutes = "0" + minutes if len(minutes) == 1 else minutes

    return f"{hour}:{minutes}:{seconds_}"


def make_readable_(s):
    return "{:02}:{:02}:{:02}".format(s / 3600, s / 60 % 60, s % 60)


def make_readable__(seconds):
    hours, seconds = divmod(seconds, 60 ** 2)
    minutes, seconds = divmod(seconds, 60)
    return "{:02}:{:02}:{:02}".format(hours, minutes, seconds)


print(make_readable(0))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))
