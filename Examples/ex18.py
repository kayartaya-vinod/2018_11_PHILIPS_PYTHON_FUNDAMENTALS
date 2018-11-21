'''
ex18

Working with generators
'''

def fibo(limit=10):
    print('Starting the fibonacii series...')
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    a, b = -1, 1
    for i in range(limit):
        c = a + b
        yield c
        # print(c)
        a, b = b, c

def main():
    f = fibo(15) # returns a generator object; the actual function is not called yet!
    # print('type(f) is', type(f))
    print(next(f)) # calls the actual function here, and comes back with the yielded value
    print(next(f))
    print(next(f))
    print('rest of the values...')
    for n in f: print(n)


if __name__ == "__main__": main()