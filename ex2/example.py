from ex2.decorators import ex_dec
'''
Helpful links and other examples:

https://pythonconquerstheuniverse.wordpress.com/2009/08/06/introduction-to-python-decorators-part-1/
http://chase-seibert.github.io/blog/2013/12/17/python-decorator-optional-parameter.html
'''

@ex_dec
def ex2():
    print 'Example 2 function'
    return True
