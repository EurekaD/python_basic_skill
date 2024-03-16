import time
from functools import wraps, lru_cache


def timekeeping(func):
    @wraps(func)
    def wrappper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("代码块执行时间:", elapsed_time, "秒")
        return result

    return wrappper


@lru_cache
def factorial1(n):
    return n * factorial1(n-1) if n else 1


def factorial2(n):
    return n * factorial2(n-1) if n else 1


@timekeeping
def keep_time1(n):
    print(factorial1(n))


@timekeeping
def keep_time2(n):
    print(factorial2(n))


keep_time1(200)


