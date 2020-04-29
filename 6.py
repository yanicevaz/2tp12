import turtle


def drawCurve(turtle, x,n):
    if n ==0:
        turtle.forward(x)
        return
    else:

        drawCurve(turtle,x/3,n-1)
        turtle.left(60)
        drawCurve(turtle,x/3,n-1)
        turtle.right(120)
        drawCurve(turtle,x/3,n-1)
        turtle.left(60)
        drawCurve(turtle,x/3,n-1)





if __name__ == "__main__":
    turtle.setup(800, 400)
    drawCurve(turtle, 300, 3)
    turtle.exitonclick()
