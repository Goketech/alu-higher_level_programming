# JavaScript - Web Scraping

This directory contains JavaScript scripts focused on web scraping, HTTP requests, file operations, and API interactions. The exercises demonstrate various techniques for working with external APIs, handling HTTP responses, and processing data in Node.js.

## Prerequisites

- Node.js installed
- `request` module (install with: `npm install request`)

## Scripts Overview

| File | Description |
|------|-------------|
| 0-readme.js | Reads and displays the content of a file |
| 1-writeme.js | Writes a string to a file |
| 2-statuscode.js | Displays the status code of a GET request |
| 3-starwars_title.js | Prints the title of a Star Wars movie by episode number |
| 4-starwars_count.js | Counts movies where "Wedge Antilles" appears |
| 5-request_store.js | Gets a webpage and stores it in a file |
| 6-completed_tasks.js | Computes the number of tasks completed by user id |
| 100-starwars_characters.js | Prints all characters of a Star Wars movie |
| 101-starwars_characters.js | Prints all characters of a Star Wars movie (in order) |

## Detailed Descriptions

### 0-readme.js
Reads and prints the content of a file passed as argument.
```bash
./0-readme.js filename.txt
```

### 1-writeme.js
Writes a string to a file. Takes filename and content as arguments.
```bash
./1-writeme.js my_file.txt "Python is cool"
```

### 2-statuscode.js
Makes a GET request to a URL and displays the status code.
```bash
./2-statuscode.js https://httpbin.org/status/200
```

### 3-starwars_title.js
Prints the title of a Star Wars movie using the Star Wars API.
```bash
./3-starwars_title.js 1
```

### 4-starwars_count.js
Counts the number of movies where the character "Wedge Antilles" appears.
```bash
./4-starwars_count.js https://swapi-api.hbtn.io/api/films/
```

### 5-request_store.js
Downloads the content from a URL and stores it in a file.
```bash
./5-request_store.js http://loripsum.net/api loripsum
```

### 6-completed_tasks.js
Computes the number of tasks completed by each user from a JSON API.
```bash
./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
```

### 100-starwars_characters.js
Prints all characters from a Star Wars movie (order may vary due to async requests).
```bash
./100-starwars_characters.js 3
```

### 101-starwars_characters.js
Prints all characters from a Star Wars movie in the correct order using recursive calls.
```bash
./101-starwars_characters.js 3
```

## Key Concepts Covered

- File system operations (reading/writing files)
- HTTP requests using the `request` module
- JSON parsing and manipulation
- API interactions (Star Wars API, JSONPlaceholder)
- Asynchronous programming
- Error handling
- Data processing and filtering

## Installation

To run these scripts, you'll need to install the required dependencies:

```bash
npm install request
```

## Usage

Make sure the scripts are executable:
```bash
chmod +x *.js
```

Then run any script with:
```bash
./<script-name> [arguments]
```

## Author

Goketech
