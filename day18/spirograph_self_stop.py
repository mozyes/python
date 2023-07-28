#note : i need to import as small letter.

import turtle as t
import random

degree = [0, 90, 180, 270]
tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


def circle(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


circle(10)

screen = t.Screen()
screen.exitonclick()
