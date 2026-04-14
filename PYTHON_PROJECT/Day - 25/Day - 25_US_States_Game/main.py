import turtle
import pandas as pd
screen = turtle.Screen()
writing = turtle.Turtle()

screen.title("US. States Game")
image = "PYTHON_PROJECT/Day - 25/Day - 25_US_States_Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def mark_in_map(input):
    writing.penup()
    writing.hideturtle()
    writing.goto(data.x[input], data.y[input])
    writing.write(f"{data.state[input]}", align = "center")
    correct_guess.append(data.state[input])

data = pd.read_csv("PYTHON_PROJECT/Day - 25/Day - 25_US_States_Game/50_states.csv")
data = data.state.to_list()

answer = screen.textinput(title = "Guess the state", prompt = "What's another state's name?")
correct_guess = []
if answer in data:
    writing.penup()
    writing.hideturtle()
    state_data = data[data.state == answer]
    writing.goto(state_data.x.item(), state_data.y.item())
    writing.write(answer)



# def guess(ans):
#     for i in range(len(data.state)):
#         if ans.title() == data.state[i]:
#             return True
#         else:
#             return False
             



# for i in range(len(data.state)):
#     answer = screen.textinput(title = "Guess the state", prompt = "What's another state's name?")
#     for i in range(len(data.state)):
#         if guess(answer) == True:
#             mark_in_map(i)
#         else:
#             print("wrong answer")


            

turtle.mainloop()
