import unittest

class CalcTest(unittest.TestCase):
    def test_input_text(self, expected_result=11, actual_result=11):
        assert expected_result == actual_result, \
            f"expected  {expected_result} got  {actual_result}"

if __name__ == '__main__':
    unittest.main()