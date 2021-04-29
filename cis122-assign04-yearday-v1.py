'''
Author: Joseph Macalinao
Assignment 4 CIS 122
Credit: Me and Kaya Jang
Description: Accept a user year and day and convert it to a month, day, and year
'''

def date_calculator_non_leap():
    '''
    This function will calculate what day of the year it is.

    This function will take an input and by using/
    12 if statements and then checking the index/
    of that input in the month's given range

    arguments - none

    return
    month(str) - the month of the day input
    day(int) - day of the month that was calculated
    '''
    day = int(input("What day of they year will you be calculating from 1-365?"))
    if 0 < day <= 31:
        month = 'January'
        day = range(0, 32).index(day)
        return month, day
    elif 31 < day <= 59:
        month = 'February'
        day = range(32, 60).index(day) + 1
        return month, day
    elif 59 < day <= 90:
        month = 'March'
        day =  range(60, 91).index(day) + 1
        return month, day
    elif 90 < day <= 120:
        month = 'April'
        day = range(91, 121).index(day) + 1
        return month, day
    elif 120 < day <= 151:
        month  = 'May'
        day = range(121, 152).index(day) + 1
        return month, day
    elif 151 < day <= 181:
        month = 'June'
        day = range(151, 182).index(day) + 1
        return month
    elif 181 < day <= 212:
        month = 'July'
        day = range(182, 213).index(day) + 1
        return month, day
    elif 212 < day <= 243:
        month = 'August'
        day = range(213, 244).index(day) + 1
        return month, day
    elif 243 < day <= 273:
        month = 'September'
        day = range(244, 274).index(day) + 1
        return month, day
    elif 273 < day <= 304:
        month = 'October'
        day = range(274, 305).index(day) + 1
        return month, day
    elif 304 < day <= 334:
        month = 'November'
        day = range(305, 335).index(day) + 1
        return month, day
    elif 334 < day <= 365:
        month = 'December'
        day = range(335, 367).index(day) + 1
        return month, day
    else:
        print("Invalid Date: Give a day that is 1-365")


print("The date is" + str(date_calculator_non_leap()))

'''
def print_date(day, year):
    if the year is a leap year
    if year % 4 != 0 and year % 100 != 0 or year % 400 != 0:
    
    if the year is a normal year
    else:
'''
