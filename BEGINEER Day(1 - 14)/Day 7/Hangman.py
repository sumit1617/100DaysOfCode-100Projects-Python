import random
import hangman_logo
import hangman_stages
import hangman_words

end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6
print(hangman_logo.logo)

# Testing a code
print(f"Psst, the chosen word is {chosen_word}")

# Clear blanks
display = []
for _ in range(word_length):
    display += "_"


while not end_of_game:
    guess = input("Guess a letter: ").lower()

# Check guesses letter
    if guess in display:
        print(f"You've already guessed {guess}")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

# Check if the user is wrong.
    if guess not in chosen_word:
        print(f"You gussed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose.")

# Join all the element in the list and turn it into a string
    print(f"{' '.join(display)}") 

    if "_" not in display:
        end_of_game = True
        print("You Win!")

    print(hangman_stages.stages[lives])
    