# Python Programs for Module 7: Lab Activity

This repository contains Python programs developed as part of Module 7 Lab Activity. Each program is designed to solve specific problems and demonstrate the use of various Python features and modules. Below are the details of each program, including their purpose, implementation, and example outputs.

---

```markdown
# Python Problems

## Description
This repository contains Python programs solving various problems related to basic computations, list manipulations, and object-oriented programming. Each problem is encapsulated in a separate Python file, as listed below:

- `Problem1AreaOfCircle.py`: Calculates the area of a circle.
- `Problem2CheckRange.py`: Checks if a number is within a specified range.
- `Problem3MultiplyList.py`: Multiplies all numbers in a list.
- `Problem4Unique.py`: Returns unique elements from a list.
- `Problem5Squares.py`: Draws concentric squares using the turtle module.
- `Problem6ClassCar.py`: Defines a `Car` class with various attributes and methods.

## Installation
To run these programs, ensure you have Python installed on your system. You can download Python from the official [Python website](https://www.python.org/).

## Usage
### Problem 1: Area of a Circle
Calculates the area of a circle given its radius.

```python
# Problem1AreaOfCircle.py

import math

def areaOfCircle(r):
    """Calculate the area of a circle with radius r."""
    return math.pi * r**2

# Example usage
radius = 5
print(f"The area of a circle with radius {radius} is {areaOfCircle(radius)}")
```

### Problem 2: Check Range
Checks whether a number is within the range 1 to 10.

```python
# Problem2CheckRange.py

def checkRange(n):
    """Check if n is in the range 1 to 10."""
    if n in range(1, 11):
        return f"{n} is in the range"
    else:
        return f"{n} is not in the range"

# Example usage
number = 5
print(checkRange(number))
```

### Problem 3: Multiply List
Multiplies all numbers in a list.

```python
# Problem3MultiplyList.py

def multiplyList(lst):
    """Multiply all numbers in a list."""
    result = 1
    for num in lst:
        result *= num
    return result

# Example usage
numbers = [5, 2, 7, -1]
print(f"The result of multiplying the list {numbers} is {multiplyList(numbers)}")
```

### Problem 4: Unique Elements
Returns unique elements from a list.

```python
# Problem4Unique.py

def uniqueList(lst):
    """Return a list of unique elements."""
    unique = []
    for num in lst:
        if num not in unique:
            unique.append(num)
    return unique

# Example usage
numbers = [1, 3, 3, 3, 6, 2, 3, 5]
print(f"The unique elements in the list {numbers} are {uniqueList(numbers)}")
```

### Problem 5: Draw Squares
Draws concentric squares using the turtle module.

```python
# Problem5Squares.py

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of side sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)

# Set up the screen and the turtle
wn = turtle.Screen()
wn.bgcolor("white")

# Create a turtle named alex
alex = turtle.Turtle()
alex.color("blue")
alex.pensize(2)

# Draw concentric squares
size = 20  # Initial size of the square
for i in range(5):
    drawSquare(alex, size)
    size += 20  # Increase the size for the next square
    alex.penup()
    alex.backward(10)  # Move back to the bottom-left corner of the next square
    alex.right(90)
    alex.forward(10)
    alex.left(90)
    alex.pendown()

# Wait for user to close the window
wn.exitonclick()
```

### Problem 6: Car Class
Defines a `Car` class with attributes and methods.

```python
# Problem6ClassCar.py

class Car:
    def __init__(self, model, year, color, type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.manufacturer = manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type

    def get_manufacturer(self):
        return self.manufacturer

    def fullspecs(self):
        return f"{self.model} {self.year} {self.color} {self.type} {self.manufacturer}"

# Example usage
car1 = Car("Sports", 2012, "Blue", "Coupe", "Toyota")
car2 = Car("Sedan", 2020, "Black", "Saloon", "Honda")

print(car1.get_color())       # Output: Blue
print(car1.get_model())       # Output: Sports
print(car2.get_color())       # Output: Black
print(car1.fullspecs())       # Output: Sports 2012 Blue Coupe Toyota
print(car2.fullspecs())       # Output: Sedan 2020 Black Saloon Honda
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- This project was developed as part of a Python tutorial series.
- Inspiration and code examples from various online resources and tutorials.
```

Save this content in a file named `README.md` in your project directory. This file provides a comprehensive guide for anyone who wants to understand and use the Python programs in your repository.
