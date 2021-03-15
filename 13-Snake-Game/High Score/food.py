from turtle import Turtle
import random


# inheriting from the turtle class
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        # default: 20 X 20 pixels, this makes it 10 X 10 pixel turtle
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")

    def refresh(self):
        random_x = random.randint(-280, 250)
        random_y = random.randint(-280, 250)
        self.goto(random_x, random_y)
