from src.GraphInterface import GraphInterface
from src.Vertices import Vertices
import random


#this is the class that represent Directed Weight Graph
class DiGraph(GraphInterface):
    global vertices
    global edges
    global modCounter
    global r_edges

    # this is the Digraph contructor
    def __init__(self):
        self.vertices = {}
        self.edges = {}
        self.r_edges = {}
        self.modCounter = 0

    # this function returns the amount of vertices in a graph
    def v_size(self) -> int:
        return len(self.vertices)

    # this function retruns the amount of edges in a graph
    def e_size(self) -> int:
        counter = 0
        for i in self.edges.keys():
            counter += len(self.edges.get(i))
        return counter

    # this function returns a dictionary of all the vertices that are in a graph
    def get_all_v(self) -> dict:
        return self.vertices

    # this function returns a dictionary of all the vertices connected from id1
    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.edges.get(id1)

    # this function returns a dictionary of all the vertices connected to id1
    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.r_edges.get(id1)

    # this function returns the mod Counter
    def get_mc(self) -> int:
        return self.modCounter

    # this functions add an edge to the graph if the edge does not exist
    def add_edges(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self.vertices.keys() or id2 not in self.vertices.keys() and weight <= 0:
            return False
        if id1 in self.edges.keys():
            if id2 in self.edges.get(id1):
                return False
            self.edges.get(id1).update({id2: weight})
            if id2 in self.r_edges.keys():
                self.r_edges.get(id2).update({id1: weight})
            else:
                self.r_edges[id2] = {id1, weight}
            self.modCounter += 1
            return True
        else:
            self.edges[id1] = {id2: weight}
            if id2 in self.r_edges.keys():
                self.r_edges.get(id2).update({id1: weight})
            else:
                self.r_edges[id2] = {id1: weight}
            self.modCounter += 1
            return True

    # this functions adds a vertice if it is not in the graph
    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.vertices.keys():
            return False
        for i in self.vertices.keys():
            if self.vertices.get(i).pos == pos:
                return False
        v = Vertices()
        v.set_id(node_id)
        if pos is None:
            x,y=random.uniform(0,55), random.uniform(0,55)
            Tuple=(x,y,0)
            v.pos=Tuple
        else:
            if type(pos) is str:
                v.pos=eval(pos)
            else:
                v.pos(pos)
        self.vertices[node_id]=v
        self.modCounter+=1
        return True

#this function removes an edge from the graph
    def remove_edge(self, node_id1:int, node_id2: int)-> bool:
        if node_id1 not in self.vertices.keys() or node_id2 not in self.vertices.keys():
            return False
        if node_id1 not in self.edges or node_id2 not in self.edges.get(node_id1):
            return False
        del(self.edges[node_id1][node_id2])
        del(self.r_edges[node_id2][node_id1])
        self.modCounter+=1
        return True

#this function remove a vertices from the graph
    def remove_node(self,node_id:int)-> bool:
        if node_id not in self.vertices.keys():
            return False
        if node_id in self.edges.keys():
            self.modCounter+= len(self.edges[node_id])
            del(self.edges[node_id])
        delete=[]
        for i in self.edges.keys():
            if node_id in self.edges.get(i).keys():
                delete.append(i)
        for i in delete:
            del self.edges[i][node_id]
            self.modCounter+=1
        delete.clear()
        for i in self.r_edges.keys():
            if node_id in self.r_edges.get(i).keys():
                delete.append(i)
        for i in delete:
            del self.r_edges[i][node_id]
        del(self.vertices[node_id])
        self.modCounter+=1
        return True

    #this function makes our grapgh into dictionary so we could save it as a json
    def to_dictionary(self)-> dict:
        result = {}
        edge_list=[]
        vertices_list=[]

        for s in self.edges.keys():
            for d in self.edges.get(s).keys():
                edge_list.append({"src":s,"w":self.edges.get(s).get(d),"dest":d})
        result["Edges"]=edge_list
        for i in self.vertices.keys():
            vertices_list.append({"pos":str(self.vertices.get(i).pos[0])+","+str(self.vertices.get(i).pos[1])+","+str(0),"id":i})
        result["Nodes"]=vertices_list