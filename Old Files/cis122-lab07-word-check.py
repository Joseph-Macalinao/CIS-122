'''
Joseph Macalinao
CIS122- Spring 2021
Credit: Lab
Description: Check to see if a word is in a file
'''

# Loop until nothing entered
while True:
    # Prompt for input
    word = input("Enter a search word (blank to exit): ")
    word = word.strip()  # Remove leading/trailing
    word = word.lower()
    if len(word) == 0:

        # Exit if nothing entered
        break
    else:
        # Perform search

        # Open file
        fin = open("../words_alpha.txt")

        # Search for word by looping over file
        found = False
        for line in fin:
            line = line.strip()
            line = line.lower()
            if word == line:
                found = True
                break

        # Close file
        fin.close()

        # Print results
        if found:
            print(f'Word {word} found')
        else:
            print(f'Word {word} not found')
