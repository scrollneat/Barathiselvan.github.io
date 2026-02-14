import ascii_art
import game_data

#Function to generate 2 random data from the game_data list

print(ascii_art.higher_lower_logo)
print(f"Compare A: {game_data.data[0]['name']}, a {game_data.data[0]['description']} from {game_data.data[0]['country']}")
print(ascii_art.higher_lower_vs_logo)
print(f"Compare B: {game_data.data[0]['name']}, a {game_data.data[0]['description']} from {game_data.data[0]['country']}")
user_input = input("Who has more followers? Type 'A' or 'B': ").upper()