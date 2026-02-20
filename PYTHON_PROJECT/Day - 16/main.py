from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

power_on = True
while power_on:
    options = menu.get_items()
    user_input = input(f'What would you like? ({options}): ')
    if user_input == 'report':
        coffee_maker.report()
        money_machine.report()
    elif user_input == 'off':
        print("The Machine is under Maintanence!")
        power_on = False
    else:
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        

