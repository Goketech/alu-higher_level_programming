# python-more_data_structures

Collection of intermediate Python exercises that extend basic data structures work into dictionaries, sets, matrix transformations, and small algorithms. These files build on the `python-data_structures` exercises and introduce slightly more complex operations and common patterns used in data manipulation.

## Purpose
- Practice working with dictionaries, sets, nested lists (matrices), and common transformations or aggregations. Exercises focus on clarity, correct handling of edge cases, and small helper functions that can be reused.

## Files and brief descriptions
- `0-square_matrix_simple.py` — transforms a matrix (list of lists) by squaring each integer element.
- `1-search_replace.py` — searches and replaces values in a list, returning a new list or modifying in-place depending on the exercise.
- `2-uniq_add.py` — adds unique integers to a set or similar collection and returns the updated result.
- `3-common_elements.py` — finds common elements between two lists and returns them as a set or list.
- `4-only_diff_elements.py` — returns elements that differ between two collections (symmetric difference).
- `5-number_keys.py` — returns the number of keys in a dictionary.
- `6-print_sorted_dictionary.py` — prints dictionary items sorted by key.
- `7-update_dictionary.py` — updates a dictionary with another mapping and returns the result.
- `8-simple_delete.py` — removes a key from a dictionary and returns the modified dictionary.
- `9-multiply_by_2.py` — multiplies each value in a dictionary by 2 and returns a new dictionary.
- `10-best_score.py` — given a dictionary of student scores, returns the key with the highest score (best student).
- `100-weight_average.py` — compute weighted averages from a list of integer pairs (score, weight) and return the rounded average.
- `101-square_matrix_map.py` — alternative implementation to square matrix entries using `map` and functional constructs.
- `102-complex_delete.py` — a slightly more complex delete operation that carefully removes nested or conditional elements from a data structure.

## Requirements
- Python 3.x.

## Usage
- Most files provide a single function. Import the function into a small test script or use `python -c` for a quick check. Example:

```bash
python3 -c "from 6-print_sorted_dictionary import print_sorted_dictionary; print_sorted_dictionary({'b': 2, 'a': 1})"
```

- Run script files directly if they include an example `if __name__ == '__main__'` block:

```bash
python3 10-best_score.py
```

## Contributing
- Keep exercises focused and well-named following the numeric-naming convention.
- Add docstring examples and small inline tests under the `if __name__ == '__main__'` guard.

## License
- Follow repository license or treat as educational examples if no license is present.
