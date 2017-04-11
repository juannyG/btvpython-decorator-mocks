import time

from functools import wraps

'''
Helpful links and other examples:

https://pythonconquerstheuniverse.wordpress.com/2009/08/06/introduction-to-python-decorators-part-1/
http://chase-seibert.github.io/blog/2013/12/17/python-decorator-optional-parameter.html
'''

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

@ex_dec
def ex2():
    print 'Example 2 function'
    return True
