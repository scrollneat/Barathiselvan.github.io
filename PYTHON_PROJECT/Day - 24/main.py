with open('PYTHON_PROJECT/Day - 24/Input/Letters/starting_letters.txt', 'r') as let:
    letter = let.read()
    print(letter)

with open('PYTHON_PROJECT/Day - 24/Input/Names/invited_names.txt', 'r') as names:
    invited_names = names.readlines()

for i in invited_names:
    new_invited_names = i.strip("\n")
    with open(f"PYTHON_PROJECT/Day - 24/Output/ReadyToSend/{new_invited_names}.docx", 'w') as names:
        names.write(letter.replace('[name]', new_invited_names))

