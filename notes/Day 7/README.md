# Lists in Python

## Introduction

Lists are one of the most versatile and commonly used data structures in Python. They are used to store a collection of items in a specific order. Lists are mutable, which means you can change their content after they are created.

## Creating Lists

There are two ways to create a list in Python:

1. Using square brackets `[]`:
```python
fruits = ["apple", "banana", "orange"]
```

2. Using the `list()` function:
```python
numbers = list(range(1, 6))
```

## Accessing Data in Lists

You can access individual elements in a list using their index. The index starts from 0 for the first element and increases by 1 for each subsequent element.

Example:
```python
numbers = [10, 20, 30, 40, 50]
print(numbers[0])  # Output: 10
print(numbers[2])  # Output: 30
```

## Iterating Over Lists

You can use a `for` loop to iterate over all the elements in a list.

Example:
```python
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
```

Output:
```
apple
banana
orange
```

## List Methods

### 1. Append
The `append()` method adds an element to the end of the list.

Example:
```python
fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'orange']
```

### 2. Extend
The `extend()` method adds multiple elements from another list to the end of the current list.

Example:
```python
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]
```

### 3. Insert
The `insert()` method inserts an element at a specified index.

Example:
```python
fruits = ["apple", "banana"]
fruits.insert(1, "orange")
print(fruits)  # Output: ['apple', 'orange', 'banana']
```

### 4. Clear
The `clear()` method removes all elements from the list.

Example:
```python
numbers = [1, 2, 3]
numbers.clear()
print(numbers)  # Output: []
```

### 5. Pop
The `pop()` method removes and returns the last element of the list.

Example:
```python
fruits = ["apple", "banana", "orange"]
removed_fruit = fruits.pop()
print(removed_fruit)  # Output: 'orange'
print(fruits)         # Output: ['apple', 'banana']
```

### 6. Remove
The `remove()` method removes the first occurrence of a specified element from the list.

Example:
```python
fruits = ["apple", "banana", "orange"]
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'orange']
```

### 7. Index
The `index()` method returns the index of the first occurrence of a specified element in the list.

Example:
```python
fruits = ["apple", "banana", "orange"]
index = fruits.index("banana")
print(index)  # Output: 1
```

### 8. Count
The `count()` method returns the number of occurrences of a specified element in the list.

Example:
```python
fruits = ["apple", "banana", "banana", "orange"]
count = fruits.count("banana")
print(count)  # Output: 2
```

### 9. Sort
The `sort()` method sorts the list in ascending order.

Example:
```python
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4]
```

### 10. Reverse
The `reverse()` method reverses the order of the list.

Example:
```python
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)  # Output: [4, 3, 2, 1]
```

### 11. Join 


The `join()` method is a powerful string method in Python that allows you to concatenate elements from an iterable (e.g., a list, tuple, or set) into a single string. It is commonly used to join the elements of a list into a string with a specified delimiter.

## Syntax

The syntax of the `join()` method is as follows:
```python
delimiter.join(iterable)
```
Here, `delimiter` is the string that will be used as a separator to join the elements, and `iterable` is the collection of elements to be joined.

## Example

```python
fruits = ['apple', 'banana', 'orange']
result = ', '.join(fruits)
print(result)
# Output: "apple, banana, orange"
```


## List Slicing

List slicing allows you to extract a portion of a list by specifying the start and end indices.

Example:
```python
numbers = [1, 2, 3, 4, 5]
sliced_numbers = numbers[1:4]
print(sliced_numbers)  # Output: [2, 3, 4]
```

## Swapping Values in Lists

You can swap the values of two elements in a list using a temporary variable.

Example:
```python
numbers = [1, 2, 3, 4]
numbers[0], numbers[3] = numbers[3], numbers[0]
print(numbers)  # Output: [4, 2, 3, 1]
```

## List Comprehension

List comprehension is a concise way to create lists in Python.

Syntax:
```python
new_list = [expression for item in iterable if condition]
```

Example:
```python
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
```

## List Comprehension with Conditional Logic

You can use conditional logic in list comprehension to filter elements based on a condition.

Example:
```python
numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4]
```

## Nested Lists or 2D Lists

Nested lists, also known as 2D lists, are lists that contain other lists as elements.

Example:
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for num in row:
        print(num)
```

Output:
```
1
2
3
4
5
6
7
8
9
```

---

## Coding Questions for Practice

1. Write a Python program that takes a list of words as input and joins them into a single string separated by spaces.

2. Given a list of integers, write a program to join the even numbers into a string separated by a hyphen ("-").

3. Create a list of strings containing names of fruits. Write a Python function that joins the names into a single string separated by semicolons (";").

4. Write a program to join the elements of a list of sentences into a single string separated by newline characters.

5. Given a list of sentences, remove all punctuation marks from each sentence and then join the words into a single string separated by spaces.

6. Create a list of numbers from 1 to 10. Join the numbers into a single string separated by "+" signs and calculate the result of the addition.

7. Write a Python function that takes a list of words and returns a string containing the first letter of each word, separated by colons (":").

8. Given a list of strings, join the strings into a single string separated by commas. Also, capitalize the first letter of each string before joining.

9. Write a program that takes a list of integers as input and joins them into a single string with each number enclosed in square brackets.

10. Create a list of names. Write a Python function that joins the names into a single string, but if a name starts with the letter "A," it should be excluded from the result.

11. Given a list of sentences, write a program to join the words into a single string with each word reversed.

12. Write a Python function that takes a list of sentences and returns a string containing the last word of each sentence, separated by spaces.

13. Create a list of integers and join them into a single string with each number padded with leading zeros to form a fixed-length string.

14. Given a list of names, write a program to join the names into a single string separated by vertical bars ("|") and display the result in uppercase.

15. Write a Python function that takes a list of sentences and joins them into a single string with the sentences in reverse order.

16. Given a list of words, join the words into a single string, but if a word contains the letter "e," replace it with the letter "o" before joining.

17. Create a list of sentences and join the sentences into a single string with the first letter of each sentence capitalized and followed by a period.

18. Write a program that takes a list of strings and joins them into a single string with each word in lowercase.

19. Given a list of names, write a Python function that joins the names into a single string separated by spaces and then sorts the names in alphabetical order.

20. Create a list of sentences and join them into a single string with each sentence repeated three times, separated by newline characters.

--- 