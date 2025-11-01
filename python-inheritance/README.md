# python-inheritance

This folder contains exercises that explore the concept of inheritance in Python. The exercises focus on creating base classes, derived classes, and understanding how inheritance works in Python.

## Purpose
- Learn how to define and use base and derived classes.
- Understand the `isinstance()` and `issubclass()` functions.
- Explore method overriding and polymorphism.
- Implement abstract base classes and methods.

## Files and brief descriptions

### Inheritance and Class Hierarchies
- `0-lookup.py` — Function that returns the list of available attributes and methods of an object.
- `1-my_list.py` — Custom list class that inherits from `list` and adds a method to print the list in sorted order.
- `2-is_same_class.py` — Function that checks if an object is exactly an instance of a specified class.
- `3-is_kind_of_class.py` — Function that checks if an object is an instance of, or inherits from, a specified class.
- `4-inherits_from.py` — Function that checks if an object is an instance of a class that inherited (directly or indirectly) from a specified class.
- `5-base_geometry.py` — Empty class `BaseGeometry` as a foundation for further exercises.
- `6-base_geometry.py` — Adds a `area()` method to `BaseGeometry` that raises an exception with a message.
- `7-base_geometry.py` — Adds `integer_validator()` method to `BaseGeometry` for validating integer inputs.
- `8-rectangle.py` — Defines a `Rectangle` class that inherits from `BaseGeometry` and implements `area()` and `__str__()` methods.
- `9-rectangle.py` — Extends `Rectangle` to include width and height validation using `integer_validator()`.

## Requirements
- Python 3.x.

## Usage
- Import classes and functions into a test script or interactive session:

```bash
python3 -c "from 3-is_kind_of_class import is_kind_of_class; print(is_kind_of_class(5, int))"
```

- Run files directly if they include example code under `if __name__ == '__main__'`:

```bash
python3 8-rectangle.py
```

## Key Learning Concepts
- **Inheritance**: Reusing and extending functionality of base classes.
- **Polymorphism**: Using methods in derived classes that override or extend base class methods.
- **Validation**: Implementing input validation in base and derived classes.
- **Abstract Classes**: Creating base classes with methods that must be implemented by derived classes.

## Contributing
- Follow the existing naming convention and incremental complexity pattern.
- Add docstrings and type hints where appropriate.
- Include simple test cases under `if __name__ == '__main__'` blocks.

## License
- Follow repository license or treat these files as educational examples if none is specified.