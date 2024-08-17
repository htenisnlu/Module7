import turtle

# Hikmet Tenis
# 08/17/2024
# Problem: Draw concentric squares using the turtle module.

def drawSquare(t, sz):
    """
    Get turtle t to draw a square of side sz.
    """
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