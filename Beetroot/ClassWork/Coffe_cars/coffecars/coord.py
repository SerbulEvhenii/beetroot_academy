import math


class CoordXY:
    '''
    lat, lon
    distance_to(self, other)

    todict
    restore
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def dict_cord(self):
        return {'x':self.x, 'y':self.y}

    def distance_to(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2   )

class Coord(CoordXY):
    pass
