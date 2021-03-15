import turtle
import random

screen = turtle.Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle do you want to bet on? Enter a color: ")
is_race_on = False
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
competing_turtles = list()

for turtle_index in range(6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(rainbow_colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    competing_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in competing_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle_color = turtle.pencolor()
            if winning_turtle_color == user_bet:
                print(f"You've won! The {winning_turtle_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_turtle_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
