import turtle
from turtle import Screen, Turtle
import pandas
#
screen = Screen()
screen.title("us_states_game")
screen.setup(width=730, height=500)

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput("Guess a State", prompt="What's another state's name").lower()

data = pandas.read_csv("50_states.csv")
state_list = (data.state).tolist()
print(state_list)


def create_turtle(x, y, input):
    new_turtle = Turtle(visible=False)
    new_turtle.penup()
    new_turtle.goto(x, y)
    new_turtle.speed("fastest")
    new_turtle.write(input, align="center", font=("Arial", 12, ""))

count = 0
game_on = True
while game_on:
    for state in state_list:
        if answer_state == state.lower():
            count += 1
            state_data = data[data.state == state]
            x_cor = int(state_data.x)
            y_cor = int(state_data.y)
            create_turtle(x_cor, y_cor, state)

    answer_state = turtle.textinput(f"{count}/50 States Correct", prompt="What's another state's name").lower()
    if count == 50:
        game_on = False

screen.mainloop()