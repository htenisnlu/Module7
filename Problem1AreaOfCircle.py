# Hikmet Tenis
# 08/17/2024
# Problem 1: Write a function areaOfCircle(r) which returns the area of a circle of radius r.
# Make sure you use the math module in your solution.

import math

def areaOfCircle(r):
    """
    Calculate the area of a circle with radius r.
    """
    return math.pi * (r ** 2)

# Example usage
radius = 5
print(f"The area of the circle with radius {radius} is {areaOfCircle(radius)}")