import random
word_list = ["python", "java", "kotlin", "javascript"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)


game_over = False
list_correct = []
while not game_over:
    display = ""
    guess = input("Guess a letter otherwise you will be hanged: ").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display += chosen_word[i]
            list_correct.append(guess)
        elif chosen_word[i] in list_correct:
             display += chosen_word[i]
        else:
            display += "_"
    print(display)
    if "_" not in display:
        print("You won the game")
        game_over = True

for i in chosen_word:
  for j in range(len(guess)):
        if i == guess[j]:
            print("Right")
            break
        else:
            print("Wrong")
        
