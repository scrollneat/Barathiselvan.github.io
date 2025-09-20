import ascii_art

print(ascii_art.auction_logo)

bidders = {}

print("Welcome to the Secret Auction Programm.")

stop = False
while not stop:
    name = input("What is your name?:  ")
    bid = int(input("What is your Bid: $"))
    bidders[name] =  bid
    print(bidders)
    response = print(input("Are there any more bidders? : Type 'yes' or 'no'.\n").lower())
    if response == 'yes':
        stop = False
    else:
        stop = True