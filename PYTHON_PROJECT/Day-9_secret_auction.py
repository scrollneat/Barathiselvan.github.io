import ascii_art


def highest_bidder(bidding_list):
    max_bid = 0
    winner = ''
    for i in bidding_list:
        bidding_Amount = bidding_list[i]
        if bidding_Amount > max_bid:
            max_bid = bidding_Amount
            winner = i
    print(f"The Highest Bidder is {winner} with the Bid of {max_bid}")

print(ascii_art.auction_logo)

bidders = {}

print("Welcome to the Secret Auction Programm.")

stop = False
while not stop:
    name = input("\nWhat is your name?:  ")
    bid = int(input("What is your Bid: $"))
    bidders[name] =  bid
    response = input("Are there any more bidders? : Type 'yes' or 'no'.\n").lower()
    if response == 'yes':
        stop = False
        print("\n"*1000)
    else:
        stop = True
        print("\n"*1000)
        highest_bidder(bidders)




    