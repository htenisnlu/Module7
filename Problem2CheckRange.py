# Hikmet Tenis
# 08/17/2024
# Problem 2: Write a Python function to check whether a number is in a given range. Use
# range(1,10). Print whether the number is in or not in the range.

def checkRange(num, start=1, end=10):
    """
    Check if num is within the range [start, end).
    """
    if num in range(start, end):
        print(f"{num} is in the range.")
    else:
        print(f"{num} is not in the range.")

# Example usage
number = 7
checkRange(number)