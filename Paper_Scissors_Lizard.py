# Rock- Paper- Lizard -Spock program
import random


# The idea is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0- rock
# 1- Spock
# 2- paper
# 3- lizard
# 4- scissors

# helper function

# assign name to given number
def number_to_name(number):
    switcher = {0: "rock", 1: "Spock", 2: "paper", 3: "lizard"}
    return switcher.get(number, "scissors");


# assign the number to given name
def name_to_number(name):
    switcher = {"rock": 0, "Spock": 1, "paper": 2, "lizard": 3}
    return switcher.get(name, 4)


def gamePlay(player_choice):
    # print a blank line to separate consecutive games
    print("")

    # print out the message for the player's choice
    print("Player chooses: " + player_choice)

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for computer_number using random.randrange()
    computer_number = random.randrange(0, 5)

    # convert the computer number to name using the function number_to_name()
    computer_choice = number_to_name(computer_number)

    # print out the message for computer's choice
    print("Computer chooses: " + computer_choice)

    # compute difference of computer_number and player_number modulo five
    difference = ((player_number - computer_number) % 5)

    print("Difference: ", difference)
    # determine winner, print winner message
    if (difference == 1 or difference == 2):
        print("Player wins!")
    elif difference == 3 or difference == 4:
        print("Computer wins!")
    else:
        print("Player and computer ties!")
    return ""


if __name__ == '__main__':
    gamePlay("rock")

    print(-1 % 5)
