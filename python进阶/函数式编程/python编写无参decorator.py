# !user/bin/python

from functools import reduce
import time


def log(f):
    def fn(x):
        print ('call ' + f.__name__ + '()...')
        return f(x)
    return fn


@log
def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))


print(factorial(10))


def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print('call %s() in %fs' % (f.__name__, (t2 - t1)))
        return print(t2)
    return fn


@performance
def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))


print(factorial(10))