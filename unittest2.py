#!/bin/python
# Unittest

import unittest
# .... other imports, script code, etc ...

class FactorialTests(unittest.TestCase):
    def testSingleValue(self):
        self.assertEqual(factorial(5), 120)
    def testMultipleValues(self):
        self.assertRaises(TypeError, factorial, [1,2,3,4])
    def testBoolean(self):
        self.assertRaises(factorial(5) == 120)
def main():
    """ Main function for this script """
    unittest.main() #checks functioon docs for more verbosity level

    if __name__ == "__main__":
        main()

import unittest
print(dir(unittest.TestCase))