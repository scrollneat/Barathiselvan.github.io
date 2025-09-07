import random
word_list = ["python", "java", "kotlin", "javascript"]
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)
guess = input("Guess a letter otherwise you will be hanged: ").lower()
display = ""
for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        display += chosen_word[i]
    else:
        display += "_"
print(display)
for i in chosen_word:
  for j in range(len(guess)):
        if i == guess[j]:
            print("Right")
            break
        else:
            print("Wrong")
        
