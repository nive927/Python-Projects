from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.penup()
        self.go_to_start()

    def go_to_start(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_fd(self):
        self.fd(MOVE_DISTANCE)

    def crossed_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False

