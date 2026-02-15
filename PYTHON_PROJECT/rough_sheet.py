import ascii_art
import game_data
import random
import copy
print(ascii_art.higher_lower_logo)
#Function to generate 2 random data from the game_data list
def generate_random_data():
    """Return two distinct random indices into game_data.data."""
    # random.sample gives two unique indices (no duplicates)
    return random.sample(range(len(game_data.data)), 2)

def comaparison_data(R1,C1,R2,C2):
    print(f"Compare A: {game_data.data[rand_choice1[R1][C1]]['name']}, a {game_data.data[rand_choice1[R1][C1]]['description']} from {game_data.data[rand_choice[R1][C1]]['country']}")
    print(ascii_art.higher_lower_vs_logo)
    print(f"Compare B: {game_data.data[rand_choice1[R2][C2]]['name']}, a {game_data.data[rand_choice1[R2][C2]]['description']} from {game_data.data[rand_choice[R2][C2]]['country']}")
    

def higher_follower_count():
    if game_data.data[rand_choice[0]]['follower_count'] > game_data.data[rand_choice[1]]['follower_count']:
        return  'A'
    elif game_data.data[rand_choice[0]]['follower_count'] < game_data.data[rand_choice[1]]['follower_count']:
        return 'B'
    else:
        return 'C'

rand_choice1 = []
score = 0
rand_choice = generate_random_data()
rand_choice1.append(rand_choice)
# comaparison_data(0,0,0,1)
print(higher_follower_count())
user_input = input("Who has more followers? Type 'A' or 'B': ").upper()

if user_input == higher_follower_count():
    score += 1
    print(f"You're right! Current score: {score}")
    # Append a copy of the current random choice so later modifications won't affect stored entries
    print(rand_choice1)
    rand_choice = generate_random_data()
    rand_choice1.append(rand_choice)
    comaparison_data(0,1,1,0)






