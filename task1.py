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
    cars = [[home, arrival]]
    if not len(people): cars.append('no_people'); return cars
    car_id = 0
    while len(people):
        current_car_size = give_rnd_car_limit()
        if len(people) > current_car_size:
            tmp = people[:current_car_size]
            idstr = '.'.join(tmp) + f';{str(current_car_size)}-{str(car_id)}'
            cars.append(idstr)
            people = people[current_car_size:]
        else:
            idstr = '.'.join(people) + f';{str(current_car_size)}-{str(car_id)}'
            cars.append(idstr)
            people = []
        car_id += 1
    return cars

def get_time_id(id, allcars):
    id = str(id)
    for i, cars in enumerate(allcars):
        for car in cars:
           if id in car:
                return i
    return -1

def get_slot_id(id, allcars):
    time_id = get_time_id(id, allcars)
    id = str(id)
    car = allcars[time_id]
    for i, slot in enumerate(car, start=1):
        if id in slot:
            return slot.split('-')[1], time_id
    return -1

def dynamic_shift(id, allcars, old_arrival, new_arrival):
    # I just need to remove the id from the old idstr, put it into a new one and update cars
    '''
    steps:
    1. Get the old cars array
    2. remove the id from the string
    3. Update the car
    4. Get the new cars array
    5. Insert id where space
    6. Update the new car
    '''
    id = str(id)
    slot_id, time_id = get_slot_id(id, allcars)
    print('slot', slot_id, 'time', time_id)
    oldstr = allcars[int(time_id)][int(slot_id) + 1]
    print(oldstr)
    car_limit = oldstr.split(';')[1]
    print('car_limit:', car_limit)
    oldstr = oldstr.split(';')[0]
    print(oldstr)
    oldstr = oldstr.split('.')
    print(oldstr)
    print(id)
    oldstr.pop(oldstr.index(str(id)))
    print(".".join(oldstr))
    allcars[int(time_id)][int(slot_id) + 1] = oldstr
    print(allcars)
    pass

gendb(DBNAME)
addtable(DBNAME, PEOPLE_TABLE, 'home', 'work', 'arrival', 'departure')
#addperson('Mersch', 'Esch', '9', '16')
#addperson('Mersch', 'Esch', '9', '16')
#car1 = fillcar(getfromdb(DBNAME, PEOPLE_TABLE, 'home', 'Mersch', 'arrival', '8'))
#car2 = fillcar(getfromdb(DBNAME, PEOPLE_TABLE, 'home', 'Mersch', 'arrival', '9'))
#print("all", getfromdb(DBNAME, PEOPLE_TABLE, 'home', 'Mersch', 'arrival', '9'))
cars1 = fillcars('Mersch', '9')
cars0 = fillcars('Mersch', '8')
allcars = [cars0, cars1]
#print(cars0, cars1)
#dynamic_shift(6, cars, '9', 8)
'''print(allcars)
time_id = get_time_id(0, allcars)
print(time_id)'''
#slot_id = get_slot_id(7, allcars)
#print(slot_id)

dynamic_shift(7, allcars, '9', '8')