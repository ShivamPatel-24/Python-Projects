from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.score = 0
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(0, 270)
        self.write("Score: " + str(self.score), align="center", font=FONT)

    def game_over(self):
        self.score = 0
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

    def update_score(self):
        self.score += 1
        self.display_score()
