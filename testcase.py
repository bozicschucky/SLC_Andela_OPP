import unittest

class Mytest(unittest.test):
    """ return the unit test of the methods defined in the oopcase class"""

    def test_isMammal(self):
        self.assertEqual(isCow('cow'),'True')




unittest.main()