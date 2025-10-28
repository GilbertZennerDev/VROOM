#User Experience is like so:
'''
run the program:
people get filled into fitting cars
the program outputs a json of cars with ids of people
'''

from db import *

def addperson(home, work, arrival, departure):
    inserttotable(
        'vroom1.db',
        "people",
        [(home, work, arrival, departure)],
        cols=['home', 'work', 'arrival_time', 'departure_time']
    )
def fillcar(data):
    return [piece[0] for piece in data]

gendb('vroom1.db')
addtable('vroom1.db', 'people', 'home', 'work', 'arrival_time', 'departure_time')
#addperson('Mersch', 'Esch', '8', '16')
#addperson('Mersch', 'Esch', '8', '16')
data = getfromdb('vroom1.db', 'people', 'home', 'Mersch')
car = fillcar(data)
print("vroom!", car)