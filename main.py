import turtle

import pandas
import pandas as pd


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
print(all_states)
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title= f"Guess the State{len(guessed_states)}/50", prompt="What's another state's name?")
    if answer_state.upper() in [state.upper() for state in all_states]:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        guessed_states.append(state_data.state.item())

        print(answer_state.upper())







screen.exitonclick()