import ascii_art
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

function_call = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}
keep_running = True
while keep_running: 
    print(ascii_art.calculator_logo)
    go_ahead = True
    number1 = float(input("\nWrite your first Number?: "))
    while go_ahead:
        for i in function_call:
            print(i)
        operation = input("Pick you operation: ")
        number2 = float(input("Write your Next Number: "))

        my_function = function_call[operation]
        answer  = my_function(n1 = number1, n2 = number2)
        print(f"{number1} {operation} {number2} = {answer}")

        user_response = input(f"Type 'y' to continue calculating {answer}, or type 'n' to start new calcualation: ").lower()
        if user_response == 'y':
            number1 = answer
            go_ahead = True
        else: 
            go_ahead = False
            print("\n"*1000)
