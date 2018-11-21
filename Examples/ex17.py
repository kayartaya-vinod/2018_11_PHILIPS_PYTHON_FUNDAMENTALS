'''
ex17

Initializing data members in inheritance scenario
'''

def id_generator(seed=1):
    id = seed
    while True:
        yield id
        id += 1

resource_id = id_generator(1001)

class Resource(object):
    def __init__(self, **kwargs):
        self.id = next(resource_id)
        self.description = kwargs.get('description', 'Just another resource :)')

class Person(object):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')

    def log(self):
        print('Name   = {}'.format(self.name))
        print('Email  = {}'.format(self.email))

class Employee(Resource, Person):
    def __init__(self, **kwargs):
        # super().__init__(**kwargs)
        Resource.__init__(self, **kwargs)
        Person.__init__(self, **kwargs)
        
        self.salary = kwargs.get('salary')
        self.department = kwargs.get('department')

    def log(self):
        print('Id     = {}'.format(self.id))
        Person.log(self)
        print('Descr  = {}'.format(self.description))
        print('Salary = {}'.format(self.salary))
        print('Dept   = {}'.format(self.department))
        print('-'*50)

def main():
    e1 = Employee(name='John', email='john@xmpl.com', salary=22000, department='ADMIN')
    e2 = Employee(name='Kiran', salary=25000, department='PRODUCTION')

    e1.log()
    e2.log()

if __name__ == "__main__": main()