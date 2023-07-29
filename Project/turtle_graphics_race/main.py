from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = (screen.textinput("Make your bet", "Which turtle will win the race?\nEnter a turtle_color: ").
            lower())
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []

i = 0
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-225, 180 - i)
    i += 67
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for color_turtle in all_turtle:
        if color_turtle.xcor() > 230:
            is_race_on = False
            winning_color = color_turtle.pencolor()
            if winning_color == user_bet:
                print("You have won!. {winning_color} turtle won the race. ")
            else:
                print(f"You have lost! {winning_color} turtle won the race. ")
        rand_distance = random.randint(0, 10)
        color_turtle.forward(rand_distance)

screen.exitonclick()
