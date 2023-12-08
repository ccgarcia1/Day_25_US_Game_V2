import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

df = pandas.read_csv("50_states.csv")
types = [df['{0}'.format(i)].dtype for i in df.columns]
#print(types)
# print(all_states)
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title= f"Guess the State{len(guessed_states)}/50", prompt="What's another state's name?").upper()
    if answer_state == "EXIT":
        #keeping the track of the missing states
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states")
        break
    if answer_state in [state.upper() for state in all_states]:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state.str.upper() == answer_state]
        #print(state_data.state + ' ' + str(state_data.y))
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        guessed_states.append(state_data.state.item())

