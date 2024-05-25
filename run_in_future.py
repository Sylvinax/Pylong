from concurrent import futures
import functools
import queue
import threading
import time


executor = futures.ThreadPoolExecutor(max_workers=100000)


def run_in_future(func):

    def decorate(*args, **kwargs):
        print(func.__name__)

        future = executor.submit(func, *args, **kwargs)

        return future

    return decorate


@run_in_future
def test1(value):
    print(threading.get_ident())
    time.sleep(5)
    print(value)


@run_in_future
def test2(value):
    print(threading.get_ident())
    time.sleep(5)
    print(value)


@run_in_future
def test3(value):
    print(threading.get_ident())
    time.sleep(5)
    print(value)


for i in range(100):
    x=test1(1)
    z=test1(2)
