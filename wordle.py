from words import words as w
import random
import string


alphabet = ['f', 'g', 'm', 'b', 'x', 'q', 'n', 'v', 'r', 'p', 'o', 'i',
            's', 'e', 'l', 'k', 'd', 'z', 'y', 'c', 'h', 'j', 't', 'a', 'u', 'w']


def find_a_word():
    five_letter_word = random.choice(w)
    while len(five_letter_word) < 5 or len(five_letter_word) > 5:
        five_letter_word = random.choice(w)
    return five_letter_word


word = find_a_word()
print(word)
display_word = ["_", "_", "_", "_", "_"]

chances = 0

while chances < 6:
    print(display_word)
    guess = input("Guess a 5 letter word: ")
    i = 0
    chances += 1
    for letter in word:
        if letter in guess and letter != guess[i]:
            display_word[i] = "#"
            i += 1

        elif letter == guess[i]:
            display_word[i] = letter
            i += 1

        else:
            display_word[i] = "_"
            i += 1
