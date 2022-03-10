import time as tm
from time import time


def measure_time(func):
    def wrapper(*args, **kwargs):

        start = time()
        result = func(*args, **kwargs)
        print(f"Elapsed time is {time() - start} ms")
        return result

    return wrapper


@measure_time
def sleeping_func(sleep_time):
    tm.sleep(sleep_time)


sleeping_func(0.5)
sleeping_func(1)
sleeping_func(1.5)
sleeping_func(2)


def logger(func):
    from datetime import datetime

    def wrapper(*args, **kwargs):
        print("_" * 25)
        print(f'Run on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(func.__name__)
        func(*args, **kwargs)
        print("_" * 25)

    return wrapper


@logger
def shutdown():
    print("System shutdown")


@logger
def restart():
    print("System restarts")


shutdown()
restart()
