import turtle as t
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
degree = [0, 90 , 180, 270]

tim = t.Turtle()
def walk():
    tim.color(random.choice(colours))
    tim.pensize(5)
    tim.forward(20)
    tim.setheading(random.choice(degree))

i = 0
while i <= 200:
    walk()
    i +=1

screen = t.Screen()
screen.exitonclick()
