# Employee Class

A Python OOP project from the freeCodeCamp Python curriculum.

## Description

This project demonstrates how to create an `Employee` class and manage employee information such as name, level, and salary.

The class uses properties and setters to validate changes to employee attributes and prevent invalid level or salary updates.

## Concepts Practiced

* Classes and objects
* `__init__`
* `__str__` and `__repr__`
* Class attributes
* Instance attributes
* Properties
* Getters and setters
* Attribute validation
* `hasattr()`
* Dictionaries
* Exception handling with `TypeError` and `ValueError`

## Features

* Stores employee name and level
* Automatically assigns a base salary according to the employee's level
* Validates employee names
* Validates employee levels
* Prevents promotion to a lower level
* Prevents selecting the same level again
* Validates salary values
* Updates salary when an employee is promoted
* Provides readable string and representation formats

## Example

```python
charlie_brown = Employee('Charlie Brown', 'trainee')

print(charlie_brown)
print(f'Base salary: ${charlie_brown.salary}')

charlie_brown.level = 'junior'
```

## What I Learned

This project helped me practice using Python properties and setters to control how object attributes are accessed and modified. It also reinforced how class attributes, instance attributes, and methods work together in an OOP design.