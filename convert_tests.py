import unittest
from convert import str_to_float

#Task 1
class TestStrToFloat(unittest.TestCase):

    def test_valid_float(self):
        self.assertEqual(str_to_float("3.14"), 3.14)
        self.assertEqual(str_to_float("-2.718"), -2.718)

    def test_integer_string(self):
        self.assertEqual(str_to_float("42"), 42.0)

    def test_invalid_string(self):
        self.assertIsNone(str_to_float("abc"))
        self.assertIsNone(str_to_float("123abc"))
        self.assertIsNone(str_to_float(""))

    def test_special_floats(self):
        self.assertEqual(str_to_float("inf"), float("inf"))
        self.assertEqual(str_to_float("-inf"), float("-inf"))
        self.assertEqual(str_to_float("nan"), float("nan"))


if __name__ == "__main__":
    unittest.main()

