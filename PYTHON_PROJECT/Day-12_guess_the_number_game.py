import ascii_art
import random

print(ascii_art.guess_game_logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")

def comp_num_generator():
    list_of_num = []
    for i in range(1,101):
        list_of_num.append(i)
    return random.choice(list_of_num)

computer_number = comp_num_generator()

def low_high(u_num, com_num):
    if u_num > com_num:
        return 1
    else:
        return 0

def game_funciton(attempts, guess_number, computer_num):
    if guess_number == computer_num:
        print(f"You got it! The answer was {computer_num}.")
    else:
        while guess_number != computer_num and attempts != 0:
            l_h_output = low_high(guess_number, computer_num)
            if l_h_output == 1:
                attempts -= 1
                print(f"Too high.\nGuess again.\nYou have {attempts} attempts remaining to guess the number.\n")
            else:
                attempts -= 1
                print(f"Too low.\nGuess again.\nYou have {attempts} attempts remaining to guess the number.\n")
        if guess_number == computer_num:
            print(f"You got it! The answer was {computer_num}.")

    
user_reponse = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if user_reponse == 'easy':
    lives = 10
    print(f"You have {lives} attempts remaining to guess the number.")
    user_number = input("Make a guess: ")
    game_funciton(lives, user_number, computer_number)

elif user_reponse == 'hard':
    lives = 5
    print(f"You have {lives} attempts remaining to guess the number.")
    user_number = input("Make a guess: ")
    game_funciton(lives, user_number, computer_number)