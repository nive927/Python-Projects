from turtle import Turtle

ALIGNMENT = "center"
FONT = "Arial"
FONT_SIZE = 24
FONT_STYLE = "normal"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", mode="r") as f:
            self.high_score = int(f.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_STYLE))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
