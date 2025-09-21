import ascii_art
import random
def you_win():
    print(f'''Your final hand:       {Your_Card},    Your_final_score:     {Your_score}
              Computer's final hand: {Computer_Card}, Computer_final_score: {Computer_Score}
               You Win''')

def you_lose():
    print(f'''Your final hand:       {Your_Card},    Your_final_score:     {Your_score}
              Computer's final hand: {Computer_Card}, Computer_final_score: {Computer_Score}
              You Lose!''')
    
print(ascii_art.black_jack_logo)

card_deck = [2,3,4,5,6,7,8,9,10,10,10,10,11]

random.shuffle(card_deck)
random.shuffle(card_deck)

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

Your_Cards = []
Computer_Cards = []

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

while Computer_Score < 17:
    Computer_Cards.append(deal_Card())
    Computer_Score = calculate_score(Computer_Cards)

def compare(user_score, com_score):
    if user_score == com_score:
        return 
    Your_score = calculate_score(Your_Cards)
    Computer_Score = calculate_score(Computer_Cards)

Your_Card = random.sample(card_deck,2)
Your_score = sum(Your_Card)
print(f"         Your Cards: {Your_Card}, Current Score: {Your_score}")

random.shuffle(card_deck)
random.shuffle(card_deck)
Computer_Card = random.sample(card_deck,2)
Computer_Score = sum(Computer_Card)
print(f"         Computer First card: {Computer_Card[0]} ")

if Your_score == 21 or Computer_Score == 21:
    if Your_score == 21 and Computer_Score != 21:
        print(f'''Your final hand:       {Your_Card},    Your_final_score:     {Your_score}
                  Computer's final hand: {Computer_Card}, Computer_final_score: {Computer_Score}
                  You Have BlackJack , Your You Win!''')
    elif Your_score != 21 and Computer_Score == 21:
        print(f'''Your final hand:       {Your_Card},    Your_final_score:     {Your_score}
                  Computer's final hand: {Computer_Card}, Computer_final_score: {Computer_Score}
                  Computer Have BlackJack, You Lose!''')
else:
    if Your_score > 21:
        for i in range(len(Your_Card)):
            if Your_Card[i] == 11:
                Your_Card[i] = 1
                if sum(Your_Card)> 21:
                   you_lose()
                else:
                    user_response = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            else: 
                you_lose()
    else:
        user_response = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    