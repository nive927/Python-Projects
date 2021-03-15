from turtle import Turtle
MOVE_AMT = 10
BALL_PACE = 0.1


class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.shape("circle")
        self.penup()

        self.x_move = MOVE_AMT
        self.y_move = MOVE_AMT
        self.pace = BALL_PACE

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # To reverse the ball direction when it hits the top screen or bottom
        self.y_move *= -1

    def bounce_x(self):
        # To reverse the ball direction when it hits the paddle
        self.x_move *= -1
        # Increase speed of ball when it hits paddle
        self.pace *= 0.9

    def reset_position(self):
        self.home()
        # To get the ball to reset to the original pace after each point
        self.pace = BALL_PACE
        self.bounce_x()