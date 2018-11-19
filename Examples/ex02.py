'''
ex02

Working with user defined, re-usable functions.
'''

def say_hello():
    '''
    say_hello

    This function just prints a hello message on the console
    '''
    print('Hello, world!')
    print('Python is different!!')

# The following will be ignored, when "import"ing this module
if __name__=='__main__':
    say_hello()