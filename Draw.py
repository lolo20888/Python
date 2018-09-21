import turtle
from tringle import triangle
def shapes():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    angy = turtle.Turtle()
    rasfy = turtle.Turtle()
    i = 0 
    while i <= 3:
        brad.forward(100)
        brad.right(90)
        i = i + 1
    angy.circle(100)
    angy.shape("square")
    angy.color("blue")
    rasfy.triangle(50)
    angy.shape("triangle")
    angy.color("green")

    window.exitonclick()
shapes()