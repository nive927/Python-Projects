from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
# Used to turn off animation
# You need manually update any changes required on the screen henceforth
# The screen also requires refreshing
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    # To move the ball at a reasonable pace
    # Increase pace after each paddle hit
    time.sleep(ball.pace)
    # NOTE: Screen Tracer is off prevent animations from showing onscreen
    # Here, we update the screen after performing the necessary turtle movements
    # without the corresponding animations from turning up onscreen
    screen.update()
    ball.move()

    # Detect collision with ball at the top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect contact with the paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect r paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect l paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# To check the screen specifications
# The screen disappears otherwise
screen.exitonclick()
