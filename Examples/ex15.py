'''
ex15

member functions in a class
'''
import math

class Circle(object):
    def __init__(self, radius=1.0):
        self.radius = radius # assignment via property
    
    @property
    def radius(self): return self.__radius

    @radius.setter
    def radius(self, value):
        if type(value) not in (int, float):
            raise TypeError('Radius must be numeric')
        if value < 0: 
            raise ValueError('Radius cannot be negative')

        self.__radius = value

    # readonly property
    @property
    def AREA(self):
        return math.pi * self.radius * self.radius

    def __str__(self):
        return 'Circle [radius={}, area={}]'.format(
            self.radius, self.AREA)

    def __lt__(self, value):
        if type(value) == Circle:
            return self.radius < value.radius
        elif type(value) in (int, float):
            return self.radius < value
        else:
            raise TypeError('Invalid value for < operator')

    def __add__(self, value):
        if type(value) == Circle:
            return Circle(self.radius + value.radius)
        elif type(value) in (int, float):
            return Circle(self.radius + value)
        else:
            raise TypeError('Invalid value for + operator')

    def __iadd__(self, value):
        # __i*__ functions should return self
        if type(value) in (int, float):
            self.radius += value
        elif type(value) == Circle:
            self.radius += value.radius
        else:
            raise TypeError('Invalid type for +=')
        return self

def main():
    c1 = Circle()
    c2 = Circle(12.34)
    c3 = Circle(1.234)
    print(c1)
    print(c2)
    print(c3)
    c2 += 5.0
    print(c2)
    c2 += c3
    print(c2)

    print('c2 < c3 is', c2 < c3)
    print('c2 < 15.0 is', c2 < 15.0)

    c4 = c2 + c3 # c4 is a new Circle object with radius added from both c2 and c3
    print(c4)
    c5 = c2 + 5.0 # c5 is a new Circle object with c2.radius + 5.0
    print(c5)

if __name__ == "__main__": main()