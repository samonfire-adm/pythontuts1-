# Notes on Dictionaries in Python

## Introduction

Dictionaries are an essential data structure in Python used to store collections of key-value pairs. They are unordered, mutable, and can hold elements of different data types. Dictionaries are incredibly useful for mapping unique keys to their corresponding values, making them ideal for tasks such as data retrieval and organization.

## Creating Dictionaries

There are two ways to create dictionaries in Python:

1. Using Curly Braces: Dictionaries can be defined using curly braces `{}` and specifying key-value pairs separated by colons. For example:
   ```python
   student = {"name": "John", "age": 25, "gender": "male"}
   ```

2. Using `dict()` Function: Dictionaries can also be created using the built-in `dict()` function and providing key-value pairs as arguments. For example:
   ```python
   student = dict(name="John", age=25, gender="male")
   ```

## Accessing Data in Dictionaries

To access the value associated with a specific key in a dictionary, use square bracket notation with the key. For example:
```python
name = student["name"]
```

To avoid raising a `KeyError` when accessing a key that does not exist, you can use the `get()` method. For example:
```python
age = student.get("age", 0)  # If "age" key does not exist, returns 0
```

## Iterating Dictionaries

You can iterate through dictionaries using various methods:

1. Iterating Through Keys:
   ```python
   for key in student.keys():
       print(key)
   ```

2. Iterating Through Values:
   ```python
   for value in student.values():
       print(value)
   ```

3. Iterating Through Key-Value Pairs:
   ```python
   for key, value in student.items():
       print(key, value)
   ```

## Using `in` with Dictionaries

You can use the `in` keyword to check if a key exists in the dictionary. For example:
```python
if "name" in student:
    print("Name exists!")
```

## Dictionary Methods

Some commonly used dictionary methods include:

- `clear()`: Removes all items from the dictionary.
- `copy()`: Returns a shallow copy of the dictionary.
- `fromkeys()`: Creates a new dictionary with specified keys and values.
- `get()`: Returns the value for a given key, and a default value if the key does not exist.
- `pop()`: Removes and returns the value for a given key.
- `popitem()`: Removes and returns the last key-value pair added to the dictionary.
- `update()`: Updates the dictionary with new key-value pairs from another dictionary.

## Dictionary Comprehension

Dictionary comprehension is a concise way to create dictionaries using an expression and an optional condition. For example:
```python
squares = {x: x**2 for x in range(1, 6)}
```

## Nested Dictionaries

Dictionaries can also be nested, creating multi-dimensional data structures. For example:
```python
contacts = {
    "John": {"phone": "123-456-7890", "email": "john@example.com"},
    "Jane": {"phone": "987-654-3210", "email": "jane@example.com"}
}
```
---