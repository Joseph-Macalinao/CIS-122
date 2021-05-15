'''
Author: Joseph Macalinao
Assignment 4 CIS 122
Credit: Me and Kaya Jang
Description: Accept a user year and day and convert it to a month, day, and year
'''

def date_calculator_non_leap():
    '''
    This function will calculate what day of the year it is for non-leap years.

    This function will take an input and by using/
    12 if statements and then checking the index/
    of that input in the month's given range

    arguments - none

    return
    month(str) - the month of the day input
    day(int) - day of the month that was calculated
    '''
    day = int(input("What day of they year will you be calculating from 1-365?"))
    if day < 0 or day == 0:
        print("Day must be above 0.")
        start()
    elif 0 < day <= 31:
        month = 'January'
        day = range(0, 32).index(day)
        print(month + ", " + str(day))
    elif 31 < day <= 59:
        month = 'February'
        day = range(32, 60).index(day) + 1
        print(month + ", " + str(day))
    elif 59 < day <= 90:
        month = 'March'
        day =  range(60, 91).index(day) + 1
        print(month + ", " + str(day))
    elif 90 < day <= 120:
        month = 'April'
        day = range(91, 121).index(day) + 1
        print(month + ", " + str(day))
    elif 120 < day <= 151:
        month  = 'May'
        day = range(121, 152).index(day) + 1
        print(month + ", " + str(day))
    elif 151 < day <= 181:
        month = 'June'
        day = range(151, 182).index(day) + 1
        print(month + ", " + str(day))
    elif 181 < day <= 212:
        month = 'July'
        day = range(182, 213).index(day) + 1
        print(month + ", " + str(day))
    elif 212 < day <= 243:
        month = 'August'
        day = range(213, 244).index(day) + 1
        print(month + ", " + str(day))
    elif 243 < day <= 273:
        month = 'September'
        day = range(244, 274).index(day) + 1
        print(month + ", " + str(day))
    elif 273 < day <= 304:
        month = 'October'
        day = range(274, 305).index(day) + 1
        print(month + ", " + str(day))
    elif 304 < day <= 334:
        month = 'November'
        day = range(305, 335).index(day) + 1
        print(month + ", " + str(day))
    elif 334 < day <= 365:
        month = 'December'
        day = range(335, 367).index(day) + 1
        print(month + ", " + str(day))
    else:
        print("Invalid Date: Give a day that is 1-365")
        start()


def date_calculator_leap():
    '''
    This function will calculate what day of the year it is for leap years.

    This function will take an input and by using/
    12 if statements and then checking the index/
    of that input in the month's given range. /
    This function also adds a day to the end of February onwards to account for the extra day.

    arguments - none

    return
    month(str) - the month of the day input
    day(int) - day of the month that was calculated
    '''
    day = int(input("What day of they year will you be calculating from 1-366?"))

    if day < 0 or day == 0:
        print("Day must be above 0.")
        start()
    elif 0 < day <= 31:
        month = 'January'
        day = range(0, 32).index(day)
        print(month + ", " + str(day))
    elif 31 < day <= 60:
        month = 'February'
        day = range(32, 61).index(day) + 1
        print(month + ", " + str(day))
    elif 60 < day <= 91:
        month = 'March'
        day =  range(61, 92).index(day) + 1
        print(month + ", " + str(day))
    elif 91 < day <= 121:
        month = 'April'
        day = range(92, 122).index(day) + 1
        print(month + ", " + str(day))
    elif 121 < day <= 152:
        month  = 'May'
        day = range(122, 153).index(day) + 1
        print(month + ", " + str(day))
    elif 152 < day <= 183:
        month = 'June'
        day = range(152, 183).index(day) + 1
        print(month + ", " + str(day))
    elif 182 < day <= 213:
        month = 'July'
        day = range(183, 214).index(day) + 1
        print(month + ", " + str(day))
    elif 213 < day <= 244:
        month = 'August'
        day = range(214, 245).index(day) + 1
        print(month + ", " + str(day))
    elif 244 < day <= 274:
        month = 'September'
        day = range(245, 275).index(day) + 1
        print(month + ", " + str(day))
    elif 274 < day <= 305:
        month = 'October'
        day = range(275, 306).index(day) + 1
        print(month + ", " + str(day))
    elif 305 < day <= 335:
        month = 'November'
        day = range(306, 336).index(day) + 1
        print(month + ", " + str(day))
    elif 335 < day <= 366:
        month = 'December'
        day = range(336, 368).index(day) + 1
        print(month + ", " + str(day))
    else:
        print("Invalid Date: Give a day that is 1-365")
        start()





def print_date():
    '''
    This function will print out the date depending on the year

    This function will take a year input and if the year is a
    leap year, it will call the leap year function, but if it is
    a regular year, it will call the non-leap year funciton.
    It also checks to make sure the year is valid.

    arguments - None

    reuturn - none
    '''
    year = int(input("Enter a year: "))

    if year == 0:
        print("Enter a valid year above 1.")
        start()


    #if the year is a leap year
    elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        date_calculator_leap()

    
    #if the year is a normal year
    elif year:
        date_calculator_non_leap()

    #other circumstances
    else:
        print("Enter a valid year above 1.")
        start()



def start():
    '''
    Initializes program to start(I read ahead and thought I came up with this idea and
    when I realized what happened, it was too late)
    '''
    print_date()

start()

