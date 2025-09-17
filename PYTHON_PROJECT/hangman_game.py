import random
import word_list
# from word_list import list_of_words
import ascii_art


print(ascii_art.logo)
chosen_word = random.choice(word_list.list_of_words)
# print(chosen_word)

placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)


game_over = False
lives = 6
list_correct = []
while not game_over:
    
    guess = input("Guess a letter otherwise you will be hanged: ").lower()
    if guess in list_correct:
        print(f"\nYou have already guessed {guess}\n")
        
    display = ""
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display += chosen_word[i]
            list_correct.append(guess)
        elif chosen_word[i] in list_correct:
             display += chosen_word[i]
        else:
            display += "_"
            
    print(display)
    
    if guess not in chosen_word :
        lives -= 1
        print(f"\nYou have guessed {guess}, that's not in the word.\nYou lose a Life\n")
        if lives == 0:
            print(f"\n***************************It was {chosen_word}. You lost and You have been hanged***************************")
            game_over = True
    if "_" not in display:
        print("\n***************************You won the game***************************")
        game_over = True
    print(f"\nLives left {lives}")
    print(ascii_art.HANGMANPICS[lives])

        
