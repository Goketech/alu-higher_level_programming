# JavaScript - Web jQuery

This directory contains exercises focused on jQuery and front-end JavaScript development. The projects demonstrate the differences between vanilla JavaScript and jQuery, showcasing how jQuery simplifies DOM manipulation, event handling, and AJAX requests.

## Prerequisites

- Web browser with JavaScript support
- jQuery library (included via CDN in most examples)
- Basic understanding of HTML, CSS, and JavaScript

## Project Structure

Each exercise consists of an HTML file and a corresponding JavaScript file:
- `X-main.html` - HTML page that includes the JavaScript file
- `X-script.js` - JavaScript/jQuery implementation

## Scripts Overview

| Files | Description |
|-------|-------------|
| 0-main.html, 0-script.js | Update header color using vanilla JavaScript |
| 1-main.html, 1-script.js | Update header color using jQuery |
| 2-main.html, 2-script.js | Update header color on click using jQuery |
| 3-main.html, 3-script.js | Add CSS class on click using jQuery |
| 4-main.html, 4-script.js | Toggle CSS classes on click using jQuery |
| 5-main.html, 5-script.js | Add list item to UL using jQuery |
| 6-main.html, 6-script.js | Update header text on click using jQuery |
| 7-main.html, 7-script.js | Fetch character name from Star Wars API |
| 8-main.html, 8-script.js | Fetch and list movie titles from Star Wars API |
| 9-main.html, 9-script.js | Fetch "Hello" in French and display it |
| 100-main.html, 100-script.js | Update header color with vanilla JS (DOM ready) |
| 101-main.html, 101-script.js | Advanced list manipulation (add/remove/clear) |
| 102-main.html, 102-script.js | Translation tool with input field |
| 103-main.html, 103-script.js | Translation tool with click and Enter key support |
| learn.html | Learning/practice file for jQuery GET requests |

## Detailed Descriptions

### Basic DOM Manipulation (0-4)
- **0-script.js**: Uses `document.querySelector()` to change header color to red
- **1-script.js**: Uses jQuery `$('header').css()` to achieve the same result
- **2-script.js**: Adds click event listener to change header color
- **3-script.js**: Adds CSS class instead of inline styles
- **4-script.js**: Toggles between red and green classes

### List Management (5, 101)
- **5-script.js**: Appends new `<li>` elements to a list
- **101-script.js**: Complete list management with add, remove, and clear functionality

### Text Manipulation (6)
- **6-script.js**: Updates header text content when button is clicked

### API Integration (7-9, 102-103)
- **7-script.js**: Fetches character data from Star Wars API
- **8-script.js**: Fetches and displays list of Star Wars movies
- **9-script.js**: Fetches greeting in French from translation API
- **102-script.js**: Interactive translation tool with language code input
- **103-script.js**: Enhanced translation tool with Enter key support

### Advanced Concepts (100)
- **100-script.js**: Demonstrates proper DOM ready handling with vanilla JavaScript

## Key Concepts Covered

- **jQuery vs Vanilla JavaScript**: Comparing syntax and approaches
- **DOM Manipulation**: Selecting elements, changing styles, adding/removing content
- **Event Handling**: Click events, keyboard events (Enter key)
- **AJAX Requests**: GET requests to external APIs
- **CSS Class Management**: Adding, removing, and toggling classes
- **Document Ready**: Ensuring scripts run after DOM is loaded
- **API Integration**: Working with REST APIs (Star Wars API, Translation API)

## APIs Used

- **Star Wars API**: `https://swapi-api.alx-tools.com/api/`
- **Translation API**: `https://fourtonfish.com/hellosalut/`

## How to Use

1. Open any HTML file in a web browser
2. The corresponding JavaScript file will be automatically loaded
3. Interact with the page elements as described in each exercise
4. Check the browser console for any output or errors

### Example Usage

```bash
# Open in browser
open 1-main.html

# Or serve via HTTP server
python3 -m http.server 8000
# Then visit http://localhost:8000/1-main.html
```

## jQuery Features Demonstrated

- Element selection: `$('selector')`
- CSS manipulation: `.css()`, `.addClass()`, `.removeClass()`, `.toggleClass()`
- Text manipulation: `.text()`, `.html()`
- DOM manipulation: `.append()`, `.remove()`, `.empty()`
- Event handling: `.click()`, `.on()`
- AJAX requests: `$.get()`, `$.getJSON()`
- Document ready: `$(document).ready()`

## Learning Progression

The exercises are designed to progress from basic DOM manipulation to advanced AJAX operations:

1. **Basic styling** (0-1): Compare vanilla JS vs jQuery
2. **Event handling** (2-4): Learn click events and CSS classes
3. **Content manipulation** (5-6): Add content and change text
4. **API integration** (7-9): Fetch external data
5. **Advanced features** (100-103): Complex interactions and multiple event types

## Author

Goketech
