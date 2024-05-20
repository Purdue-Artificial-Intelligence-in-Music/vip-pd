# Modified from https://docs.python.org/3/library/unittest.html

import unittest

class TestStringMethods(unittest.TestCase):       # Your testing class MUST extend unittest.TestCase to be test-able

    def test_upper(self):                         # All test methods must start with test_XXXXXX
        self.assertEqual('foo'.upper(), 'FOO')    # self.assertEqual(X, Y) fails the test if X doesn't equal Y

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())          # self.assertTrue(X) fails the test if X isn't True
        self.assertFalse('Foo'.isupper())         # self.assertFalse(X) fails the test if X isn't False
        
    def test_bad(self):                           # This test should fail
        self.assertTrue(1 == 2)

if __name__ == '__main__':                        # You need this last bit of code to run the test from the VSCode "play" button or the command line
    unittest.main()