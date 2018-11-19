from ex04 import is_leap, max_days_in_month, date_serial, print_calendar
import sys

def test01():
    if len(sys.argv)>=2: y = int(sys.argv[1])
    else: y = int(input('Enter an year: '))
    
    leap = is_leap(y)
    print('is_leap({}) = {}'.format(y, leap))

def test02():
    m = int(input('Enter month: '))
    y = int(input('Enter year: '))
    days = max_days_in_month(m, y)
    print('{}/{} has {} days'.format(m, y, days))

def test03():
    d = int(input('Enter date: '))
    m = int(input('Enter month: '))
    y = int(input('Enter year: '))
    ds = date_serial(d, m, y)

    print('{}/{}/{} --> {}'.format(d, m, y, ds))
    dow = ds % 7
    print('Day of the week', dow)

def test04():
    m = int(input('Enter month: '))
    y = int(input('Enter year: '))
    print_calendar(m, y)

if __name__=='__main__': test04()