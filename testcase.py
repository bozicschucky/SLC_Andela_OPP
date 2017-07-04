import unittest
import oopcase

class Mytest(unittest.TestCase):
    """ return the unit test of the methods defined in the oopcase class"""

    def test_call(self):
        p=oopcase.phone()
        self.assertEqual(p.call(123),'calling the number !123')
