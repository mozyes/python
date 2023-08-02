from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.score = 0
        self.goto(0, 265)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"score: {self.score}", False, "center", FONT)
        self.score += 1

    def game_end(self):
        self.clear()
        self.goto(0, -5)
        self.write(f"Game Over!!!\nTotal score:{self.score}", False, "center", FONT)
        
