import turtle
from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("us_states_game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# answer_state = screen.textinput("Guess a State", prompt="What's another state's name").title()

data = pandas.read_csv("50_states.csv")
state_list = (data.state).tolist()
print(state_list)


def create_turtle(x, y, input):
    new_turtle = Turtle(visible=False)
    new_turtle.penup()
    new_turtle.goto(x, y)
    new_turtle.speed("fastest")
    new_turtle.write(input, align="center", font=("Arial", 12, ""))


guess_list = []
remaining_states_list = []
while len(guess_list) < 50:

    answer_state = turtle.textinput(f"{len(guess_list)}/50 States Correct", prompt="What's another state's name").title()

    if answer_state == "Exit":
        remaining_states_list = [state for state in state_list if state not in guess_list]
        new_data = pandas.DataFrame(remaining_states_list)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list:
        guess_list.append(answer_state)
        state_data = data[data.state == answer_state]
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)
        create_turtle(x_cor, y_cor, answer_state)



