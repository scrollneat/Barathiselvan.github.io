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

user_reponse = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if user_reponse == 'easy':
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess_number = input("Make a guess: ")
    if guess_number == computer_num:
        print(f"You got it! The answer was {computer_num}.")
    else:
        while guess_number != computer_num and attempts == 0:
            