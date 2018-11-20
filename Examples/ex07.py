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

def main1():
    test1('vinod', 'vinod@vinod.co')
    test1('john', 'john@example.com', 'dallas')

    data = ['jane', 'jane@example.com', 'washington']
    test1(*data) # destructuring of the list/tuple

    data = {'email':'kiran@example.com', 'city':'hassan', 'name':'kiran'}
    test1(**data) 
    # single * with dict --> keys
    # double * with dict --> values

# test2 accepts 'arbitrary' arguments
def test2(*args):
    print('type of args is', type(args))
    print('args is', args)
    print('-'*50)

def main2():
    test2()
    test2(100, 200, 'vinod', 'bangalore')
    nums = [12, 34, 56, 78]
    test2(*nums)

# this function accepts 'keyward' arguments
def test3(**kwargs):
    print('type of args is', type(kwargs))
    print('kwargs is', kwargs)
    print('-'*50)

def main3():
    test3(name='vinod', city='blore', email='vinod@vinod.co')
    test3(x=10, y=20, z=15)
    test3()
    data = dict(a=100, b=200, c=300)
    test3(**data)
    # test3('vinod') # error; no positional or arbitrary args

# combination of all types of args
def test4(name, city='bangalore', *args, **kwargs):
    print('Name  = %s' % name)
    print('City  = %s' % city)
    print('args  =', args)
    print('kwargs  =', kwargs)
    print('-'*50)

def main():
    test4('vinod')
    test4('harish', 'hassan')
    test4('james', 'dallas', 100, 200, 300)
    test4(name='jones', email='jones@xmpl.com')
    test4('smith', 'washington', 100, 200, state='texas', country='USA')

if __name__=='__main__': main()