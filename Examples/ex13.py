'''
ex13

Passing initalization values while creating an object
'''

class Person(object):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.city = kwargs.get('city', 'Bangalore')
        self.email = kwargs.get('email')

    def __str__(self):
        # this function should return a textual representation
        # of the object
        return 'Person [Name={}, City={}, Email={}]'.format(self.name, self.city, self.email)


def main():
    p1 = Person(name='Vinod', email='vinod@vinod.co')
    p2 = Person(name='John', city='Dallas')
    p3 = Person(name='Jane')

    # Since the member data is accessible using p1,
    # we may assign even wrong values also; should be avoided
    p3.city = 1234

    print(p1) # same as print(p1.__str__()) and p1 is implicitly passed as the argument to __str__()
    print(p2)
    print(p3)

if __name__ == "__main__":
    main()