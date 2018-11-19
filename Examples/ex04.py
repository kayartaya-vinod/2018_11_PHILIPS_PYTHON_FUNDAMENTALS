'''
ex04

Calendar functionalities
'''

def is_leap(year):
    if year != None and type(year) != int: raise Exception('Invalid type for year. Only int is allowed')
    if year != None and year < 1900: raise Exception('Invalid value for year. Only above 1900 is allowed')

    # method #1: 
    # if year % 400 == 0: return True
    # if year % 4 ==0 and year % 100 != 0: return True
    # return False
    
    # method #2: 
    return (year % 400 == 0) or (
        year % 4 ==0 and year % 100 != 0)

def max_days_in_year(year): 
    return 366 if is_leap(year) else 365

def max_days_in_month(month, year):
    # assumption: month and year are valid values
    if month == 2: return 29 if is_leap(year) else 28
    elif month in [4, 6, 9, 11]: return 30
    else: return 31

def date_serial(day, month, year):
    ds = 0
    # days between 1/1/1900 and last day of (year-1)
    for y in range(1900, year): 
        ds += max_days_in_year(y)

    # days between 1/1/year and last-day/month-1/year
    for m in range(1, month): 
        ds += max_days_in_month(m, year)

    # remaining days in month/year
    ds += day

    return ds

def print_calendar(month, year):
    print('Su Mo Tu We Th Fr Sa')
    print('--------------------')
    max_days = max_days_in_month(month, year)
    ds = date_serial(1, month, year)
    dow = ds%7
    print(' '*dow*3, end='')
    for d in range(1, max_days+1):
        print('{:2} '.format(d), end='') # Python 3.x
        # print '{:2} '.format(d),  # Python 2.x

        if (d+dow)%7==0: print()

    print()
    print('--------------------')
