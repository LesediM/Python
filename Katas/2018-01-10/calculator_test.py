import unittest
from calculator import StringCalculator, NegativeNumberException


class StringCalculatorTest(unittest.TestCase):
    def test_that_emptystring_should_return_zero(self):
        string_calculator = StringCalculator()
        result = string_calculator.add("")
        self.assertEqual(0, result)

    def test_that_string_with_single_number_should_return_number(self):
        string_calculator = StringCalculator()
        result = string_calculator.add("32")
        self.assertEqual(32, result)

    def test_that_string_with_two_numbers_should_return_sum(self):
        string_calculator = StringCalculator()
        result = string_calculator.add("3,2")
        self.assertEqual(5, result)

    def test_that_string_with_three_numbers_should_return_sum(self):
        string_calculator = StringCalculator()
        result = string_calculator.add("1,3,2")
        self.assertEqual(6, result)

    def test_that_string_with_newline_character_should_return_sum(self):
        string_calculator = StringCalculator()
        result = string_calculator.add("1\n3,2")
        self.assertEqual(6, result)

    def test_that_string_with_newdelimiter_should_return_sum(self):
        string_calculator = StringCalculator()
        result = string_calculator.add("//;\n1;2")
        self.assertEqual(3, result)

    def test_that_string_with_negative_should_throw_exception(self):
        string_calculator = StringCalculator()
        with self.assertRaises(NegativeNumberException) as error:
            string_calculator.add("1,-2")
        self.assertEqual(error.exception.error_message,
                         "negatives not allowed: -2")

    def test_that_string_with_many_negative_should_throw_exception(self):
        string_calculator = StringCalculator()
        with self.assertRaises(NegativeNumberException) as error:
            string_calculator.add("1,-2,-3")
        self.assertEqual(error.exception.error_message,
                         "negatives not allowed: -2,-3")

    def test_that_string_with_numbers_above_1000_should_ignore_them_in_sum(self):
        string_calculator = StringCalculator()
        result = string_calculator.add("1,1000,3")
        self.assertEqual(4, result)

    def test_that_string_with_long_delimiter_should_return_sum(self):
        string_calculator = StringCalculator()
        result = string_calculator.add("//[***]\n1***2***3")
        self.assertEqual(6, result)

    def test_that_string_with_multiple_delimiters_should_return_sum(self):
        string_calculator = StringCalculator()
        result = string_calculator.add("//[*][%]\n1*2%3")
        self.assertEqual(6, result)

    def test_that_string_with_random_sized_delimiters_should_return_sum(self):
        string_calculator = StringCalculator()
        result = string_calculator.add("//[***][%]\n1***2%3")
        self.assertEqual(6, result)


if __name__ == "__main__":
    unittest.main()
