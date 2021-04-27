import calendar

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
            result = result + str(year) + ', '
    print(result)

test_is_leap_year(1996, 2112)

def validate_leap_year(start_year, end_year):
    '''

    '''
    for year in range(start_year, end_year + 1):
        is_leap = is_leap_year(year)
        if is_leap:
            result = result + str(year) + ', '
    print(result)
