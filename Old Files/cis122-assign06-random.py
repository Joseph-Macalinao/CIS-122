'''
Author: Joseph Macalinao
Credit: Lab
Description - making a set attribute calculator
Cis Assign 6 Sprint 2021
'''


from cis122_assign06_shared import pad_left, pad_right

import os


def file():
    '''
    this function will give the stats about a file

    this function, after validating the existence of a file, will print the count, average, amount of numbers
    and amount of comments. this function also uses the os module to verify that the file called exists

    arg - none

    return - none
    '''
    fil = input("Enter filename (blank to exit): ")
    if fil == '':
        return 0
    while os.path.exists(fil) == False:
        print("Invalid filename")
        fil = input("Enter filename (blank to exit): ")
        if fil == '':
            return 0

    na = open('random_numbers.txt')
    total_hash = 0
    total_num = 0
    total = 0
    for line in na:
        line.strip()
        line.lower()
        if line[0] == '#':
            total_hash += 1
        else:
            line = int(line)
            total_num += 1
            total += line

    avg = total / total_num
    label_spacing = 10
    print(pad_right("Count", label_spacing + 1) + str(total_num))
    print(pad_right("Comments", label_spacing) + str(total_hash))
    print(pad_right("Total", label_spacing) + str(total))
    print(pad_right("Average", label_spacing - 3) + str(avg))


    na.close()
    '''
    print(f'Count: {total_num}')
    print(f'Comments: {total_hash}')
    print(f'Total: {total}')
    print(f'Average: {avg}')
    '''

file()