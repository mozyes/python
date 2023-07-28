import turtle as t
import random

degree = [0, 90 , 180, 270]
tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b # also can do rand_color = (r,g,b) and return rand_color
def walk():
    tim.pensize(5)
    tim.forward(20)
    tim.setheading(random.choice(degree))

i = 0
while i <= 200:
    r1, g1, b1 = random_color() #can omit this with the above method
    tim.color(r1, g1, b1) # here with above different method i can directly use tim.color(random_color())
    walk()
    i +=1

screen = t.Screen()
screen.exitonclick()
