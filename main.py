import turtle
from turtle import Screen
import pandas
#
screen = Screen()
screen.title("us_states_game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput("Guess a State", prompt="What's another state's name")

data = pandas.read_csv("50_states.csv")
print(data)


print(data[data.x )

# screen.mainloop()