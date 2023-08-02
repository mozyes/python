from turtle import Turtle
INITIAL_LOCATION = (0, -280)
MOVEMENT_LENGTH = 20


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.left(90)
        self.goto(INITIAL_LOCATION)

    def move_up(self):
        self.forward(MOVEMENT_LENGTH)

    def move_down(self):
        self.backward(MOVEMENT_LENGTH)

    def player_reset(self):
        self.goto(INITIAL_LOCATION)
        
