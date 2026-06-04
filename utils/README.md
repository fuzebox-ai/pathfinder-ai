# Python Utils

This directory contains Python utility functions for text processing and other operations.

## Installation

Make sure you have Python 3.9+ installed. To run the tests, install pytest:

```bash
pip install pytest
```

## Modules

### text_utils.py

Text processing utilities for manipulating and splitting text data.

#### Functions

##### `split_text_by_newline(text: str, keep_empty: bool = False) -> list[str]`

Split text by newline characters.

**Parameters:**
- `text` (str): The input text to split
- `keep_empty` (bool, optional): If True, keep empty lines in the result. If False, filter out empty lines. Default is False.

**Returns:**
- `list[str]`: A list of strings, each representing a line from the input text

**Raises:**
- `TypeError`: If the input is not a string

**Examples:**

```python
from text_utils import split_text_by_newline

# Basic usage
text = "Hello\nWorld"
lines = split_text_by_newline(text)
print(lines)  # Output: ['Hello', 'World']

# Keep empty lines
text = "Hello\n\nWorld"
lines = split_text_by_newline(text, keep_empty=True)
print(lines)  # Output: ['Hello', '', 'World']

# Filter empty lines (default behavior)
text = "Hello\n\nWorld"
lines = split_text_by_newline(text, keep_empty=False)
print(lines)  # Output: ['Hello', 'World']

# Works with different line endings
text = "Hello\r\nWorld\nPython"
lines = split_text_by_newline(text)
print(lines)  # Output: ['Hello', 'World', 'Python']
```

## Running Tests

To run the test suite:

```bash
cd utils
pytest test_text_utils.py -v
```

To run tests with coverage:

```bash
pytest test_text_utils.py --cov=text_utils --cov-report=html
```

## Features

- ✅ Handles different line ending styles (LF, CRLF, CR)
- ✅ Optional filtering of empty lines
- ✅ Type hints for better IDE support
- ✅ Comprehensive error handling
- ✅ Full Unicode support
- ✅ Well-documented with examples
- ✅ Comprehensive test coverage
