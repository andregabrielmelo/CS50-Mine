import sys
import random

def main():

    # Get level
    while True:
        # Try to get a positive integer
        try:
            level = input("Level: ")
            level = int(level)
            if level < 1:
                raise ValueError
        except ValueError:
            pass
        else:
            break

    # Generate guess, random integer between 1 and level
    computer_number = random.randint(1, level)

    # Keep the user guessing until the guess is right  
    while True:
        # Try getting the guess
        try:
            # Get user guess
            guess = input("Guess: ")
            guess = int(guess)

            # Verify if guess and answer is equal
            if guess < computer_number:
                print("Too small!")
            elif guess > computer_number:
                print("Too large!")
            else:
                sys.exit("Just right!")
    
        except ValueError:
            pass


main()