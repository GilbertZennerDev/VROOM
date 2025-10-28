#User Experience is like so:
'''
run the program:
people get filled into fitting cars
the program outputs a json of cars with ids of people
'''

from db import *

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

def fillcars(people):
    #I need to save the ids in the car. I could use a string, separate the ids per .
    people = [person[0] for person in people]
    cars = []
    idstr = ''
    for i, person in enumerate(people):
        if i % (CAR_LIMIT + 1) == 0 and i > 0:
            idstr += str(person) + '.'
            cars.append(idstr)
            idstr = ''
        else:
            idstr += str(person) + '.'
    if len(idstr): cars.append(idstr)
    #print(cars)
    car_str = ""
    for i, car in enumerate(cars):
        car_str += str(i) + ":" + cars[i] + '\n'
    return car_str

gendb(DBNAME)
addtable(DBNAME, PEOPLE_TABLE, 'home', 'work', 'arrival', 'departure')
#addperson('Mersch', 'Esch', '9', '16')
#addperson('Mersch', 'Esch', '9', '16')
car1 = fillcar(getfromdb(DBNAME, PEOPLE_TABLE, 'home', 'Mersch', 'arrival', '8'))
car2 = fillcar(getfromdb(DBNAME, PEOPLE_TABLE, 'home', 'Mersch', 'arrival', '9'))
print("all", getfromdb(DBNAME, PEOPLE_TABLE, 'home', 'Mersch', 'arrival', '9'))
car_str = fillcars(getfromdb(DBNAME, PEOPLE_TABLE, 'home', 'Mersch', 'arrival', '9'))
print(car_str)