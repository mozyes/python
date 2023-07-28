import turtle as T
import random

degree = [0, 90 , 180, 270]
tim = T.Turtle()
tim.speed("fastest")
T.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r,g,b)
    return rand_color

def circle():
    tim.circle(100)
    current_heading = tim.heading()
    tim.setheading(current_heading + 10)

i = 0
while i <= 200:
    tim.color(random_color())
    circle()
    i +=1

screen = T.Screen()
screen.exitonclick()
