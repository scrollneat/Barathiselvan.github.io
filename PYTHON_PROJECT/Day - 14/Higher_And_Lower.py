#display ascii art
from ascii_art import higher_lower_logo, higher_lower_vs_logo
from game_data import data
from random import randint

#Generate the random account from the game data 
def random_number():
    return  randint(0, 57)

#formatting the random account details
def format_Sentence(account):
    account_name = data[account]['name']
    accoutn_description = data[account]['description']
    account_country = data[account]['country']
    return f"{account_name}, a {accoutn_description}, from {account_country}."

def high_follower_count(a, b):
    if data[a]['follower_count'] > data[b]['follower_count'] :
        return 'A'
    elif data[a]['follower_count'] < data[b]['follower_count'] :
        return 'B'
    else:
        return False
print(higher_lower_logo)   
account_a = random_number()
account_b = random_number()
if account_a == account_b:
    account_b = random_number()
print(f"Compare A: {format_Sentence(account_a)}")
print(higher_lower_vs_logo)
print(f"Against B: {format_Sentence(account_b)}")
#ask for user input
user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
print('\n'*200)
print(higher_lower_logo)
#calculate who has more followers count

score = 0
game_over = True
random_account = []

while game_over:
    if high_follower_count(account_a, account_b) == user_input:
        score += 1
        print(f"You're right! Current score: {score}")
        account_a = account_b
        print(f"Compare A: {format_Sentence(account_a)}")
        print(higher_lower_vs_logo)
        account_b = random_number()
        if account_a == account_b:
            account_b = random_number()
        print(f"Against B: {format_Sentence(account_b)}")
        user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
        print('\n'*200)
        print(higher_lower_logo)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = False

