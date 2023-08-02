from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_speed = 0.1

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)

        # Set the new car's starting position to be different from the existing cars
        y_position = random.randint(-250, 250)
        new_car.goto(300, y_position)

        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.move_speed *= 0.9
