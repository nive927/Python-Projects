from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.color("white")
        # The mode must be "user" for the changes to appear onscreen
        # turtle.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)