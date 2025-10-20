# python-exceptions

Collection of small exercises that demonstrate exception handling patterns in Python. These focus on safe printing, safe arithmetic operations, and raising or handling exceptions with informative messages.

## Purpose
- Teach common error-handling idioms:
	- catching and handling exceptions
	- validating inputs and returning safe defaults
	- raising exceptions with messages
	- writing functions that fail gracefully

## Files and brief descriptions
- `0-safe_print_list.py` — safely prints elements of a list; typically catches index or type errors.
- `1-safe_print_integer.py` — safely prints integers and handles non-integer input.
- `2-safe_print_list_integers.py` — prints only integer elements from a list, ignores others safely.
- `3-safe_print_division.py` — performs division with try/except to handle ZeroDivisionError and TypeError.
- `4-list_division.py` — divides elements of two lists element-wise with safe error handling.
- `5-raise_exception.py` — demonstrates raising a generic exception.
- `6-raise_exception_msg.py` — raises an exception with a custom message.
- `100-safe_print_integer_err.py` — variation that returns exception details or error codes when printing integers.
- `101-safe_function.py` — wraps a function call and returns default values on error.
- `102-magic_calculation.py` — a more involved function that may raise or handle errors depending on inputs.

## Requirements
- Python 3.x.

## Usage
- Import functions into a test harness or run files directly if they include example blocks. Example:

```bash
python3 -c "from 3-safe_print_division import safe_print_division; safe_print_division(10, 2)"
```

## Contributing
- Keep examples small and focused. Add docstrings showing expected behavior on normal and error inputs.

## License
- Follow repository license or treat these files as permissive/educational examples if none is specified.
