'''
ex01

A very basic Python script example
'''

# Any variables, functions, classes defined in this module
# become the "attributes" of the module
name = 'Vinod Kumar K'
city = 'Bengaluru'
state = 'Karnataka'
email = 'vinod@vinod.co'
phone = '9731424784'

print('My name is ' + name)
print('I live in %s, %s' % (city, state))
print('My email is {} and phone is {}'.format(email, phone))

# __name__ is a builtin attribute for any module
# The value of this is assigned by Python runtime
# When a module is imported via "import" command,
# the value of __name__ is the name of the file.
# When the module is run as a progarm script, 
# the value of __name__ is "__main__"
print('Name of this module is', __name__)
