import unittest
import re   
   
class CalcTest(unittest.TestCase):
    def test_substring(self, full_string="some_value", substring="print"):
        assert re.search(substring, full_string), \
            f"expected '{substring}' to be substring of '{full_string}'"
if __name__ == '__main__':
    unittest.main()
