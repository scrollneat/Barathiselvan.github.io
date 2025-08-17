import random
rock = '''
Rock

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
Paper

     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list_of_play = [rock, paper, scissors]
welcome_var = int(input("What do you Want to Choose? Type 0 for Rock or, 1 for Paper or, 2 for Scissors.\n"  ))
your_hand = list_of_play[welcome_var]
computer_hand = random.choice(list_of_play)
print(f"Your Hand is {your_hand}")
print(f"Computer Hand is {computer_hand}")


if your_hand == computer_hand:
    print("It's a Tie! Play Again!")
elif your_hand == rock:
    if computer_hand == paper:
        print("You Lose! Computers are going to take over the World")
    else:
        print("You Win! You have Proved Human brain is better than Computer")
elif your_hand == paper:
    if computer_hand == scissors:
        print("You Lose! Computers are going to take over the World")
    else:
        print("You Win! You have Proved Human brain is better than Computer")
elif your_hand == scissors:
    if computer_hand == paper:
        print("You Win! You have Proved Human brain is better than Computer")
    else:
        print("You Lose! Computers are going to take over the World")
elif computer_hand == paper:
    if your_hand == rock:
        print("You Lose! Computers are going to take over the World")
    else:
        print("You Win! You have Proved Human brain is better than Computer")
elif computer_hand == rock:
    if your_hand == scissors:
        print("You Lose! Computers are going to take over the World")
    else:
        print("You Win! You have Proved Human brain is better than Computer")
elif computer_hand == scissors:
    if your_hand == paper:
        print("You Lose! Computers are going to take over the World")
    else:
        print("You Win! You have Proved Human brain is better than Computer")
else:
    print("Your input is wrong")

