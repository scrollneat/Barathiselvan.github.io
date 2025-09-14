import random
import word_list
import ascii_art


print(ascii_art.logo)
chosen_word = random.choice(word_list.list_of_words)
print(chosen_word)

placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)


game_over = True
lives = 6
# loop_lives = lives -1
list_correct = []
while game_over:
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
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print('***************************You lost and You have been hanged***************************')
            game_over = False
    if "_" not in display:
        print("***************************You won the game***************************")
        game_over = False
    print(f"Lives left {lives}")
    print(ascii_art.HANGMANPICS[lives])


for i in chosen_word:
  for j in range(len(guess)):
        if i == guess[j]:
            print("Right")
            break
        else:
            print("Wrong")
        
