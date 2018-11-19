'''
ex03

Defines a function for printing multiplication table
'''

def print_table(num, limit=10):
    '''
    print_table

    Prints a multiplication table for the input num.
    Default number of lines is 10, which can be overridden.
    '''

    i = 1
    while i<=limit:
        p = num * i
        print('{} X {} = {}'.format(num, i, p))
        i += 1

    print('-'*15)

def main():
    n = input('Enter a number: ')
    # Python 3.x only
    n = int(n)
    print_table(n)

if __name__=='__main__':
    main()