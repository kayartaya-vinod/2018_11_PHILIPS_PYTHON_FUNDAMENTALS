'''
ex06

A function to list all the regular attributes,
without any underscores
'''

def dir1(obj):
    return [at for at in dir(obj) if not at.startswith('_')]

if __name__=='__main__': 
    print(dir1(str))