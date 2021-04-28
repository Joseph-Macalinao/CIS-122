
def get_full_month(n):
    '''
    Given an int n, convert it to the equivalent month as a string
    '''
    if n == 1:
        result = "January"
    elif n == 2:
        result = "February"
    elif n == 3:
        result = "March"
    elif n == 4:
        result = "April"
    elif n == 5:
        result = "May"
    elif n == 6:
        result = "June"
    elif n == 7:
        result = "July"
    elif n == 8:
        result = "August"
    elif n == 9:
        result = "September"
    elif n == 10:
        result = "October"
    elif n == 11:
        result = "November"
    elif n == 12:
        result = "December"
    else:
        result = f'Must be an integer between 1 and 12 ({n} is invalid)'
    return result

def test_get_full_month():
    '''

    '''
    for i in range(14):
        result = get_full_month(i)
        if i > 0 and i < 13:
            print(i, result)
        else:
            print(result)

test_get_full_month()

def is_leap_year(n):
    '''
    Given an int, return whether that value is a leap year

    This function uses the algorithm of finding if a year is a leap year to determine \
    if a year is a leap year

    n(int) - year that you are testing

    return(boolean)
    '''
    if n % 4 != 0:
        return False
    if n % 100 != 0:
        return True
    if n % 400 != 0:
        return False
    else:
        return True
def test_is_leap_year(start_year, end_year):
    result = ''
    for year in range(start_year, end_year + 1):
        is_leap = is_leap_year(year)
        if is_leap:
            if year == end_year + 1:
                print(end_year)
            else:
                result = result + str(year) + ', '
    print(result)

test_is_leap_year(1996, 2112)

def validate_leap_year(start_year, end_year):
    '''
    this function will validate if the year is a leap year

    this function will see, using the test_is_leap_year function to see if the day really is a function

    start_year(int) - year that it is starting with
    end_year(int) - year that it will end with

    return - void
    '''
    result = ''
    for year in range(start_year, end_year + 1):
        is_leap = is_leap_year(year)
        if is_leap:
            result = result + str(year) + ', '
    print(result)