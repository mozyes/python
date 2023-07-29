import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")


def move_forwards():
    tim.forward(10)


def move_left():
    tim.setheading(tim.heading() + 10)


def move_right():
    tim.setheading(tim.heading() - 10)


def move_backwards():
    tim.backward(10)


def clear():
    tim.reset()
    tim.color("red")


screen = t.Screen()
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
