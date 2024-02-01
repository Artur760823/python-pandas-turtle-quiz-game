import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. Sates Game")

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("./50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    for state in all_states:
        if answer_state.lower() == state.lower():
            guessed_states.append(answer_state)
            new_state_name = turtle.Turtle()
            new_state_name.hideturtle()
            new_state_name.penup()
            state_data = data[data.state == state]
            new_state_name.goto(int(state_data["x"]), int(state_data["y"]))
            new_state_name.write(state, align="center", font=("Arial", 10, "normal"))


