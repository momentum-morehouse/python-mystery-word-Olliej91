# let the user know how many letters the computers word is
# user guesses one letter per round
# let the user know if there guess is in the comouters word
# display the partially guessed word & the letters that have not been guessed
# keep track of guesses
# game ends when word is guessed or user runs out of attempts

import random
random_word = (random.choice(open("words.txt").readlines()))

import re

def computer_picks_word():
    print(random_word)
    return random_word

computer_picks_word()

a = random_word
print(len(a))

def get_user_guess():
    guess = input("Guess a letter")
    return(guess)
    if not re.match("[a-z, A-Z]", guess):
        print ("Letters only!")
        sys.exit()
    elif len(guess) < 2:
        print("Too many letters!")
        sys.exit()   
get_user_guess()

