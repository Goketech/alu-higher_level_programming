# python-more_classes

This folder contains exercises that build on the concept of classes in Python, focusing on advanced features and use cases. The primary focus is on the `Rectangle` class, which evolves through the exercises, and a solution to the N-Queens problem.

## Purpose
- Deepen understanding of Object-Oriented Programming (OOP) in Python.
- Explore advanced class features like:
  - Special methods (`__str__`, `__repr__`, etc.)
  - Class and static methods
  - Instance counting
  - Comparison operators
  - Memory management (`__del__`)

## Files and brief descriptions

### Rectangle Class Progression
- `0-rectangle.py` — Basic empty `Rectangle` class definition.
- `1-rectangle.py` — Adds width and height attributes with validation.
- `2-rectangle.py` — Adds `area()` and `perimeter()` methods.
- `3-rectangle.py` — Adds `__str__` method for string representation of the rectangle.
- `4-rectangle.py` — Adds `__repr__` method for unambiguous string representation.
- `5-rectangle.py` — Adds `__del__` method with a message when an instance is deleted.
- `6-rectangle.py` — Adds a class attribute to count the number of instances.
- `7-rectangle.py` — Adds a class attribute to define the print symbol for the rectangle.
- `8-rectangle.py` — Adds a static method to compare two rectangles by area.
- `9-rectangle.py` — Adds a class method to create a square (a rectangle with equal width and height).

### Additional Problem
- `101-nqueens.py` — Solves the N-Queens problem for a given board size using backtracking.

## Requirements
- Python 3.x.

## Usage
- Import classes and instantiate them in a test script or interactive session:

```bash
python3 -c "from 3-rectangle import Rectangle; r = Rectangle(3, 4); print(r.area())"
```

- Run files directly if they include example code under `if __name__ == '__main__'`:

```bash
python3 4-rectangle.py
```

- For the N-Queens problem:

```bash
python3 101-nqueens.py 8
```

## Key Learning Concepts
- **Encapsulation**: Private attributes and controlled access via methods.
- **Special Methods**: `__str__`, `__repr__`, `__del__`, and comparison operators for natural object behavior.
- **Class and Static Methods**: Shared functionality and alternative constructors.
- **Algorithmic Thinking**: Solving the N-Queens problem with backtracking.

## Contributing
- Follow the existing naming convention and incremental complexity pattern.
- Add docstrings and type hints where appropriate.
- Include simple test cases under `if __name__ == '__main__'` blocks.

## License
- Follow repository license or treat these files as educational examples if none is specified.