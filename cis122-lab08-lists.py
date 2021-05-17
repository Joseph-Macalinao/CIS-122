'''
Joseph Macalinao
Cis122 lab 8
Credit: lab
Description - making a list using random ints
'''


import random
def gen_random_integer_list(num, start_range = 1, end_range = 100, sort_list = 'N'):
    '''

    '''
    #initialize empty list
    t = []

    #check if num > 0
    if num <= 0:
        print('num must be > 0')
    #check if num is int
    elif not isinstance(num, int):
        print('num must be an integer')
    #check if start or end num is int
    elif not isinstance(start_range, int) or not isinstance(end_range, int):
        print('start_range and end_range must be integers')
    #if in put is valid
    else:
        #iterate from 0 to num -1
        for i in range(num):
            #get random int in range given start to end
            r = random.randint(start_range, end_range)
            #put number in empty list
            t.append(r)
        #check optional parameter to see if list needs to be sorted
        if sort_list.upper() == 'Y':
            t.sort()
    #return the list
    return t

random_list = gen_random_integer_list(10, -1000, 1000)

def get_high_score(l):
    #guardian code
    #use isinstance to validate argument is a list
    if not isinstance(l, list):
        print('List argument expected')
        return -1

    if len(l) == 0:
        return 0

    #copy and sort list l
    cpy = sorted(l)

    #return the last element
    return cpy[-1]

def get_low_score(l):
    #guardian code
    #use isinstance to validate argument is a list
    if not isinstance(l, list):
        print('List argument expected')
        return -1

    if len(l) == 0:
        return 0

    #copy and sort list l
    cpy = sorted(l)

    #return the last element
    return cpy[0]



def get_mean_score(l):
    #guardian code
    #use isinstance to validate argument is a list
    if not isinstance(l, list):
        print('List argument expected')
        return -1

    if len(l) == 0:
        return 0

    return sum(l) / len(l)

def get_median_score(l):
    #guardian code
    #use isinstance to validate argument is a list
    if not isinstance(l, list):
        print('List argument expected')
        return -1

    if len(l) == 0:
        return 0

    cpy = sorted(l)

    if not len(cpy) % 2:
        i = (len(cpy) - 1) // 2
        return cpy[i]
        #[1, 2, 3]
        #0, 1, 2
        #len == 3
        #3 - 1 = 2
        #2/2 = 1

        #5 - 1 = 4
        #4/2 = 2
    else:
        i = len(cpy) // 2
        return (cpy[i - 1] + cpy[i]) / 2
        #[0, 1, 2, 3, 4, 5]
        # 6 / 2 = 3


t = gen_random_integer_list(10, 0, 100)
def count_range(l, start, end):
    '''

    '''
    if not isinstance(l, list):
        return -1
    if not isinstance(start, int) and not isinstance(end, int):
        print('Start and end must be integers')
        return -1
    if start >= end:
        print('Start must be < end')
        return -1
    if len(l) == 0:
        return 0
    count = 0
    for score in l:
        if score >= start and score <= end:
            count += 1

    return count


def list_range(l):
    '''

    '''
    fg = count_range(l, 0, 59)
    dg = count_range(l, 60, 69)
    cg = count_range(l, 70, 79)
    bg = count_range(l, 80, 89)
    ag = count_range(l, 90, 100)

    print(f'A: {ag}')
    print(f'B: {bg}')
    print(f'C: {cg}')
    print(f'D: {dg}')
    print(f'F: {fg}')
print(t)
list_range(t)