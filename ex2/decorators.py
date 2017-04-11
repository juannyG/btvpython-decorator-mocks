import time

from functools import wraps


def really_annoying_fn():
    print "Doing some heavy duty processing..."
    time.sleep(3)

def ex_dec(fn, *args, **kwargs):
    print "Hello from ex_dec!"

    @wraps(fn)
    def wrapped(*args, **kwargs):
        really_annoying_fn()
        return fn(*args, **kwargs)
    return wrapped
