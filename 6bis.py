from ex6 import *

def floconNeige(turtle, l, order):
    for i in range(0,3):
        drawCurve(turtle, 1,order)
        turtle.right(120)

if __name__ == "__main__":
    turtle.setup(800,600)
    floconNeige(turtle,300,3)
    turtle.exitonclick()
