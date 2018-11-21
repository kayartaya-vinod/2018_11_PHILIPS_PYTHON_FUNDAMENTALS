'''
ex10

Working with user defined classes and objects of the same
'''

class Person(object):
    # variables defined at the class level are shared among
    # objects of this class
    meta = {'name': 'Person', 'createdBy': 'Vinod'}
    # In Java/C# these variables are equivalent to 'static' members
    # A copy of this reference is kept in each object

    # When the variables are immutable, it might look different
    name = ''
    city = 'Bangalore'
    email = ''

def main():
    p1 = Person()
    print(p1.meta)
    p2 = Person()
    p2.meta['name'] = 'class Person'
    print(p1.meta)

    p1.name = 'Vinod'
    p1.email = 'vinod@vinod.co'

    p2.name = 'Shyam'
    p2.email = 'shyam@exmaple.com'
    p2.city = 'Shimoga'

    print('Name = {}, city={}, email={}'.format(p1.name, p1.city, p1.email))
    print('Name = {}, city={}, email={}'.format(p2.name, p2.city, p2.email))
    print('id of p1.meta is', id(p1.meta))
    print('id of p2.meta is', id(p2.meta))

if __name__=='__main__': main()

