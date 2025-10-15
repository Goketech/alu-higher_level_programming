
# python-if_else_loops_functions

Collection of small Python exercises used in the ALX / Higher Level Programming track to practice control flow (if/else), loops, and functions.

## Purpose
- Provide short, focused scripts that demonstrate basic Python constructs:
	- Conditional statements (if, elif, else)
	- Looping (for, while)
	- Function definition and return values
	- Simple algorithmic problems and small utilities

## Contents
- Multiple single-file exercises named with the ALX convention (e.g. `0-*.py`, `1-*.py`, ...). Each file is a tiny, self-contained script intended to be run from the command line.

Notable example files in this folder (may not be exhaustive):
- `0-positive_or_negative.py` — check and print if an integer is positive/negative/zero.
- `1-last_digit.py` — print the last digit of a number.
- `2-print_alphabet.py`, `3-print_alphabt.py` — alphabet-printing exercises.
- `10-add.py` — simple add function demonstration.
- `11-second_biggest.py` — find the second largest number in a list.
- `100-print_tebahpla.py` — printing in reverse or specialized output exercises.
- `101-remove_char_at.py` — remove a character at a given index and print result.
- `102-magic_calculation.py` — a slightly larger function that performs arithmetic based on conditions.

Each script is intentionally short and designed to be read and understood quickly.

## Requirements
- Python 3.x (3.6+ recommended).

## Usage
- To run an exercise directly with the interpreter:

```bash
python3 0-positive_or_negative.py
```

- Some scripts include a shebang (`#!/usr/bin/env python3`) and can be made executable:

```bash
chmod +x 0-positive_or_negative.py
./0-positive_or_negative.py
```

- Many scripts expect one or more command-line arguments; read the file's top comments or source to see expected inputs.

## Contributing
- Keep changes minimal and focused per exercise.
- Add a short comment at the top of any new script describing the goal and expected inputs/outputs.
- Follow PEP 8 for formatting. Keep function and variable names clear.

## Testing / Verification
- These are small scripts — to verify a change, run the modified file and confirm expected stdout.
- For functions that return values, consider adding a small if __name__ == '__main__' block with a quick smoke example.

## Style and Learning Notes
- Prefer clear, idiomatic Python constructs over clever one-liners when the goal is learning.
- Add a few inline comments for any non-obvious steps.

## License
Follow the repository license. If none is specified, treat these exercises as permissive/educational examples.

