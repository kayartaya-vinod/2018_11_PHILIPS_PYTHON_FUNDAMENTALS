'''
ex12

Working with class and object's data members
'''

class Person(object):

    def __init__(self):
        # self is a reference to a new empty object
        # using the dot operator, we can add new data members
        # to that object
        self.name = None
        self.city = 'Bangalore'
        self.email = None

def main():
    p1 = Person()
    print(p1.__dict__)
    
    p1.name = 'Vinod'
    p1.email = 'vinod@vinod.co'

    print(p1.__dict__)

if __name__ == "__main__": main()