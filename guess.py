from random import randint
NUMBER = randint(1, 100)
EASY_GUESSES = 10
HARD_GUESSES = 5

def start():
    print("Welcome to Number Guessing Game!")
    print("Im thinking of a number between 1 and 100")

    difficulty = input("Choose a diffuclty. Type 'easy'or 'hard': ").lower()
    while difficulty not in ["easy", "hard"]:
        difficulty = input("Please type either easy or hard: ").lower()


    if difficulty == "easy":
        guesses = EASY_GUESSES
    else:
        guesses = HARD_GUESSES


    print(f"You have {guesses} attempts to guess the number!\n")
    return guesses


def guess_game():
    guesses = start()
    attempt = 0

    while attempt != NUMBER:

        while True:
            try:
                attempt = int(input("Make a Guess: "))
                break
            except ValueError:
                print("Please enter a number!\n")


        if NUMBER > attempt:
            guesses -= 1
            print("Too Low.")
            print("Guess Again.")
            print(f"You have {guesses} attempts to guess the number.\n")

        elif NUMBER < attempt:
            guesses -= 1
            print("Too High.")
            print("Guess Again.")
            print(f"You have {guesses} attempts to guess the number.\n")
        
        else:
            return f"You win congratulations! The number was {NUMBER}!"


        if guesses <= 0:
            return f"You lost the number was {NUMBER}." 


print(guess_game())