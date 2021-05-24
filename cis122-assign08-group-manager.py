'''
Joseph Macalinao
Cis122 Assignment 8 Spring 2021
Credit: Me and Kaya Jang
Description: Create a group manager using dictionaries and lists
'''

group = {}
group_list = []

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


def create_group(d):
    groupName = input("Enter group name (empty to cancel): ")
    if len(groupName) == 0:
        initial_input()
    elif groupName in group.keys():
        print("That group already exists")
    elif groupName not in group.keys():
        k = groupName
        fieldName = input("Enter field name (empty to stop): ")
        while len(fieldName) != 0:
            group_list.append(fieldName)
            group[k] = group_list
            fieldName = input("Enter field name (empty to stop): ")
    initial_input()

def list_groups(d):
    field = ''
    for i in group_list:

        field += i
        field += ', '
    print("** List of Groups **\n")
    for i in group:
        print(f'{i}: {len(group_list)} properties {group_list}')
    initial_input()

def add_group_data(d):
    print('h')

def list_group_data(d):
    print('hio')

initial_input()
