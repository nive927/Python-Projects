#####Turtle Intro######

import turtle
import random

tim = turtle.Turtle()
tim.shape("turtle")
tim.color("red")

# ######## Challenge 1 - Draw a Square ############
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# ########### Challenge 2 - Draw a Dashed Line ########
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# ########### Challenge 3 - Draw different polygons with different colors ########

# colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]
# for sides in range(4, 11):
#     poly_angle = 360 / sides
#     tim.pencolor(random.choice(colors))
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(poly_angle)

# ########### Challenge 4 - Generate a Random Walk ########
#
# colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]
# directions = [0, 90, 180, 270]
#
# tim.speed("fastest")
# tim.pensize(10)
#
# for _ in range(200):
#     tim.pencolor(random.choice(colors))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# ########### Challenge 5 - Generate a Random Walk but with RGB colors########
# turtle.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     r_color = (r, g, b)
#     return r_color
#
# directions = [0, 90, 180, 270]
#
# tim.speed("fastest")
# tim.pensize(10)
#
# for _ in range(200):
#     tim.pencolor(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

########## Challenge 6 - Spirograph########

turtle.colormode(255)

tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_color = (r, g, b)
    return r_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)


### DON'T MODIFY THIS CODE ####
screen = turtle.Screen()
screen.exitonclick()
