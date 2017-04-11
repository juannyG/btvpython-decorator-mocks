from functools import wraps

'''
Helpful links and other examples:

https://pythonconquerstheuniverse.wordpress.com/2009/08/06/introduction-to-python-decorators-part-1/
http://chase-seibert.github.io/blog/2013/12/17/python-decorator-optional-parameter.html
'''

def ex_dec(fn):
    print "Hello from ex_dec!"

    @wraps(fn)
    def wrapped(*args, **kwargs):
        print "Decorator called"
        return fn(*args, **kwargs)
    return wrapped

@ex_dec
def hello_world():
    print 'HELLO WORLD!'
