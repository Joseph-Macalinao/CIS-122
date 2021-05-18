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



def cmd_help():
    print('*** Available Commands ***')
    for i in range(len(cmd)):
        print(pad_right((cmd[i]), 10 - (len(cmd[i]))) + description[i])
    print('Empty to exit')
    intitial_input()
def cmd_add(t):
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
    print(f'The total amount of items in your list is {len(list)}')
    for i in list:
        print(i)
    intitial_input()

def cmd_clear(t):
    leng = len(list)
    list.clear()
    print(f'{leng} items removed')
    intitial_input()

def get_max_list_item_size(t):
    pass


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