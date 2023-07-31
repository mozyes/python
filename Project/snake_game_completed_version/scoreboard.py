from turtle import Turtle
ALIGNMENT = "center"
FONT = ("areal", 30, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.player_score = 0
        self.penup()
        self.goto(0, 260)
        self.score_calc()

    def score_calc(self):
        self.clear()
        self.write(f"Score: {self.player_score}", False, ALIGNMENT, FONT)
        self.player_score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)
