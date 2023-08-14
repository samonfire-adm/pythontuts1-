# Basics of Object-Oriented Programming (OOP) in Python

Object-Oriented Programming (OOP) is a paradigm that allows you to organize your code into reusable, self-contained units called **classes**. Each class defines a blueprint for creating objects, which are instances of the class. OOP promotes the concept of objects and their interactions, making code more modular and easier to manage. In OOP, you treat real-world entities as objects, which have both attributes (characteristics) and methods (functions). This approach promotes better organization and understanding of code, making it easier to manage complex programs.

## Classes and Objects

A **class** is a blueprint for creating objects. It defines the structure and behavior of objects of that class. An **object** is an instance of a class, and it holds both data (attributes) and functions (methods) related to that class.

### Syntax of a Class

```python
class ClassName:
    # Class attributes
    attribute1 = value1
    attribute2 = value2

    # Constructor (initializer)
    def __init__(self, parameter1, parameter2):
        self.parameter1 = parameter1
        self.parameter2 = parameter2

    # Methods
    def method1(self):
        # Method code
        pass

    def method2(self):
        # Method code
        pass
```

- `class`: Keyword to define a class.
- `ClassName`: Name of the class (follows naming conventions).
- `__init__(self, parameter1, parameter2)`: Constructor method that initializes object attributes. `self` refers to the instance being created.
- `attribute1 = value1`: Class attributes to store data.
- `method1(self)`: Methods to define functionalities. They take `self` as the first parameter to refer to the instance.

### Example: Creating a Class and Objects

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

# Creating objects
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

print(student1.introduce())  # Output: Hi, I'm Alice and I'm 20 years old.
print(student2.introduce())  # Output: Hi, I'm Bob and I'm 22 years old.
```

In this example, `Student` is a class with attributes `name` and `age`, along with the `introduce` method. Objects `student1` and `student2` are instances of the `Student` class.

### Example: Creating a Class and Objects
```Python
class Parrot:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def speak(self, sound):
        return f"{self.name} says {sound}"

blu = Parrot("Blu", "Blue")
print(blu.speak("Hello!"))
```

OOP enables you to create organized, reusable, and modular code by defining classes and creating objects from those classes. Each object can have its own attributes and methods, allowing you to model real-world entities effectively.