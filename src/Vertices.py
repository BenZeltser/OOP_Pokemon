import random
import time


class Vertices:

    def __init__(self, pos, id):
        self.pos = pos
        self.id = id
        variables = pos.split(',')
        self.x = variables[0]
        self.y = variables[1]
        self.z = variables[2]

    def __str__(self):
        return ('ID: ' + str(self.id) + '\n' + 'pos' + str(self.x) + ',' + str(self.y))

    def getX(self):
        return self.x

    def getY(self):
        return self.y

