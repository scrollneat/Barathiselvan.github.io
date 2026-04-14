import turtle

screen = turtle.Screen()

screen.title("US. States Game")
image = "PYTHON_PROJECT/Day - 25/Day - 25_US_States_Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer = screen.textinput(title = "Guess the state", prompt = "What's another state's name?")


turtle.mainloop()
