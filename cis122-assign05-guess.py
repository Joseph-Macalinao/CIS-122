'''
Cis 122 Assignment 5 Spring 2021
Author: Jospeh Macalinao
Credit: Me and Kaya Jang
Description: Make a program that fills in missing letters in a word
'''



def guess():
    guessed_word_complete = False
    word = input("Enter a guess word (blank to quit):")
    guess_bank = ''
    count = 0
    while guessed_word_complete == False:
        guess_letter =input("Enter a letter you would like to guess: ")
        if len(guess_letter) > 1:
            print("Letter must only be 1 character.")
            guess_letter =input("Enter a letter you would like to guess:")
        for letter in word:
            if guess_letter == letter:
                letter = guess_letter
            else:
                letter = 0
            print(letter, end = '')
        guess_bank = guess_bank + guess_letter
        print()
        print(f'Guesses so far: {guess_bank}')
        print()
        count += 1
        print(f'Guesses: {count}')

def search(string):
    count_0 = 0
    for letter in string:
        if letter == '0':
            count_0 += 1
    return  count_0
guess()
