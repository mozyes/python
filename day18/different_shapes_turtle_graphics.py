import turtle as T
import random

timmy = T.Turtle()

colours = ["red", "green", "blue"]

for i in range(3, 11):
    timmy.color(random.choice(colours))
    for j in range(0, i):
        timmy.forward(100)
        timmy.right(360/i)

screen = T.Screen()
screen.exitonclick()
