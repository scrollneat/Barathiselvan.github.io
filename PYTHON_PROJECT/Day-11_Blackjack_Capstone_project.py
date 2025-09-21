import ascii_art
import random
    
def deal_Card():
    card = random.choice(card_deck)
    return card

def calculate_score(Cards):
    sum(Cards)
    if sum(Cards) == 21 and len(Cards) == 2:
        return 0
    if sum(Cards) > 21 and 11 in Cards:
        Cards.remove(11)
        Cards.append(1)
    return sum(Cards)
def draw():
    print(f'''    Your Final Hand: {Your_Cards}, Final Score: {Your_score} 
    Computer Final Hand: {Computer_Cards}, Final Score: {Computer_Score} 
    It is a Draw''')
def win():
    print(f'''    Your Final Hand: {Your_Cards}, Final Score: {Your_score} 
    Computer Final Hand: {Computer_Cards}, Final Score: {Computer_Score} 
    You Win!''')   
def lose():
    print(f'''    Your Final Hand: {Your_Cards}, Final Score: {Your_score} 
    Computer Final Hand: {Computer_Cards}, Final Score: {Computer_Score} 
    You Lose!''')

def compare(user_score, com_score):
    if user_score == com_score:
        return draw()
    elif com_score == 0 or user_score > 21:
        return lose()
    elif user_score == 0 or com_score > 21:
        return win()  
    else:
        if user_score > com_score:
            return win()   
        else:
            return lose()
        
new_game = True
while new_game:
    print(ascii_art.black_jack_logo)

    card_deck = [2,3,4,5,6,7,8,9,10,10,10,10,11]

    random.shuffle(card_deck)
    random.shuffle(card_deck)


    Your_Cards = []
    Computer_Cards = []
    Your_score = -1
    Computer_Score = -1

    game_over = False

    for i in range(2):
        Your_Cards.append(deal_Card())
        Computer_Cards.append(deal_Card())

    while not game_over:
        Your_score = calculate_score(Your_Cards)
        Computer_Score = calculate_score(Computer_Cards)

        print(f"         Your Cards: {Your_Cards}, Current Score: {Your_score}")
        print(f"         Computer First card: {Computer_Cards[0]} ")


        if  Your_score == 0 or Computer_Score == 0 or Your_score > 21 :
            game_over = True
        else:   
            game_over = False
            user_response = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_response == 'y':
                Your_Cards.append(deal_Card())
            else:
                game_over = True

    while Computer_Score != 0 and Computer_Score < 17:
        Computer_Cards.append(deal_Card())
        Computer_Score = calculate_score(Computer_Cards)


    compare(Your_score, Computer_Score)

    user2_response = input("If You want to restart the game: Type 'y', Type 'n' to quit: ").lower()

    if user2_response == 'y':
        new_game = True
        print("\n"*1000)
    else: 
        new_game = False
