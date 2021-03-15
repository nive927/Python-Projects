from turtle import Screen
import time
import snake
from food import Food
from scoreboard import ScoreBoard

WALL_X = 300
WALL_Y = 300

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

my_snake = snake.Snake()
my_food = Food()
my_score = ScoreBoard()

screen.listen()
screen.onkey(my_snake.up, key="Up")
screen.onkey(my_snake.down, key="Down")
screen.onkey(my_snake.left, key="Left")
screen.onkey(my_snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    # Detecting collision with food
    if my_snake.head.distance(my_food) < 15:
        my_food.refresh()
        my_snake.extend()
        my_score.increase_score()

    # Detect collision with wall
    if my_snake.head.xcor() > WALL_X or my_snake.head.xcor() < -WALL_X \
            or my_snake.head.ycor() > WALL_Y or my_snake.head.ycor() < -WALL_Y:
        game_is_on = False
        my_score.game_over()

    # Detect collision with tail for all segments that is not the head
    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 10:
            game_is_on = False
            my_score.game_over()

screen.exitonclick()
