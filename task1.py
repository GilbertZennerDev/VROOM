#User Experience is like so:
'''
run the program:
people get filled into fitting cars
the program outputs a json of cars with ids of people

Step 1: Collect Key Worker Information
Step 2: Build Homogeneous Travel Groups
Step 3: Dynamic Reassignment

'''

from db import *
import random as r

DBNAME = 'vroom1.db'
PEOPLE_TABLE = 'people'
CAR_LIMIT = 4 #people per car

def addperson(home, work, arrival, departure):
    inserttotable(
        'vroom1.db',
        "people",
        [(home, work, arrival, departure)],
        cols=['home', 'work', 'arrival', 'departure']
    )

def fillcar(data):
    return [piece[0] for piece in data]

def give_rnd_car_limit():
    return r.randint(6, 6)

def fillcars(home, arrival):
    people = getfromdb(DBNAME, PEOPLE_TABLE, 'home', home, 'arrival', arrival)
    people = [str(person[0]) for person in people]
    print(people)
    cars = []
    while len(people):
        current_car_size = give_rnd_car_limit()
        if len(people) > current_car_size:
            tmp = people[:current_car_size]
            idstr = '.'.join(tmp)
            cars.append(idstr)
            people = people[current_car_size:]
        else:
            idstr = '.'.join(people)
            cars.append(idstr)
            people = []
    print(cars)
    return cars

gendb(DBNAME)
addtable(DBNAME, PEOPLE_TABLE, 'home', 'work', 'arrival', 'departure')
#addperson('Mersch', 'Esch', '9', '16')
#addperson('Mersch', 'Esch', '9', '16')
car1 = fillcar(getfromdb(DBNAME, PEOPLE_TABLE, 'home', 'Mersch', 'arrival', '8'))
car2 = fillcar(getfromdb(DBNAME, PEOPLE_TABLE, 'home', 'Mersch', 'arrival', '9'))
#print("all", getfromdb(DBNAME, PEOPLE_TABLE, 'home', 'Mersch', 'arrival', '9'))
cars = fillcars('Mersch', '9')
print(cars)