import random
from words import words as w
from colorama import Fore, Back, Style


MAX_TRIES = 6
WORD_LENGTH = 5
DOUBLE_LETTER = '*'


alphabet = ['f', 'g', 'm', 'b', 'x', 'q', 'n', 'v', 'r', 'p', 'o', 'i',
            's', 'e', 'l', 'k', 'd', 'z', 'y', 'c', 'h', 'j', 't', 'a', 'u', 'w']


attempts = []


def find_a_word():
    five_letter_word = random.choice(w)
    while len(five_letter_word) != WORD_LENGTH:
        five_letter_word = random.choice(w)
    return five_letter_word.upper()


def hasWon(guess):
    return guess == secret


def accept_guess(guess):
    while len(guess) != WORD_LENGTH:
        guess = input("Sorry, 5 letter's only.  Try again: ")
    attempts.append([word for word in guess])
    return guess


def canPlay(guess):
    if len(attempts) > MAX_TRIES or hasWon(guess) == True:
        return False


def check_in_place(guess, secret):
    for i in len(secret):
        if guess[i] == secret[i]:
            attempts[-1][i] = guess[i]


def check_in_word(guess, secret):
    for i in range(WORD_LENGTH):
        if guess[i] in secret:
            attempts[-1][i] = '*'


def print_attempts():
    my_string = ""
    for i in range(len(attempts)):
        for x in attempts[i]:
            my_string += x + ' '
        my_string += '\n'
    for _ in range(MAX_TRIES - len(attempts)):
        my_string += ('_' + ' ')*WORD_LENGTH
        my_string += '\n'
    return my_string


def double_secret():
    make_list = []
    for i in range(WORD_LENGTH):
        make_list.append(secret[i])


def wordle():
    while True:
        guess = input("Guess the word: ").upper()
        while len(guess) != WORD_LENGTH:
            guess = input("Sorry, 5 letter's only.  Try again: ")
        attempts.append([word for word in guess])
        remaining_secret = list(secret)
        for i in range(WORD_LENGTH):
            if guess[i] == remaining_secret[i]:
                attempts[-1][i] = Fore.GREEN + guess[i] + Fore.RESET
                remaining_secret[i] = DOUBLE_LETTER

            elif guess[i] in remaining_secret:
                attempts[-1][i] = Fore.YELLOW + guess[i] + Fore.RESET

            else:
                attempts[-1][i] = Fore.RED + guess[i] + Fore.RESET
        print(print_attempts())
        if hasWon(guess) == True:
            print('Congratulations! You Won!')
            break
        if len(attempts) == MAX_TRIES:
            print(f'Sorry, you ran out of guesses, the word was {secret}')
            break


secret = find_a_word()
print(secret)
# print(secret)
wordle()
