# python-everything_is_object

This folder contains exercises and questions designed to deepen understanding of Python's object model. The exercises explore concepts like mutability, identity, and reference behavior in Python objects.

## Purpose
- Understand the difference between mutable and immutable objects.
- Learn how Python handles object references and memory.
- Explore special methods and object behavior.

## Files and brief descriptions

### Answer Files
- `0-answer.txt` to `28-answer.txt` — Text files containing answers to conceptual questions about Python objects.
- `103-line1.txt` to `106-line5.txt` — Additional answer files for advanced questions.

### Python Scripts
- `19-copy_list.py` — Demonstrates how to correctly copy a list in Python.
- `100-magic_string.py` — Implements a function that returns a magic string with specific behavior.
- `101-locked_class.py` — Demonstrates the use of `__slots__` to restrict dynamic attribute creation in a class.

## Requirements
- Python 3.x.

## Usage
- For answer files, open and read the content to understand the concepts.
- Run Python scripts directly to observe their behavior:

```bash
python3 19-copy_list.py
```

- For `101-locked_class.py`, test the restricted attribute behavior:

```bash
python3 -c "from 101-locked_class import LockedClass; obj = LockedClass(); obj.first_name = 'John'; print(obj.first_name)"
```

## Key Learning Concepts
- **Mutability**: Understand which objects can be modified in place.
- **Identity vs Equality**: Learn the difference between `is` and `==`.
- **Object References**: Explore how Python variables reference objects in memory.
- **Special Methods**: Implement and use methods like `__slots__` and others.

## Contributing
- Follow the existing naming convention for new files.
- Add comments or explanations to Python scripts for clarity.

## License
- Follow repository license or treat these files as educational examples if none is specified.