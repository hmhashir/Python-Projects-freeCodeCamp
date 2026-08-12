# Medical Records Validator

A Python data validation project completed as part of the freeCodeCamp curriculum.

## Overview

This project validates medical record data stored as a list or tuple of dictionaries.

The validator checks:

- Whether the input is a list or tuple
- Whether each item is a dictionary
- Whether the required keys are present
- Whether patient IDs follow the expected format
- Whether ages are valid
- Whether gender values are valid
- Whether diagnoses contain valid values
- Whether medications are stored as a list of strings
- Whether visit IDs follow the expected format

## Concepts Demonstrated

- Python functions
- Dictionaries
- Lists and tuples
- Loops
- `enumerate()`
- List comprehensions
- `isinstance()`
- Dictionary `.items()` and `.keys()`
- Regular expressions with `re`
- `**kwargs` / dictionary unpacking
- Boolean validation
- Error handling and validation logic

## Technologies

- Python 3
- Python Standard Library
- `re` module

## How to Run

Clone the repository and navigate to the project directory:

```bash
cd medical-records-validator