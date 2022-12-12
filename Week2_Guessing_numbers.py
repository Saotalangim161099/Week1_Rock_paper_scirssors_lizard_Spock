import math
import random

num_range = 100
guesses_remaining = 0
secret_number = 0


# helper function to start and restart the game
def new_game():
    # initialize the global variables used in your code here
    global num_range, guesses_remaining, secret_number
    guesses_remaining = int(math.ceil(math.log((num_range - 0), 2)))
    secret_number = random.randrange(0, num_range)
    print("\nNew game. Range is from 0 to ", num_range)
    print
    "Number of remainning guesses is ", guesses_remaining


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global num_range
    num_range = 100
    new_game()


def range1000():
    # button that changes the range to [0,1000) and start a new game
    global num_range
    num_range = 1000
    new_game()


def input_guess(guess):
    global guesses_remaining
    print("\nGuess was: " + guess)
    guess = int(guess)
    guesses_remaining -= 1
    print("Number of remaining guesses is: " + guesses_remaining)

    # main logic goes here
    if (guesses_remaining > 0):
        if (guess > secret_number):
            print("Lower")
        elif guess < secret_number:
            print("Higher")
        else:
            print("Correct!")
            new_game()
    else:
        if guess == secret_number:
            print("Correct!")
        else:
            print("You ran out of guesses. The number was ", secret_number)
        new_game()


if __name__ == '__main__':
    print("You're", 6)
