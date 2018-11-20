'''
ex07

Examples of different types of function parameters/arguments in Python
'''

# example for named/positional, mandatory/optional parameters
def test1(name, email, city='bangalore'):
    # name and email are mandatory parameters
    # city is an optional parameter, since it has a default
    # after optional parameter, we can not have positional/non-default parameter
    print('Name  = %s' % name)
    print('Email = %s' % email)
    print('City  = %s' % city)
    print('-'*50)

def main():
    test1('vinod', 'vinod@vinod.co')
    test1('john', 'john@example.com', 'dallas')

    data = ['jane', 'jane@example.com', 'washington']
    test1(*data) # destructuring of the list/tuple

    data = {'email':'kiran@example.com', 'city':'hassan', 'name':'kiran'}
    test1(**data) 
    # single * with dict --> keys
    # double * with dict --> values


if __name__=='__main__': main()