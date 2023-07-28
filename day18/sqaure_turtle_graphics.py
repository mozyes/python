from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

for i in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)


screen = Screen()
screen.exitonclick()
