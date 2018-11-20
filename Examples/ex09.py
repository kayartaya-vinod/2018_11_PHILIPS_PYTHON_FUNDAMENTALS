'''
ex09

working with files in different methods
'''
import json

def fileread_ex01(filename='ex09.py'):
    file = None
    try:
        file = open(filename)
        while True:
            line = file.readline()
            if line=='': break
            print(line, end='')

        print()
    except FileNotFoundError:
        print('File %s does not exist' % filename)
    finally:
        if file!=None: file.close()
        # if 'close' in dir(file): file.close()

def fileread_ex02(filename='ex09.py'):
    file = open(filename)
    
    # for line in file.readlines():
    for line in file:  # file objects are iterable
        print(line, end='')

    file.close()
    print()

def fileread_ex03(filename='ex09.py'):
    with open(filename) as file:
        for line in file:
            print(line, end='')


def csv2json(filename):
    people = []
    with open(filename, encoding='utf-8') as file:
        headers = file.readline().strip().split(',')
        for line in file:
            values = line.strip().split(',')
            d = dict(zip(headers, values))
            people.append(d)
    
    output_filename = filename[:-4] + '.json'
    with open(output_filename, 'wt', encoding='utf-8') as file:
        json.dump(people, file, indent=3)

    print('File %s created' % output_filename)


def csv2json_v2(filename):
    with open(filename, encoding='utf-8') as file:
        headers = file.readline().strip().split(',')
        data = [line.strip().split(',') for line in file]
        people = [dict(zip(headers, d)) for d in data]
        
        output_filename = filename[:-4] + '.json'
        with open(output_filename, 'wt', encoding='utf-8') as file:
            json.dump(people, file, indent=3)

if __name__=='__main__':
    csv2json_v2('people.csv')