#User Experience is like so:
'''

'''

from db import *

def addperson(id, home, work, arrival, departure):
    inserttotable('vroom1.db', "people", [(id, home, work, arrival, departure)])
def fillcar(data):
    return [piece[0] for piece in data]

gendb('vroom1.db')
addtable('vroom1.db', 'people', 'id', 'home', 'work', 'arrival_time', "departure_time")
data = getfromdb('vroom1.db', 'people', 'home', 'Mersch')
car = fillcar(data)
print("vroom!", car)