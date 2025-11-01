# python-input_output

This folder contains exercises that focus on file handling, JSON serialization/deserialization, and input/output operations in Python.

## Purpose
- Learn how to read from and write to files in Python.
- Understand JSON serialization and deserialization.
- Explore advanced file handling techniques.

## Files and brief descriptions

### File Handling
- `0-read_file.py` — Function to read a text file and print its content to stdout.
- `1-write_file.py` — Function to write a string to a text file and return the number of characters written.
- `2-append_write.py` — Function to append a string to a text file and return the number of characters added.

### JSON Serialization/Deserialization
- `3-to_json_string.py` — Function to convert a Python object to a JSON string.
- `4-from_json_string.py` — Function to convert a JSON string back to a Python object.
- `5-save_to_json_file.py` — Function to save a Python object to a file in JSON format.
- `6-load_from_json_file.py` — Function to load a Python object from a JSON file.
- `7-add_item.py` — Script to add all command-line arguments to a Python list and save them to a file in JSON format.
- `8-class_to_json.py` — Function to return the dictionary description of an object for JSON serialization.

### Classes and JSON
- `9-student.py` — Class `Student` with methods to serialize and deserialize its attributes.
- `10-student.py` — Extends `Student` to include selective attribute serialization.
- `11-student.py` — Further extends `Student` to allow reloading attributes from a JSON string.
- `12-pascal_triangle.py` — Function to generate Pascal's triangle up to a given number of rows.

### Advanced File Handling
- `100-append_after.py` — Function to insert a line of text to a file after each line containing a specific string.
- `101-stats.py` — Script to read lines from stdin and compute metrics (e.g., line count, status codes).

## Requirements
- Python 3.x.

## Usage
- Import functions or classes into a test script or interactive session:

```bash
python3 -c "from 0-read_file import read_file; read_file('example.txt')"
```

- Run scripts directly if they include example code under `if __name__ == '__main__'`:

```bash
python3 7-add_item.py item1 item2
```

## Key Learning Concepts
- **File Handling**: Reading, writing, and appending to files.
- **JSON**: Converting between Python objects and JSON strings/files.
- **Serialization**: Preparing objects for storage or transmission.
- **Advanced Techniques**: Modifying files based on content and processing input streams.

## Contributing
- Follow the existing naming convention and incremental complexity pattern.
- Add docstrings and type hints where appropriate.
- Include simple test cases under `if __name__ == '__main__'` blocks.

## License
- Follow repository license or treat these files as educational examples if none is specified.