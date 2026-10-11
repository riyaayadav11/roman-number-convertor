# Roman Numeral Converter

A small, dependency-free Python tool that converts integers to Roman numerals and back. Works as a library and as a command-line app.

## Features

- Integer to Roman numeral (1 to 3999)
- Roman numeral to integer, with strict validation (rejects `IIII`, `VX`, `IC`, etc.)
- Auto-detects the input direction on the command line
- Interactive mode
- Full unit test suite, including a round-trip check of every value from 1 to 3999

## Requirements

Python 3.8 or newer. No external packages.

## Usage

### Command line

```bash
python roman_converter.py 1994      # MCMXCIV
python roman_converter.py MCMXCIV   # 1994
python roman_converter.py           # interactive mode
```

### As a library

```python
from roman_converter import int_to_roman, roman_to_int

int_to_roman(2024)       # 'MMXXIV'
roman_to_int("MMXXIV")   # 2024
```

Invalid input raises `ValueError` (bad value or malformed numeral) or `TypeError` (wrong type).

## How it works

- **Integer to Roman:** walk a table of values from largest to smallest (including subtractive pairs like `CM`, `XL`, `IV`) and append each symbol as many times as it fits.
- **Roman to integer:** validate with a regular expression for canonical numerals, then scan left to right, subtracting a symbol when a larger one follows it.

## Running the tests

```bash
python -m unittest -v
```

## Project structure

```
.
├── roman_converter.py       # converter + CLI
├── test_roman_converter.py  # unit tests
├── README.md
├── LICENSE
└── .gitignore
```

## License

MIT. See [LICENSE](LICENSE).
