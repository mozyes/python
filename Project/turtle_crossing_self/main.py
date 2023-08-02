from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
import random
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player_one = Player()
car = CarManager()
score = ScoreBoard()

screen.listen()
screen.onkey(player_one.move_up, "Up")
screen.onkey(player_one.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(car.move_speed)
    screen.update()
    car.move_cars()
    if player_one.ycor() > 280:
        # resets player back to initial position and updates score and also increases speed of car!
        player_one.player_reset()
        score.score_update()
        car.increase_speed()
    if random.random() < 0.1:
        car.create_car()
    for num_cars in car.cars:
        if player_one.distance(num_cars) < 17:
            # collision detection. doesn't feel as smooth though
            score.game_end()
            game_is_on = False


screen.exitonclick()
