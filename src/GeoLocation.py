import math

class GeoLocation():

    '''
    init a GeoLocation instance
    create the geoLocation as a tuple
    '''
    def __init__(self,x,y,z):
       self.coords=(x,y,z)

    '''
    returns the x value of the geoLocation
    '''
    def get_X(self)-> float:
        return self.coords[0]

    '''
    returns the y value of the geoLocation
    '''
    def get_y(self)-> float:
        return self.coords[1]

    '''
    returns the z value of the geoLocation
    '''
    def get_z(self)-> float:
        return self.coords[2]

    '''
    returns the distance between one geolocation and another
    '''
    def distance_from(self, g)-> float:
        return math.sqrt((math.pow(self.coords[0]-g.get_x(),2)+math.pow(self.coords[1]-g.get_y(),2)+math.pow(self.coords[2]-g.get_z(),2)),2)
