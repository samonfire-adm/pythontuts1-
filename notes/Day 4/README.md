# Notes on Boolean & Conditional Logic in Python

## Boolean Data Type

In Python, the Boolean data type represents the two truth values, True and False. Booleans are used in conditional statements and logical operations to make decisions and control the flow of a program.

## Getting User Input

In Python, you can get user input using the `input()` function. The `input()` function prompts the user to enter data, and the entered value is treated as a string. To convert the input to a specific data type, you can use type casting.

## Conditional Logic

Conditional logic in Python allows us to execute specific blocks of code based on certain conditions. It involves the use of conditional statements, such as `if`, `elif`, and `else`, to control the program's flow.


## Intro to Conditional Statements

Conditional statements allow us to perform different actions based on whether a certain condition is true or false. The basic structure of an `if` statement in Python is as follows:
```python
if condition:
    # Code block to execute if the condition is true
else:
    # Code block to execute if the condition is false
```

## Multiple Elif

In addition to the `if` and `else` statements, Python also allows the use of multiple `elif` (short for "else if") statements to test multiple conditions and execute the corresponding block of code.

# More Examples on if-elif-else Statements

Example 1: Checking if a Number is Positive, Negative, or Zero
```python
num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

Example 2: Determining the Grade based on Score
```python
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

Example 3: Checking Leap Year
```python
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
```

---

# Nested Conditional Statements in Python

Conditional statements in Python allow you to control the flow of your program based on certain conditions. Nested conditional statements refer to the concept of having one conditional statement inside another. This allows you to check secondary conditions within the primary condition. Nested conditionals are useful when you need to add more granularity to your program's logic.

## Syntax of Nested Conditional Statements

The syntax of a nested conditional statement in Python looks like this:

```python
if condition1:
    # Code block executed if condition1 is True
    if condition2:
        # Code block executed if both condition1 and condition2 are True
    else:
        # Code block executed if condition1 is True and condition2 is False
else:
    # Code block executed if condition1 is False
```

## Example of Nested Conditional Statements

Let's see some examples of nested conditional statements in Python:

### Example 1: Checking Grades

```python
# Input the student's score
score = int(input("Enter the student's score: "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
else:
    # If the score is less than 80, check if it's a passing grade
    if score >= 60:
        grade = 'C'
    else:
        grade = 'F'

print(f"The student's grade is: {grade}")
```

In this example, we have a nested if-else statement inside the else block of the outer if-else statement. It checks if the score is less than 80 and assigns the appropriate grade accordingly.

### Example 2: Checking Leap Year

```python
# Input the year
year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
```

In this example, we have multiple nested if statements to determine whether a year is a leap year or not. The program checks if the year is divisible by 4, then further checks if it's divisible by 100 and 400 to determine the leap year condition.

These are just a few examples of how nested conditional statements can be used in Python to handle complex decision-making scenarios. Remember to properly indent your code to maintain the hierarchy of the nested statements.


---


## Truthiness and Falsiness

In Python, truthiness refers to values that are considered true when evaluated in a Boolean context, while falsiness refers to values that are considered false. For example, any non-zero number, non-empty strings, and non-empty containers (lists, dictionaries, etc.) are truthy, while zero, empty strings, and empty containers are falsy.

# Examples of Truthiness and Falsiness

Example 1: Using Truthy Value in a Conditional Statement
```python
name = input("Enter your name: ")

if name:
    print(f"Hello, {name}!")
else:
    print("Please enter your name.")
```

Example 2: Using Falsy Value in a Conditional Statement
```python
count = 0

if not count:
    print("The count is zero.")
else:
    print(f"The count is {count}.")
```

---

## Operators in Python

### Arithmetic Operators

Arithmetic operators perform basic mathematical operations on numeric operands:
- `+`: Addition
- `-`: Subtraction
- `*`: Multiplication
- `/`: Division
- `%`: Modulo (remainder)
- `**`: Exponentiation
- `//`: Floor Division (quotient without remainder)

#### Examples of Arithmetic Operators 
```python
x = 10
y = 3

addition = x + y         # 13
subtraction = x - y      # 7
multiplication = x * y   # 30
division = x / y         # 3.3333333333333335
modulo = x % y           # 1
exponentiation = x ** y  # 1000
floor_division = x // y  # 3
```
### Comparison Operators
Comparison operators, also known as relational operators, are used to compare two values and determine the relationship between them. These operators return a Boolean value (True or False) based on whether the comparison is true or false. Here are the six comparison operators in Python:

1. **Less Than (`<`)**: Checks if the value on the left is less than the value on the right.

2. **Greater Than (`>`)**: Checks if the value on the left is greater than the value on the right.

3. **Less Than or Equal To (`<=`)**: Checks if the value on the left is less than or equal to the value on the right.

