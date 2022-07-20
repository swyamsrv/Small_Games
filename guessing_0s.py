
# #WAP to write a guessing game of ball shuffling
from random import shuffle


def shuffle_list(name_of_list):

    """Here the first function is defined which is shuffling the terms of list"""
    shuffle(name_of_list)
    return name_of_list


def user_guess():

    """This Function is defined to opt user input """
    guess=' '
    while guess not in ['1','2','3']:
        guess = input('Predict any position among 1,2 or 3\n')
    print("You've predicted {}".format(guess))
    return int(guess)


def check_guess(name_of_list, guess):

    """Final function which is used to check whether the user's prediciton is correct or not"""

    if name_of_list[guess-1] == 'O':
        print("Correct! wohooo You Won!")
        print(name_of_list)
    else:
        print("Wrong choice, Better luck next time")
        print(name_of_list)

# Main List


game = [' ','O',' ']

# Shuffle list
shuffle_list(game)
# User input
predict=user_guess()
# Checking of the user's Input
check_guess(game,predict)