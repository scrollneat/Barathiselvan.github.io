resource = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0
}

coffee = {
    "espresso" : {
       "Water": 50,
       "Coffee": 18
    },
    "latte" : {
       "Water": 200,
       "Milk": 150,
       "Coffee": 24
    },
    "cappuccino" : {
       "Water": 250,
       "Milk": 100,
       "Coffee": 24
    }
}

def in_stock(user_need):
    if coffee[user_need]["Water"] >= resource["Water"]:
        return "Water"
    elif coffee[user_need]["Coffee"] >= resource["Coffee"]:
        return "Coffee"
    elif coffee[user_need]["Milk"] >= resource["Milk"]:
        return "Milk"
    else:
        return True
def calculate_money(quarters, dimes, nickles, penny):
    if (((0.25*quarters)+(0.1*dimes)+(0.05*nickles)+(0.01*penny))


power = True
while power:
    user_input = input(f"What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == 'report':
        for key, value in resource.items():
         if key == 'Money':
            print(f"{key}: ${value}")
         elif key == 'Coffee':
            print(f"{key}: {value}g")
         else:
            print(f"{key}: {value}ml")
    elif in_stock(user_input) == True:
        Quarters = input("Please insert the coins: \nHow many Quarters?: ") 
        Dimes = input("How many Dimes?: ")
        Nickles =input("How may Nickles?: ")
        Pennies = input("How many Pennies?:")
        calculate_money(Quarters, Dimes, Nickles, Pennies)
                   


    elif user_input == 'off':
       power = False
       print(f"Coffee Machine is under Maintenance!")

