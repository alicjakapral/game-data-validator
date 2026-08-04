# Game Data Validator

Python tool for validating game item data stored in JSON files.

The project was created as a portfolio project focused on QA and game development.
The project validates game data before it is used by the application and generates a readable validation report.

## Features

- Detects missing required fields
- Validates field data types
- Detects empty item names
- Detects negative prices
- Validates item rarity
- Detects invalid ID values
- Detects duplicate IDs
- Generates a validation summary

## Validation Rules

The validator checks:

- Required fields
- Field data types
- Empty item names
- Negative prices
- Allowed rarity values
- Positive item IDs
- Duplicate item IDs

## Project structure

- `main.py` – loads data and generates the validation report
- `validators.py` – contains validation functions
- `items.json` – valid example data
- `invalid_items.json` – intentionally invalid test data

## Technologies

- Python 3
- JSON

## Running the project

Run:

```bash
python main.py
```

By default, the validator checks:

```python
DATA_FILE = "items.json"
```

To test intentionally invalid data, change it to:

```python
DATA_FILE = "invalid_items.json"
```

## Example output

```text
========================================
GAME DATA VALIDATOR
========================================
File: invalid_items.json
Items checked: 15
Errors found: 15

[ERROR] Item ID 1: name cannot be empty.
[ERROR] Item ID 2: price cannot be negative (-50).
[ERROR] Item ID 3: rarity cannot be empty.
[ERROR] Duplicate item ID detected: 4.

Validation finished.
```

## Future improvements

- Exporting validation reports to a file
- Command-line arguments for selecting the input file
- Additional validation rules
- Automated tests

## Author

Alicja Kapral