import calculator
import unittest

class Test(unittest.TestCase):

    def test_summa(self):
        self.assertEqual(calculator.calc1(7, 1, '+'), 8)

    def test_diff(self):
        self.assertEqual(calculator.calc2(10, 3, '-'), 7)

    def test_umn(self):
        self.assertEqual(calculator.calc3(6, 7, '*'), 42)

    def test_del(self):
        self.assertEqual(calculator.calc4(33, 3, '/'), 11)



if __name__ == '__main__':
    unittest.main()