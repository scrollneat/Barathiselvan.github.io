import ascii_art
import game_data
import random
print(ascii_art.higher_lower_logo)
#Function to generate 2 random data from the game_data list
def generate_random_data():
    """Return two distinct random indices into game_data.data."""
    # random.sample gives two unique indices (no duplicates)
    return random.sample(range(len(game_data.data)), 2)

def comaparison_data(A,B):
    print(f"Compare A: {game_data.data[rand_choice[A]]['name']}, a {game_data.data[rand_choice[0]]['description']} from {game_data.data[rand_choice[A]]['country']}")
    print(ascii_art.higher_lower_vs_logo)
    print(f"Compare B: {game_data.data[rand_choice[B]]['name']}, a {game_data.data[rand_choice[1]]['description']} from {game_data.data[rand_choice[B]]['country']}")

def higher_follower_count():
    if game_data.data[rand_choice[0]]['follower_count'] > game_data.data[rand_choice[1]]['follower_count']:
        return  'A'
    elif game_data.data[rand_choice[0]]['follower_count'] < game_data.data[rand_choice[1]]['follower_count']:
        return 'B'
    else:
        return 'C'

rand_choice = generate_random_data()
comaparison_data(0,1)
print(higher_follower_count())
user_input = input("Who has more followers? Type 'A' or 'B': ").upper()

if user_input == higher_follower_count():
    i =+ 1
    print(f"You're right! Current score: {i}")
    rand_choice = generate_random_data()
    comaparison_data(1,rand_choice[0])



    
        