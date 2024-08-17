# Hikmet Tenis
# 08/17/2024
# Problem 3: Write a Python function to multiply all the numbers in a list. Use list [5, 2, 7, -1].

def multiplyList(lst):
    """
    Multiply all the numbers in a list.
    """
    result = 1
    for num in lst:
        result *= num
    return result

# Example usage
numbers = [5, 2, 7, -1]
print(f"The product of the list {numbers} is {multiplyList(numbers)}")