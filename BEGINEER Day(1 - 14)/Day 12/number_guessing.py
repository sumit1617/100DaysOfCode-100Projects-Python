from random import randint
from art import logo
import os


def clear():
    return os.system("cls")

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def game():
    print(logo)
    # Choosing a randeom number betwwen 1 to 100
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 to 100")
    answer = randint(1, 100)

    # Make funtion to set difficulty
    def set_difficulty():
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if level == "easy":
            return EASY_LEVEL_TURNS
        else:
            return HARD_LEVEL_TURNS


    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong
    guess = 0
    # Track the number of turn's and reduce by 1 if they get it wrong.
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number.
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"You run out of guesses. You loose")
            return
        elif guess != answer:
            print("Guess again.")

while input("Do you want to play a game again? Type 'y' or 'n':  ") == "y":
    clear()
    game()
