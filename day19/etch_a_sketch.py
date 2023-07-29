import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")


def move_forwards():
    tim.forward(10)


def move_left():
    tim.left(90)


def move_right():
    tim.right(90)


def move_backwards():
    tim.backward(10)


screen = t.Screen()
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="s", fun=move_backwards)
screen.exitonclick()
