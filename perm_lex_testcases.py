import unittest
from perm_lex import *

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
        self.assertEqual(perm_gen_lex('ab'),['ab','ba'])

    def test_perm_02(self):
        self.assertEqual(perm_gen_lex('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

    def test_perm_03(self):
        self.assertEqual(perm_gen_lex('a'), ['a'])

if __name__ == "__main__":
        unittest.main()
