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


def log(descriptor):
    # Implement the decorator here
    def decorator(function):
        def wrapper(*args, **kwargs):
            digits = ",".join(map(str, args))
            msg = "LOG: " + function.__name__ + "(" + digits + ")\n"
            print(msg)
            descriptor.write(msg)
            result = function(*args, **kwargs)
            return result

        return wrapper

    return decorator


def lambdaMap(arr):
    ans = map(
        lambda x: list(map(lambda z: z ** 2, list(filter(lambda y: y > 0, x))))
        # Complete the lambda function below.  It begins in the non-alterable code above
        ,
        arr,
    )


shutdown()
restart()
