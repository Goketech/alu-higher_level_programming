# python-classes

Collection of exercises that introduce Object-Oriented Programming (OOP) concepts in Python through the creation and evolution of classes. The exercises primarily focus on a `Square` class that progressively gains features, plus additional examples like linked lists and special methods.

## Purpose
- Learn fundamental OOP concepts:
  - Class definition and instantiation
  - Instance attributes and methods
  - Property decorators (getters and setters)
  - Special methods (`__str__`, `__repr__`, etc.)
  - Data validation and encapsulation
  - Class composition and relationships

## Files and brief descriptions

### Square Class Progression
- `0-square.py` — basic empty Square class definition.
- `1-square.py` — Square class with a private size attribute.
- `2-square.py` — adds size validation (must be integer >= 0) in the constructor.
- `3-square.py` — adds an `area()` method to calculate and return the square's area.
- `4-square.py` — adds getter and setter properties for the size attribute with validation.
- `5-square.py` — adds a `my_print()` method that prints the square using '#' characters.
- `6-square.py` — adds position attribute to control where the square is printed with spaces.
- `101-square.py` — enhanced version with `__str__` method for string representation.
- `102-square.py` — adds comparison operators (`<`, `<=`, `==`, `!=`, `>`, `>=`) based on area.

### Additional Classes
- `100-singly_linked_list.py` — implementation of a singly linked list with Node and SinglyLinkedList classes.
- `103-magic_class.py` — demonstrates special methods and potentially mimics a bytecode pattern.

## Requirements
- Python 3.x.

## Usage
- Import classes and instantiate them in a test script or interactive session:

```bash
python3 -c "from 3-square import Square; s = Square(5); print(s.area())"
```

- Run files directly if they include example code under `if __name__ == '__main__'`:

```bash
python3 4-square.py
```

- For the linked list example:

```bash
python3 -c "from 100-singly_linked_list import SinglyLinkedList; sl = SinglyLinkedList(); sl.sorted_insert(1); print(sl)"
```

## Key Learning Concepts
- **Encapsulation**: Private attributes (prefixed with `_`) and controlled access via properties.
- **Validation**: Input checking in setters to maintain object integrity.
- **Special Methods**: `__str__`, `__repr__`, comparison operators for natural object behavior.
- **Progressive Development**: Each file builds upon the previous, showing iterative class enhancement.

## Contributing
- Follow the existing naming convention and incremental complexity pattern.
- Add docstrings and type hints where appropriate.
- Include simple test cases under `if __name__ == '__main__'` blocks.

## License
- Follow repository license or treat these files as educational examples if none is specified.
