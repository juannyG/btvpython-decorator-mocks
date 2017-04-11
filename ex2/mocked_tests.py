import unittest
import importlib
import mock

from functools import wraps

from ex2 import decorators as ex2_decorators

"""
To run tests, inside the btvpython-decorator-mocks directory, run the command

    python -m unittest ex2.mocked_tests
"""

def test_decorator(fn, *args, **kwargs):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """Pass through to the function we're interested in"""
        return fn(*args, **kwargs)
    return wrapper


class Ex2MockedDecoratorUnitTests(unittest.TestCase):

    def setUp(self):
        # Store and override the decorator
        self.original_decorator = ex2_decorators.ex_dec
        ex2_decorators.ex_dec = mock.Mock(side_effect=test_decorator)

        # Import the module with your function
        self.example_module = importlib.import_module('ex2.example')

    def tearDown(self):
        """Leave things how we found them..."""
        ex2_decorators.ex_dec = self.original_decorator

    def test_ex2_method_returns_true(self):
        result = self.example_module.ex2()
        self.assertTrue(result)
