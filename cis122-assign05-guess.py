'''
Cis 122 Assignment 5 Spring 2021
Author: Jospeh Macalinao
Credit: Me and Kaya Jang
Description: Make a program that fills in missing letters in a word
'''
def guess():
    '''
    This guess game will ask for a word then have the user guess letters

    This function will ask the user for a word, then will prompt the user for a repeated guess /
    for letters in the word. The function will also tell the user if the letter is not found /
    and if or the lette has already been guessed

    arg - none

    return - n/a
    '''
    word = input("Enter a guess word (blank to quit):")
    if word == '':
        return 0
    guess_bank = ''
    matched_guess_bank = ''
    count = 0
    len_list = len(word)
    len_guess = (1 * len_list)
    #while loop that will continually go through guesses until all letters are found
    while len_guess > 0:
        guess_letter = input("Enter a letter you would like to guess: ")
        #checking to make sure that the input letter is only 1 letter
        if len(guess_letter) > 1:
            print("Only enter a single letter.")
            count += 1
            guess_letter = input("Enter a letter you would like to guess (blank to quit):")
        elif guess_letter == '':
            return 0
        if search(guess_bank,guess_letter) == True:
            print("That letter has already been guessed.")
            guess_letter = input("Enter a letter you would like to guess.")

        if guess_letter not in word:
            print("Letter not found:")
            guess_letter = input("Enter a letter you would like to guess.")
            count += 1
        for letter in word:

            if guess_letter == letter:
                letter = guess_letter
                len_guess -= 1
                matched_guess_bank = matched_guess_bank + letter
            else:
                letter = 0
            print(letter, end='')
        print()
        guess_bank = guess_bank + guess_letter
        print(f'Guesses so far: {guess_bank}')
        count += 1
        print(f'Guesses: {count}')
    print("*** Results ***")
    print(f'Word: \t{word}')
    print(f'Guessed: \t{guess_bank}')
    print(f'Matched: \t{matched_guess_bank}')
    print(f'Guesses: \t{count}')

def search(string, letter):
    '''
    will look for a letter

    will take a sting and a letter and will search to see if the letter appears in the string

    arg
    string(str) - string that will be checked
    letter(str) - letter that will be looked for

    return- Boolean
    '''
    for char in string:
        if char == letter:
            return True
        else:
            return False

guess()