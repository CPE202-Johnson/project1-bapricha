import unittest
from base_convert import *


class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45, 2), "101101")

    def test_base2_02(self):
        self.assertEqual(convert(44, 2), '101100')

    def test_base_03(self):
        self.assertEqual(convert(1, 2), '1')

    def test_base2_04(self):
        self.assertEqual(convert(0, 2), '0')

    def test_base4(self):
        self.assertEqual(convert(30, 4), "132")

    def test_base4_02(self):
        self.assertEqual(convert(11, 4), '23')

    def test_base4_03(self):
        self.assertEqual(convert(3, 4), '3')

    def test_base4_04(self):
        self.assertEqual(convert(0, 4), '0')

    def test_base16(self):
        self.assertEqual(convert(316, 16), "13C")

    def test_base16_02(self):
        self.assertEqual(convert(10, 16), 'A')

    def test_base16_03(self):
        self.assertEqual(convert(0, 16), '0')

    def test_base16_04(self):
        self.assertEqual(convert(11259375, 16), 'ABCDEF')

    def test_base10_01(self):
        self.assertEqual(convert(12, 10), '12')


if __name__ == "__main__":
    unittest.main()
