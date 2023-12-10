import random
from hangman_word_list import word_list
from hangman_art import hangman_logo, hangman_stages
import os



print(hangman_logo)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

end_of_game = False
chosen_word = random.choice(word_list).lower()
word_length = len(chosen_word)

lives = 6

print(f"The chosen word is {chosen_word}")

display = ["_"] * word_length

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    clear_screen()

    if guess in display or guess == ' ':
        print(f"You've already guessed {guess}")
        continue

    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        print(f"You guessed {guess}, that is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
        else:
            print(f"Lives remaining: {lives}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win!")

    print(hangman_stages[lives])
