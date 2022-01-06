import random
import time


class Vertices:

    id=0
    count=0
    w=0.0
    i=""
    t=0
    p=None
    v="false"
    S_t=0.0
    c=""
    t=0
    dub=0
    position=()

#this is the constructor of a vertices
    def __init__(self):
        self.id=self.count
        Vertices.count+=1
#print the vertice
    def __repr__(self):
        return str(self.id)+" "+ str(self.position)


#set the id of the vertice

    def set_id(self, key:int):
        self.id = key

#copies a vertice
    def copy_vertices(self,v):
        self.id=v.get_id()
        self.w=v.get_weight()
        self.i=v.get_info()
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
        return self.i
#set the info of a vertice
    def set_info(self,i):
        self.i=i

#get the tag of a vertice
    def get_tag(self):
        return self.t

#set the that of a vertice
    def set_tag(self,t:float):
        self.t=t

#get the second tag of a vertice
    def get_s_t(self):
        return self.s_t

#set the second tag of a vertice
    def set_s_t(self,t):
        self.s_t=t

#set the value of dub for the vertice
    def set_dub(self,e):
        self.dub=e

#set the counter of the vertice
    def set_counter(self,counter):
        self.count=counter