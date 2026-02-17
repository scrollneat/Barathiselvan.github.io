import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print("Welcome to the PyPassword Generator!")
input_letters= int(input(f"How many letters would you like in your password?\n")) 
input_numbers = int(input(f"How many numbers would you like?\n"))
input_symbols = int(input(f"How many symbols would you like?\n"))

#using functions
# r1 = random.choices(letters, k=input_letters) 
# r2 = random.choices(symbols, k=input_symbols)
# r3 = random.choices(numbers, k=input_numbers)
let = []
for i in range (input_letters):
  let.append(random.choice(letters))
for i in range (input_numbers):
  let.append(random.choice(numbers))
for i in range (input_symbols):
  let.append(random.choice(symbols))

random.shuffle(let)

password = ""
for i in let:
  password += i
print(password)
