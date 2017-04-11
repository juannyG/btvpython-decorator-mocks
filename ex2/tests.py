import unittest

from ex2.example import ex2

"""
To run tests, inside the btvpython-decorator-mocks directory, run the command

    python -m unittest ex2.tests
"""


class Ex2UnitTests(unittest.TestCase):
    def test_ex2_method_returns_true(self):
        result = ex2()
        self.assertTrue(result)
