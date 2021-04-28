'''
Author: Joseph Macalinao
Assignment 4 CIS 122
Credit: Me and Kaya Jang
Description: Accept a user year and day and convert it to a month, day, and year
'''

def date_calculator_non_leap(day):
    '''

    '''
    i = 365
    if 0 < day <= 31:
        month = 'January'
        return month
    elif 31 < day <= 59:
        month = 'February'
        return month
    elif 59 < day <= 90:
        month = 'March'
        return month
    elif 90 < day <= 120:
        month = 'April'
        return month
    elif 120 < day <= 151:
        month  = 'May'
        return month
    elif 151 < day <= 181:
        month = 'June'
        return month
    elif 181 < day <= 212:
        month = 'July'
        return month
    elif 212 < day <= 243:
        month = 'August'
        return month
    elif 243 < day <= 273:
        month = 'September'
        return month
    elif 273 < day <= 304:
        month = 'October'
        return month
    elif 304 < day <= 334:
        month = 'November'
        return month
    elif 334 < day <= 365:
        month = 'December'
        return month
    else:
        print("Invalid Date - Give a day that is 1-365")


print(date_calculator_non_leap(135))


#def print_date(day, year):
    #if the year is a leap year
    #if year % 4 != 0 and year % 100 != 0 or year % 400 != 0:


    #if the year is a normal year
    #else:
        #
