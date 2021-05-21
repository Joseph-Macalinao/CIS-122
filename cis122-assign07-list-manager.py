'''
Joseph Macalinao
CIS122 Spring Assign 7
Credit - Me and Kaya Jang
Description - Make functions that will help with list
things
'''

list = []
cmd = ['Add', 'Delete', 'List', 'Clear']
description = ['Add to list', 'Delete information', 'List information', 'Clear list']

def intitial_input():
    '''
    function takes input for list and directs user

    this function will take an input and will direct the user around the program if input is
    "?". it will tell the user what each thing does and is called at the end of each function

    arg - na

    return(int) - 0 if nothing is input
    '''
    deci = input("Enter a command (? for help):")
    deci = deci.strip()
    deci = deci.lower()
    if len(deci) == 0:
        print("Goodbye")
        return 0
    if deci == '?':
        cmd_help()
    elif deci == 'add':
        cmd_add(list)
    elif deci == 'list':
        cmd_list(list)
    elif deci == 'clear':
        cmd_clear(list)
    elif deci == 'delete':
        cmd_delete(list)
    else:
        print("Input not usable. Try again.")
        intitial_input()



def cmd_help():
    '''
    function helps user around function

    this function will guide users around the inputs by printing out the inputs and what
    they do to lists

    arg - none

    return - none

    '''
    print('*** Available Commands ***')
    for i in range(len(cmd)):
        print(pad_right((cmd[i]), 10 - (len(cmd[i]))) + description[i])
    intitial_input()
def cmd_add(t):
    '''
    will add elements to a list

    this function will take user input and will add to the given list(list) above.

    arg(list) - t

    return - none
    '''
    ad = False
    while ad == False:
        elem = input('Enter information (empty to stop): ')
        if len(elem) == 0:
            ad = True
        else:
            list.append(elem)
            print(f'Added, item count {len(list)}')
    intitial_input()
def cmd_delete(t):
    '''
    function will delete a given element in a list

    this function will take user input and will delete the given cooresponding numbered element

    arg(list) - t

    return - none
    '''
    n = 0
    dele_dec = False
    for i in range(len(list)):
        print(pad_right(str(n),3) + list[i])
        n += 1
    while dele_dec == False:
        if len(list) == 0:
            print('There are no more elements to delete.')
            intitial_input()
        dele = input("Enter number to delete (empty to stop): ")
        dele = dele.strip()
        if dele.isdigit():
            dele = int(dele)
            del list[dele]
        if dele == '':
            dele_dec = True
        intitial_input()
def cmd_list(t):
    '''
    this function prints the list

    this function prints the list given the changes done to it

    arg
    list(t) - given list that was changed

    return - none
    '''
    print(f'The total amount of items in your list is {len(list)}')

    for i in list:
        if len(list) == 0:
            print("List has no elements")
        print(i)
    intitial_input()

def cmd_clear(t):
    '''
    clears the list

    this function clears the list given in the arg by using the list.clear function

    arg
    list(t) - list being cleared

    return - none
    '''
    leng = len(list)
    list.clear()
    print(f'{leng} items removed')
    intitial_input()

def get_max_list_item_size():
    '''
    gets the biggest item size in the lists

    checks the two lists used for descriptions and sees the length of the biggest
    command and description

    arg - none

    return
    Long1 and long2(int) - longest elements in the lists
    '''
    long_1 = 0
    long_2 = 0
    for i in cmd:
        if len(i) > long_1:
            long_1 = i
    for i in description:
        if len(i) > long_2:
            long_2 = i
    return long_1, long_2


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
intitial_input()