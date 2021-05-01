
def is_leap_year(year):

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def valid_year(year):

    if year > 0:
        return True
    else:
        print("The year that is input has to be greater than 0")
        return False

def valid_day_of_year(year, day_of_year):

    if day_of_year > 0:
        return True
    else:
        print("The day of the year that is input has to be greater than 0")
        return False
def input_year():

    year = int(input("Enter year greater than 0: "))
    while year <= 0:
        print("The day of the year that is input has to be greater than 0: ")
        year = int(input("Enter year: "))
    if valid_year(year) == True:
        return year

def get_days_in_year(year):

    if is_leap_year(year) == True:
        return 366
    elif is_leap_year(year) == False:
        return 365
    else:
        return 0

def input_day_of_year(year):

    day = int(input("Enter day greater than 0: "))
    if is_leap_year(year) == True:
        while day > get_days_in_year(year) or day <= 0:
            while day > get_days_in_year(year):
                print("The day of the year that is input has to be less than or equal to 366")
                day = int(input("Enter a day greater than 0: "))
            while day <= 0:
                print("The day of the year that is input has to be greater than 0")
                day = int(input("Enter a day greater than 0: "))
        if valid_year and valid_day_of_year(year, day) and day <= get_days_in_year(year):
            return day
    elif is_leap_year(year) == False:
        while day > get_days_in_year(year) or day <= 0:
            while day > get_days_in_year(year):
                print("The day of the year that is input has to be less than or equal to 365")
                day = int(input("Enter a day greater than 0: "))
            while day <= 0:
                print("The day of the year that is input has to be greater than 0")
                day = int(input("Enter a day greater than 0: "))
        if valid_year(year) and valid_day_of_year(year, day) and day <= get_days_in_year(year):
            return day
        else:
            return 0

def valid_month(month):

    if 0 < month <= 12:
        return True
    elif month <= 0 or month > 12:
        print("The month input must be greater than 0 and less than 12")
        return False

def translate_month(month):
    if valid_month(month):
        if month == 1:
            return "January"
        elif month == 2:
            return "February"
        elif month == 3:
            return "March"
        elif month == 4:
            return "April"
        elif month == 5:
            return "May"
        elif month == 6:
            return "June"
        elif month == 7:
            return "July"
        elif month == 8:
            return "August"
        elif month == 9:
            return "September"
        elif month == 10:
            return "October"
        elif month == 11:
            return "November"
        elif month == 12:
            return "December"
    else:
        return ''

def get_days_in_month(year, month):
    if month == 1:
        return 31
    elif is_leap_year(year) == True and valid_month(month) == True and month == 2:
        return 29
    elif is_leap_year(year) == False and valid_month(month) == True and month == 2:  # If it's not a leap year
        return 28
    elif month == 3:
        return 31
    elif month == 4:
        return 30
    elif month == 5:
        return 31
    elif month == 6:
        return 30
    elif month == 7:
        return 31
    elif month == 8:
        return 31
    elif month == 9:
        return 30
    elif month == 10:
        return 31
    elif month == 11:
        return 30
    elif month == 12:
        return 31
    else:
        return 0


def valid_day(year, month, day):
    if valid_year(year) == True and valid_month(month) == True and valid_day_of_year(year, day) == True:
        return True
    else:
        return False

def get_date_string(year, month, day):
    if is_leap_year(year) is True and valid_year(year) is True:
        if (day == 1) or (day <= 31):
            month = "January"
        elif (day == 32) or (day <= 60):
            month = "February"
            day = day - 31
        elif (day == 61) or (day <= 91):
            month = "March"
            day = day - 60
        elif (day == 92) or (day <= 121):
            month = "April"
            day = day - 91
        elif (day == 122) or (day <= 152):
            month = "May"
            day = day - 121
        elif (day == 153) or (day <= 182):
            month = "June"
            day = day - 152
        elif (day == 183) or (day <= 213):
            month = "July"
            day = day - 182
        elif (day == 214) or (day <= 244):
            month = "August"
            day = day - 213
        elif (day == 245) or (day <= 274):
            month = "September"
            day = day - 244
        elif (day == 275) or (day <= 305):
            month = "October"
            day = day - 274
        elif (day == 306) or (day <= 335):
            month = "November"
            day = day - 305
        elif (day == 336) or (day <= 366):
            month = "December"
            day = day - 335
        print(month, str(day) + ",", year)
    if is_leap_year(year) is False and valid_year(year) is True:
        if (day == 1) or (day <= 31):
            month = "January"
        elif (day == 32) or (day <= 59):
            month = "February"
            day = day - 31
        elif (day == 60) or (day <= 90):
            month = "March"
            day = day - 59
        elif (day == 91) or (day <= 120):
            month = "April"
            day = day - 90
        elif (day == 121) or (day <= 151):
            month = "May"
            day = day - 120
        elif (day == 152) or (day <= 181):
            month = "June"
            day = day - 151
        elif (day == 182) or (day <= 212):
            month = "July"
            day = day - 181
        elif (day == 213) or (day <= 243):
            month = "August"
            day = day - 212
        elif (day == 244) or (day <= 273):
            month = "September"
            day = day - 243
        elif (day == 274) or (day <= 304):
            month = "October"
            day = day - 273
        elif (day == 305) or (day <= 334):
            month = "November"
            day = day - 304
        elif (day == 335) or (day <= 365):
            month = "December"
            day = day - 334
        print(month, str(day) + ",", year)

def start():
    month = get_date_string
    year = input_year()
    get_date_string(year, month, input_day_of_year(year))

start()