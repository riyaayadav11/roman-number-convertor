"""Roman Numeral Converter.

Convert integers (1-3999) to Roman numerals and back, from Python code
or from the command line.

Usage:
    python roman_converter.py 1994        -> MCMXCIV
    python roman_converter.py MCMXCIV     -> 1994
    python roman_converter.py             -> interactive mode
"""

import argparse
import re
import sys

MIN_VALUE = 1
MAX_VALUE = 3999

# Value/symbol pairs from largest to smallest, including subtractive forms.
_NUMERALS = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]

_SYMBOL_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

# Matches only canonical (standard) Roman numerals, e.g. rejects "IIII" or "VX".
_VALID_ROMAN = re.compile(
    r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
)


def int_to_roman(number: int) -> str:
    """Convert an integer between 1 and 3999 to a Roman numeral string."""
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("number must be an integer")
    if not MIN_VALUE <= number <= MAX_VALUE:
        raise ValueError(f"number must be between {MIN_VALUE} and {MAX_VALUE}")

    result = []
    for value, symbol in _NUMERALS:
        count, number = divmod(number, value)
        result.append(symbol * count)
    return "".join(result)


def roman_to_int(roman: str) -> int:
    """Convert a valid Roman numeral string to an integer."""
    if not isinstance(roman, str):
        raise TypeError("roman must be a string")

    roman = roman.strip().upper()
    if not roman:
        raise ValueError("roman numeral cannot be empty")
    if not _VALID_ROMAN.match(roman):
        raise ValueError(f"invalid Roman numeral: {roman!r}")

    total = 0
    for current, nxt in zip(roman, roman[1:] + " "):
        value = _SYMBOL_VALUES[current]
        # A smaller symbol before a larger one is subtracted (e.g. IV = 4).
        if nxt in _SYMBOL_VALUES and _SYMBOL_VALUES[nxt] > value:
            total -= value
        else:
            total += value
    return total


def convert(text: str) -> str:
    """Auto-detect the input type and convert it to the other form."""
    text = text.strip()
    if text.isdigit():
        return int_to_roman(int(text))
    return str(roman_to_int(text))


def _interactive() -> None:
    print("Roman Numeral Converter (type 'q' to quit)")
    while True:
        try:
            text = input("Enter a number or Roman numeral: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if text.lower() in {"q", "quit", "exit"}:
            break
        if not text:
            continue
        try:
            print(f"  -> {convert(text)}")
        except ValueError as error:
            print(f"  Error: {error}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Convert between integers (1-3999) and Roman numerals."
    )
    parser.add_argument(
        "value",
        nargs="?",
        help="An integer or a Roman numeral. Omit for interactive mode.",
    )
    args = parser.parse_args(argv)

    if args.value is None:
        _interactive()
        return 0

    try:
        print(convert(args.value))
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
