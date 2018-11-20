'''
ex08

Handling exceptions
'''

import sys

def main():
    try:
        n1 = sys.argv[1]
        n2 = sys.argv[2]
        n1 = int(n1)
        n2 = int(n2)
        q = n1//n2
        print('{} / {} = {}'.format(n1, n2, q))
    except (IndexError, ValueError):
        print('You must supply two numbers:')
        # return
        # exit()
        raise Exception('Just causing a problem..')
    except ZeroDivisionError: 
        print('Cannot divide by zero:')
    except:
        print('There was an error!')
    finally:
        # executes in all scenarios (exception or no exception)
        print('Now inside the finally block!')

    print('End of script')

if __name__=='__main__': main()