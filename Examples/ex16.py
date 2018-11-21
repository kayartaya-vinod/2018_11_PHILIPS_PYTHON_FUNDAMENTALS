'''
ex16

Working with aggregation and inheritance
'''
class Address(object):
    street = None
    city = None
    state = None

class Person(object):
    name = None
    email = None
    address = Address() # aggregation/composition (HAS-A)

    def __init__(self):
        print('Person.__init__ called')

class Employee(Person): # inheritance (IS-A)
    id = None
    salary = 20000
    department = None
    def __init__(self):
        print('Employee.__init__ called')

def main():
    Employee()
    # Python creates an empty object and invokes 
    # Employee.__init__ for initialization.
    # If Employee class does not have an __init__, it would
    # have inherited from Person. If Person class did not have
    # __init__, it would have inherited from 'object' class

if __name__ == "__main__": main()