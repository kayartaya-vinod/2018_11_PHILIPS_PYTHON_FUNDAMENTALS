'''
ex11

work with classes and constructor
'''

class Person(object):
    def __init__(self):
        print('Person object is initialized')
        print('id of self is', id(self))

def main():
    p1 = Person()
    # since Person is a class and not a function, the statement
    # Person() is an instruction to Python RT to create an object
    # and then call the object's __init__ passing the reference
    # of the newly created object as its parameter. This is done
    # for object's initialization purpose only. After that, the
    # same reference is given to p1

    print('p1 is an object of', type(p1))
    print('id of p1 is', id(p1))

    # though this is possible, we are not expected to call this
    # Python's philosophy is developers are matured enough to
    # follow its guidelines. Dunder attributes should not be
    # invoked.
    p1.__init__()
    Person.__init__(p1)

if __name__=='__main__': main()