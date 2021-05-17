'''
Author: Joseph Macalinao
Credit: Lab
Description - making a set attribute calculator
Cis lab 6 Sprint 2021
'''


def pad_string(string, amount, space, side = 'left'):
    '''
    this function allows the padding of a string to either the left or right

    this function takes in a string, amount of spaces, space type, and side to pad a side with
    a certain amount of spaces to move strings around

    string(str) - string being padded
    amount(int) - how much its being padded
    space(str) - what the space will be
    side(optional/str) - side that the string will be padded on

    return(str) - padded amount with string
    '''
    if side.lower() == 'left':
         stm = (space * amount) + string + ':'
         return stm
    elif side.lower() =='right':
        stm = string + ':' + (space * amount)
        return stm



def pad_left(string,amount):
    '''
    this function allows the padding of a string to either the left or right

    this function takes in a string, amount of spaces, space type, and side to pad a side with
    a certain amount of spaces to move strings around which will be to the left

    string(str) - string being padded
    amount(int) - how much its being padded

    return(str) - padded amount with string
    '''
    stm = pad_string(string,amount, ' ', 'left')
    return stm
def pad_right(string, amount):
    '''
    this function allows the padding of a string to either the left or right

    this function takes in a string, amount of spaces, space type, and side to pad a side with
    a certain amount of spaces to move strings around which will be to the right

    string(str) - string being padded
    amount(int) - how much its being padded

    return(str) - padded amount with string
    '''
    stm = pad_string(string, amount, ' ', 'right')
    return stm
