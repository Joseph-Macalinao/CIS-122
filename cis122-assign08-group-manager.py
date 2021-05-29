'''
Joseph Macalinao
Cis122 Assignment 8 Spring 2021
Credit: Me and Kaya Jang
Description: Create a group manager using dictionaries and lists
'''

group = {}

def initial_input():
    '''
    this function starts the program

    this function allows the user to decide what they want to do to the group

    arg - non

    return - none
    '''
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
    '''
    this function creates group to add info to

    this function asks users to input a name for a group if the name len is 0 or if the name is already
    in use, the name will not be taken

    arg(group) - dictionary

    return - none
    '''
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


def list_groups(group, cont = True):
    '''
    this function lists the groups given

    this function lists the groups with their attributes/properties

    arg
    group(dict) - dictionary storing info
    cont(optional) - allows to pass onto next function without messing things up

    return - none
    '''
    print("** List of Groups **\n")
    for i in group:
        print(f'{i}: {len((group[i].split()))} properties ({group[i].split()})')
    if cont is True:
        initial_input()
    elif cont is False:
        pass


def add_group_data(group):
    '''
    this function adds data to the groups attributes

    this function allows the user to add data to the attributes of the groups. it stores them as dictionary values

    arg
    group(dict) - dictionary storing in

    return
    none
    '''
    val = ''
    ele = ''
    valid = True
    list_groups(group, False)
    while valid == True:
        group_data = input("Which group would you like to add data to (empty to cancel): ")
        if len(group_data) == 0:
            initial_input()
        elif group_data not in group:
            print("Value not in group.")
            continue
        else:
            for i in group.copy():
                if i  == group_data:
                    for ele in group[i].split():
                        val = ''
                        add_data = input(f'Enter data for {ele}')
                        val += add_data
                        group[ele] = val
        print(group)


def list_group_data(group):
    '''
    this function prints out the group data

    this function prints out the group data and shows it

    arg
    group(dict) - dictionary where info is being stores

    return
    none
    '''
    list_groups(group, False)
    for i in group:
        if i in group.keys():
            print(f'{group[i]}')



initial_input()
