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
