resource = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0
}

coffee = {
    "espresso" : {
    "ingredients" : {
       "Water": 50,
       "Coffee": 18,
    },
    "cost" : 1.5,
    },
    "latte" : {
    "ingredients" : {   
       "Water": 200,
       "Milk": 150,
       "Coffee": 24,
    },
    "cost" : 2.5,
    },
    "cappuccino" : {
    "ingredients" : {  
       "Water": 250,
       "Milk": 100,
       "Coffee": 24,
    },
    "cost" : 3,
}}

def in_stock(user_need):
    if coffee[user_need]["ingredients"].get("Water",0) >= resource["Water"]:
        return "Water"
    elif coffee[user_need]["ingredients"].get("Coffee",0) >= resource["Coffee"]:
        return "Coffee"
    elif coffee[user_need]["ingredients"].get("Milk",0) >= resource["Milk"]:
        return "Milk"
    else:
        return True
def calculate_money(quarters, dimes, nickles, penny):
    return ((0.25*quarters)+(0.1*dimes)+(0.05*nickles)+(0.01*penny))

def update(user_input, key):
    resource.update({key: (resource.get(key)) - (coffee[user_input]["ingredients"].get(key))})

def print_Report():
    for key, value in resource.items():
            if key == 'Money':
                print(f"{key}: ${value}")
            elif key == 'Coffee':
                print(f"{key}: {value}g")
            else:
                print(f"{key}: {value}ml")

power = True
while power:
    user_input = input(f"What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == 'report':
        print("----------------Report-----------------")
        print_Report()
        print("------------------END------------------")
    elif user_input == 'off':
        power = False
        print(f"Coffee Machine is under Maintenance!")
    else:
        if in_stock(user_input) != True :
            print(f"Sorry there is not enough {in_stock(user_input)}.")
        elif in_stock(user_input) == True:
            Quarters = int(input("Please insert the coins: \nHow many Quarters?: ")) 
            Dimes = int(input("How many Dimes?: "))
            Nickles =int(input("How may Nickles?: "))
            Pennies = int(input("How many Pennies?:"))
            user_money = calculate_money(Quarters, Dimes, Nickles, Pennies)
            if user_money < coffee[user_input].get("cost"):
                print("Sorry that's not enough money. Money refunded.")
            else:
                resource.update({"Money": coffee[user_input].get("cost")})
                if user_money > coffee[user_input].get("cost"):
                    print(f"Here is ${round((user_money - coffee[user_input].get("cost")),2)} dollars in change.")
                for key in (coffee[user_input].get("ingredients")).keys():
                    update(user_input, key)
                print(f"Here is your {user_input}☕. Enjoy!")

    

