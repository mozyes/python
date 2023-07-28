import turtle as t

timmy = t.Turtle()
for i in range(1, 100):
    if i % 4 != 0:
        timmy.pendown()
        timmy.forward(1)
    else:
        timmy.penup()
        timmy.forward(1)


screen = t.Screen()
screen.exitonclick()
