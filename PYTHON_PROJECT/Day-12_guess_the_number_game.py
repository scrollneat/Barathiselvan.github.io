import ascii_art
import random

print(ascii_art.guess_game_logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")

def comp_num_generator():
    list_of_num = []
    for i in range(1,101):
        list_of_num.append(i)
    return random.choice(list_of_num)

computer_num = comp_num_generator()