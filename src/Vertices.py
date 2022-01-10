import random
import time


class Vertices:

    id=0
    count=0
    w=0.0
    inf=""
    t=0
    p=None
    v="false"
    TB=0.0
    c=""
    time=0
    pos=()

#this is the constructor of a vertices
    def __init__(self):
        self.id=self.count
        Vertices.count+=1
#print the vertice
    def __repr__(self):
        return str(self.id)+" "+ str(self.pos)


#set the id of the vertice

    def set_id(self, key:int):
        self.id = key

#copies a vertice
    def copy_vertices(self,v):
        self.id=v.get_id()
        self.w=v.get_weight()
        self.inf=v.get_info()
        self.t=v.get_tag()

#returns the id of a vertice
    def get_id(self):
        return self.id

#returns the weight of a vertice
    def get_weight(self):
        return self.w

#set the weight of a vertice
    def set_weight(self,w:float):
        self.w=w

#get the info of a vertice
    def get_info(self):
        return self.inf

#set the info of a vertice
    def set_info(self,i):
        self.inf=i

#get the tag of a vertice
    def get_tag(self):
        return self.t

#set the that of a vertice
    def set_tag(self,t:float):
        self.t=t

#get the second tag of a vertice
    def get_TB(self):
        return self.TB

#set the second tag of a vertice
    def set_TB(self,t):
        self.TB=t

#set the value of dub for the vertice
    def set_dub(self,e):
        self.dub=e

#set the counter of the vertice
    def set_counter(self,counter):
        self.count=counter