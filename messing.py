'''
Cis 122 Assignment 5 Spring 2021
Author: Jospeh Macalinao
Credit: Me and Kaya Jang
Description: Make a program that fills in missing letters in a word
'''
def guess():
    word = input("Enter a guess word (blank to quit):")
    if word == '':
        return 0
    guess_bank = ''
    count = 0
    len_list = len(word)
    len_guess = (1 * len_list)
    #while loop that will continually go through guesses until all letters are found
    while len_guess > 0:
        guess_letter = input("Enter a letter you would like to guess: ")
        #checking to make sure that the input letter is only 1 letter
        if len(guess_letter) > 1:
            print("Letter must only be 1 character.")
            guess_letter = input("Enter a letter you would like to guess (blank to quit):")
        elif guess_letter == '':
            return 0
        if search(guess_bank,guess_letter):
            print("That letter has already been guessed.")
            guess_letter = input("Enter a letter you would like to guess.")
        for letter in word:
            if search(word, letter) == False:
                print("That letter wasn't found.")
                guess_letter = input("Enter a letter you would like to guess")
            if guess_letter == letter:
                letter = guess_letter
                len_guess -= 1

            else:
                letter = 0
            print(letter, end='')
        print()
        guess_bank = guess_bank + guess_letter
        print(f'Guesses so far: {guess_bank}')
        count += 1
        print(f'Guesses: {count}')
    print(f'Good job, you guessed the word: {word} in {count} tries.')
    print(f'You matched: {guess_bank}')

def search(string, letter):
    for i in string:
        if letter == letter:
            return True
        else:
            return False

guess()
