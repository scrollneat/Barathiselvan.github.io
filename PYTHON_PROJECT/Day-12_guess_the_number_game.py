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

def game_funciton(lives):
    game_over = True
    while game_over:
        if lives >= 1:
            print(f"You have {lives} attempts remaining to guess the number.")
            user_number = int(input("Make a guess: "))
            if user_number == computer_number  and lives != 0:
                print(f"You got it! The answer was {computer_number}.")
                game_over = False
            elif (user_number != computer_number) and (lives >= 1):
                l_h_output = low_high(user_number, computer_number)
                if l_h_output == 1:
                    lives -= 1
                    print(f"Too high.\nGuess again.\n")
                elif l_h_output == 0:
                    lives -= 1
                    print(f"Too low.\nGuess again.\n")
        else:
            print(f"Oops! You ran out of guesses.\nYou lost better luck next time!\n")
            game_over = False

def mode_select():
    user_reponse = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if user_reponse == 'easy':
        lives = 10
        game_funciton(lives)
    elif user_reponse == 'hard':
        lives = 5
        game_funciton(lives)  
    else:
        print(f"Select the Correct difficulty level. Type 'easy' or 'hard':  ")
        mode_select()

mode_select()


