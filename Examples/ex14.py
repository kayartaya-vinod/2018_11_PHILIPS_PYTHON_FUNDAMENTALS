'''
ex14

Working with object properties
'''

class Book(object):
    def __init__(self, **kwargs):
        # following statements are using setter properties..
        self.title = kwargs.get('title')
        self.author = kwargs.get('author')
        self.price = kwargs.get('price')

    # following creates a readable property (getter)
    @property
    def title(self): return self.__title

    # for a readable property, we can also create a 
    # writable property (setter or mutator). A setter cannot
    # be created for a non existing getter
    @title.setter
    def title(self, value):             
        if type(value) != str: 
            raise TypeError('Title must be a string')
        if len(value) <2 or len(value)>50:
            raise ValueError('Title must be between 2 and 50 letters')

        self.__title = value
        # b1.title = 'Let us C again'
        # b1 is the invoking object, received as 'self'
        # the RHS 'Let us C again' is received as 'value'

    @property
    def author(self): return self.__author
        
    @author.setter
    def author(self, value):
        if value!=None and type(value)!=str:
            raise TypeError('Author must be a string')
        self.__author = value

    @property
    def price(self): return self.__price

    @price.setter
    def price(self, value):
        if value!=None and type(value) not in (int, float):
            raise TypeError('Price must be numeric')
        if value!=None and value<0:
            raise ValueError('Price cannot be negative')
        self.__price = value

    def __str__(self):
        # Python adds the '_Book' prefix to each of the
        # dunder attributes being accessed here
        return 'Book [Title={}, Author={}, Price={}]'.format(
            self.title, self.author, self.price)

def main():
    b1 = Book(title='Let us C', author='Yashwant', price=299)
    print('title is', b1.title)
    print(b1)
    b1.title = 'Let us C again'
    b1.author = 'Yashwanth Kanitkar'
    b1.price = 300
    print(b1)

    b2 = Book(title='C Pearls', author='Yashwanth Kanitkar', price=499)
    print(b2)

if __name__ == "__main__":
    main()