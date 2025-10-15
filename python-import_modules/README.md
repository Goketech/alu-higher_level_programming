
# python-import_modules

Small collection of Python exercises and examples that demonstrate importing modules, using packages, and organizing code across multiple files. These examples are intended for learners following the ALX / Higher Level Programming track who want to practice structuring small Python projects and using imports correctly.

## Purpose
- Teach module creation and import mechanics in Python:
	- top-level scripts vs. modules
	- absolute and relative imports
	- package layout (using __init__.py when appropriate)
	- avoiding circular imports
	- using the `if __name__ == '__main__'` guard for module testing

## Contents
- This folder contains short, focused examples and exercises, typically named using the ALX convention (e.g. `0-*.py`, `1-*.py`, ...). Each file demonstrates a specific import-related concept.

Typical files you may see:
- `0-readme.py` — a tiny example that may import a helper module and print the result.
- `1-writeme.py` — demonstrate writing helper functions in another module and importing them.
- `100-starwars_characters.py`, `101-starwars_characters.py` — slightly larger examples that show splitting logic across several modules for readability and testability.

Project layout notes:
- If an example uses multiple files, you'll see helper modules in the same folder or a subpackage. Look for `__init__.py` if a package layout is used.

## Requirements
- Python 3.x.

## Usage
- Run single-file examples directly with the interpreter:

```bash
python3 0-readme.py
```

- If the example is part of a package and uses relative imports, run the example as a module from the package root. Example (from repo root):

```bash
python3 -m python_import_modules.some_example
```

- Inspect the top of each file for expected inputs or usage notes. Some scripts accept command-line arguments.

## Common import gotchas (learning tips)
- Use absolute imports for clarity in larger projects.
- Use relative imports for small packages where modules are tightly coupled (e.g. `from .helpers import foo`).
- Avoid running modules that use relative imports directly from within the package directory; prefer `python -m package.module`.
- Keep side-effects out of module import time; place run-time code under `if __name__ == '__main__':`.

## Contributing
- Add small, focused examples. Each new example should include a short header comment explaining what it demonstrates.
- Add tests or simple usage examples under an `if __name__ == '__main__'` block.

## License
Follow the repository license or treat these files as educational examples if no license is present.

