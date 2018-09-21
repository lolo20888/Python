import turtle
def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("green")
    brad.speed(3)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    angy = turtle.Turtle()
    angy.circle(100)
    angy.shape("square")
    angy.color("blue")
    window.exitonclick()
draw_square()

