import time

class Edge:

    def __init__(self, src, w, dest):

        self.src=src
        self.w=w
        self.dest=dest

    def __str__(self):
        return ('src: '+str(self.src)+'\n'+'w'+str(self.w)+'\n'+' dest:'+str(self.dest))

    def getSRC(self):
        return self.src

    def getDest(self):
        return self.dest

    def getWeight(self):
        return self.w