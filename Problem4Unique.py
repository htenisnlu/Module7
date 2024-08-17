# Hikmet Tenis
# 08/17/2024
# Problem 4: Write a Python function that takes a list of numbers and returns a new list with
# unique elements of the first list. Use list [1, 3, 3, 3, 6, 2, 3, 5]. Use the append function.

def uniqueList(lst):
    """
    Return a new list with unique elements of the first list.
    """
    unique_elements = []
    for num in lst:
        if num not in unique_elements:
            unique_elements.append(num)
    return unique_elements

# Example usage
numbers = [1, 3, 3, 3, 6, 2, 3, 5]
print(f"The unique elements in the list {numbers} are {uniqueList(numbers)}")