# colorgram to take color from the image. had to install colorgram from pypi.org

# import colorgram
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

# colors = colorgram.extract('image.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors. append(new_color)

color_list = [(192, 165, 115), (138, 166, 190), (56, 102, 140), (141, 91, 50), (12, 23, 55), (222, 207, 123),
              (182, 154, 42), (61, 22, 11), (182, 146, 165), (142, 177, 151), (72, 117, 81), (58, 15, 26),
              (126, 79, 102), (130, 30, 16), (15, 39, 23), (24, 53, 127), (177, 188, 215), (164, 104, 134),
              (115, 31, 46), (97, 150, 100), (98, 121, 172), (210, 178, 197), (174, 105, 93), (74, 150, 165),
              (25, 91, 65), (172, 205, 180)]

tim.speed("fastest")
tim.penup()
tim.setheading(218)
tim.forward(300)
tim.setheading(0)


def spot():
    initial_position = tim.pos()[0]
    for i in range(10):
        for j in range(10):
            tim.pendown()
            rand_color = random.choice(color_list)
            tim.color(rand_color)
            tim.dot(20)
            tim.penup()
            tim.goto(tim.pos()[0] + 50, tim.pos()[1])
        tim.goto(initial_position, tim.pos()[1] + 50)


spot()
screen = t.Screen()
screen.exitonclick()
