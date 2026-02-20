from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu_items = MenuItem('name','ingredients' ,'cost')
menu = Menu()
user_input = input('What would you like? (espresso/latte/cappuccino): ')
coffee_maker.is_resource_sufficient(menu_items.name)
# power_on = True
# while power_on:
#     user_input = input('What would you like? (espresso/latte/cappuccino): ')
#     if user_input == 'report':
#         coffee_maker.report()
#         money_machine.report()

#     if coffee_maker.is_resource_sufficient(menu_items.user_input):

#     elif user_input == 'off':
#         print("The Machine is under Maintanence!")
#         power_on = False
