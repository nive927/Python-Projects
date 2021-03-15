import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].tolist()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="Enter state name").strip().title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States to learn")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        answer_state_details = data[data.state == answer_state]
        t.goto(int(answer_state_details.x), int(answer_state_details.y))
        t.write(answer_state)

    if len(guessed_states) == 50:
        t.goto(0, 260)
        t.write("You guessed all the states!", font=("Verdana", 20, "normal"), align="center")
        break

screen.exitonclick()




