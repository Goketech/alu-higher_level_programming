# python-data_structures

Small collection of exercises that demonstrate basic Python data structures and common operations on them. Each file is a short script or function that focuses on lists, tuples, matrices, and related manipulations.

## Purpose
- Practice working with Python built-in data structures: lists, tuples, and nested lists (matrices). These exercises are small, self-contained, and suitable for learning and quick testing.

## Files and brief descriptions
- `0-print_list_integer.py` — function that prints all integers of a list, one per line.
- `1-element_at.py` — retrieves and returns an element at a specific index from a list.
- `2-replace_in_list.py` — returns a new list where an element at a specific index is replaced.
- `3-print_reversed_list_integer.py` — prints all integers of a list in reverse order, one per line.
- `4-new_in_list.py` — returns a copy of a list with a new element at a specific index.
- `5-no_c.py` — removes all occurrences of the letter 'c' from a string (or similar behavior).
- `6-print_matrix_integer.py` — prints a matrix of integers with proper formatting.
- `7-add_tuple.py` — adds two tuples element-wise and returns a new tuple.
- `8-multiple_returns.py` — returns multiple values from a function (e.g., first element and length) as a tuple.
- `9-max_integer.py` — finds and returns the maximum integer in a list.
- `10-divisible_by_2.py` — filters a list, returning booleans or values divisible by 2.
- `11-delete_at.py` — deletes an element at a given index in a list and returns the modified list.
- `12-switch.py` — demonstrates swapping variables or values in a container.

## Requirements
- Python 3.x.

## Usage
- Most files provide a function; run them from a small test harness or import the functions into a script. Example:

```bash
python3 -c "from 0-print_list_integer import print_list_integer; print_list_integer([1, 2, 3])"
```

- For files that are scripts, run directly:

```bash
python3 3-print_reversed_list_integer.py
```

## Contributing
- Add small, focused exercises that follow the existing naming convention.
- Include a short comment at the top describing the function signature and expected behavior.

## License
- Follow repository license or treat examples as permissive/educational if none is specified.
