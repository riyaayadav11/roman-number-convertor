import unittest

from roman_converter import convert, int_to_roman, roman_to_int, main


class TestIntToRoman(unittest.TestCase):
    def test_known_values(self):
        cases = {
            1: "I",
            4: "IV",
            9: "IX",
            14: "XIV",
            40: "XL",
            90: "XC",
            400: "CD",
            1994: "MCMXCIV",
            2024: "MMXXIV",
            3999: "MMMCMXCIX",
        }
        for number, expected in cases.items():
            with self.subTest(number=number):
                self.assertEqual(int_to_roman(number), expected)

    def test_out_of_range(self):
        for bad in (0, -5, 4000):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    int_to_roman(bad)

    def test_wrong_type(self):
        for bad in ("5", 3.5, None, True):
            with self.subTest(bad=bad):
                with self.assertRaises(TypeError):
                    int_to_roman(bad)


class TestRomanToInt(unittest.TestCase):
    def test_known_values(self):
        cases = {"I": 1, "IV": 4, "IX": 9, "LVIII": 58, "MCMXCIV": 1994, "MMMCMXCIX": 3999}
        for roman, expected in cases.items():
            with self.subTest(roman=roman):
                self.assertEqual(roman_to_int(roman), expected)

    def test_case_and_whitespace_insensitive(self):
        self.assertEqual(roman_to_int("  mcmxciv "), 1994)

    def test_invalid_numerals(self):
        for bad in ("", "   ", "IIII", "VX", "IC", "MMMM", "ABC", "IVI"):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    roman_to_int(bad)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            roman_to_int(10)


class TestRoundTrip(unittest.TestCase):
    def test_every_value(self):
        for number in range(1, 4000):
            self.assertEqual(roman_to_int(int_to_roman(number)), number)


class TestConvertAndCli(unittest.TestCase):
    def test_convert_detects_direction(self):
        self.assertEqual(convert("2024"), "MMXXIV")
        self.assertEqual(convert("MMXXIV"), "2024")

    def test_main_success_and_failure(self):
        self.assertEqual(main(["1994"]), 0)
        self.assertEqual(main(["IIII"]), 1)
        self.assertEqual(main(["0"]), 1)


if __name__ == "__main__":
    unittest.main()