4. **Greater Than or Equal To (`>=`)**: Checks if the value on the left is greater than or equal to the value on the right.

5. **Equal To (`==`)**: Checks if the value on the left is equal to the value on the right.

6. **Not Equal To (`!=`)**: Checks if the value on the left is not equal to the value on the right.

## Syntax and Examples

Here are some examples of how comparison operators are used in Python:

```python
x = 10
y = 5

# Less Than
print(x < y)    # Output: False

# Greater Than
print(x > y)    # Output: True

# Less Than or Equal To
print(x <= y)   # Output: False

# Greater Than or Equal To
print(x >= y)   # Output: True

# Equal To
print(x == y)   # Output: False

# Not Equal To
print(x != y)   # Output: True
```

Comparison operators can also be used with other data types, such as strings, floats, tuples, sets, and dictionaries:

```python
# String Comparison
name1 = "Alice"
name2 = "Bob"
print(name1 < name2)    # Output: True

# Float Comparison
num1 = 3.14
num2 = 2.71
print(num1 > num2)      # Output: True

# Tuple Comparison
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
print(tuple1 <= tuple2) # Output: True

# Set Comparison
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 != set2)     # Output: True

# Dictionary Comparison
dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 1, 'b': 3}
print(dict1 == dict2)   # Output: False
```
---

### Assignment Operators

Assignment operators are used to assign values to variables:
- `=`: Assigns the value on the right to the variable on the left.
- `+=`, `-=`, `*=`, `/=`, `%=`: Performs the operation on the right and assigns the result to the variable on the left.

### Examples of Assignment Operators
```python
x = 10
y = 3

x += y  # Equivalent to x = x + y (x becomes 13)
x -= y  # Equivalent to x = x - y (x becomes 10)
x *= y  # Equivalent to x = x * y (x becomes 30)
x /= y  # Equivalent to x = x / y (x becomes 10.0)
x %= y  # Equivalent to x = x % y (x becomes 1)
```

### Conditional Operator

The conditional operator (ternary operator) allows for a compact way to write simple `if-else` statements in a single line:
```python
variable = value_if_true if condition else value_if_false
```

#### Examples of Conditional Operators

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
```


### Logical Operators

Logical operators perform logical operations on Boolean values:
- `and`: Returns True if both operands are True.
- `or`: Returns True if at least one operand is True.
- `not`: Returns the negation of the operand.

#### Examples of Logical  Operators
```python
x = True
y = False

and_result = x and y   # False
or_result = x or y     # True
not_x = not x          # False
```

### Identity Operators

Identity operators compare the memory location of two objects:
- `is`: Returns True if both operands refer to the same object.
- `is not`: Returns True if both operands refer to different objects.

#### Examples of Identity Operators
```python
x = [1, 2, 3]
y = [1, 2, 3]
z = x

is_same_x_y = x is y          # False (x and y have different memory locations)
is_same_x_z = x is z          # True (x and z refer to the same object)
is_not_same_x_y = x is not y  # True (x and y have different memory locations)
```

### Membership Operators

Membership operators test for membership in a sequence (e.g., lists, tuples, strings):
- `in`: Returns True if the specified item is present in the sequence.
- `not in`: Returns True if the specified item is not present in the sequence.

#### Examples of Membership Operators
```python
name = "Alice"
contains_l = "l" in name           # True
contains_z = "z" not in name       # True
contains_al = "al" in name         # True
contains_xyz = "xyz" not in name   # True
```

---

## Comparison between "is" and "=="

In Python, `is` is used to compare object identities, i.e., if two variables refer to the same object in memory. On the other hand, `==` is used to compare the values of two objects. While `==` checks for equality of values, `is` checks for identity.

---

## Practice Questions

1. What is the output of the following code?
```python
num = 10
if num > 5:
    print("Greater than 5")
else:
    print("Less than or equal to 5")
```

2. Write a Python program that takes a user's age as input and prints whether they are a minor (below 18) or an adult.

3. What is the difference between the `and` and `or` logical operators? Provide examples.

4. How can you check if an element is present in a list using the membership operator?

5. Explain the truthiness and falsiness concept in Python with examples.

6. What is the purpose of the `elif` statement? Provide a scenario where it is used.

7. Write a Python program that checks if a given year is a leap year or not.

8. Explain the difference between the `/` (division) and `//` (floor division) arithmetic operators.

9. What happens if you use the `input()` function without assigning it to a variable?

10. Describe the usage of the conditional operator (ternary operator) in Python.

11. What is the result of the expression `2 ** 3 // 4 + 5 % 6`?

12. Explain the working of the `not in` membership operator with strings.

13. Write a Python program that takes two numbers as input and swaps their values without using a third variable.

14. How can you determine if a given string is empty or not?

15. What is the difference between using `is` and `==` for comparing two variables in Python?

---

