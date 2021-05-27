'''
Joseph Macalinao
Cis122 Assignment 8 Spring 2021
Credit: Me and Kaya Jang
Description: Create a group manager using dictionaries and lists
'''

group = {}

def initial_input():
    print(">>Welcome to Group Manager<<\nThis program creates groups with dynamic properties")
    boo = True
    while boo == True:
        deci = input("Command(empty or X to quit, ? for help):")
        deci = deci.strip()
        deci = deci.upper()
        if len(deci) == 0 or deci == 'X':
            return 0
        elif deci == '?':
            print(
                '?: list commands\nC: Create a new group\nA: Add data to a group\n'
                'G: List groups\nL: List data for a group\nX: Exit'
                )
        elif deci == 'C':
            create_group(group)
            boo = False
        elif deci == 'A':
            add_group_data(group)
            boo = False
        elif deci == 'G':
            list_groups(group)
            boo = False
        elif deci == 'L':
            list_group_data(group)
            boo = False


def create_group(group):
    val = ''
    valid = False
    groupName = input("Enter group name (empty to cancel): ")
    while valid == False:
        if len(groupName) == 0:
            initial_input()
        elif groupName in group.keys():
            print("That group already exists")
            groupName = input("What would you like the name of your group to be: ")
        else:
            valid = True
    field = True
    while field == True:
        fieldName = input("Enter field name (empty to stop): ")
        if len(fieldName) == 0:
            break
        else:
            val += fieldName + ' '
        group[groupName] = val
    initial_input()


def list_groups(group):
    field = ''
    for i in group.values():
        field += i
    field = field.split(' ')
    field = list(field)
    field.remove('')
    print("** List of Groups **\n")
    for i in group:
        print(f'{i}: {len(field)} properties ({field})')
    initial_input()

def add_group_data(d):
    print('h')

def list_group_data(d):
    print('hio')


initial_input()
