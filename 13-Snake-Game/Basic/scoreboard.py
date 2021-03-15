from turtle import Turtle

ALIGNMENT = "center"
FONT = "Arial"
FONT_SIZE = 24
FONT_STYLE = "normal"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write_on_screen(f"Score: {self.score}")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_on_screen(f"Score: {self.score}")

    def write_on_screen(self, text):
        self.write(text, align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_STYLE))

    def game_over(self):
        self.goto(0, 0)
        self.write_on_screen("GAME OVER.")
