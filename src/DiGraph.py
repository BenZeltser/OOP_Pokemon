from src.GraphInterface import GraphInterface
from src.Vertices import Vertices


#this is the class that represent Directed Weight Graph
class DiGraph(GraphInterface):
    global vertices
    global edges
    global modCounter
    global r_edges


#this is the Digraph contructor
    def __init__(self):
        self.vertices = {}
        self.edges = {}
        self.r_edges={}
        self.modCounter=0

#this function returns the amount of vertices in a graph
    def v_size (self) ->int:
        return len(self.vertices)

#this function retruns the amount of edges in a graph
    def e_size (self)-> int:
        counter=0
        for i in self.edges.keys():
            counter+= len(self.edges.get(i))
        return counter

#this function returns a dictionary of all the vertices that are in a graph
    def get_all_v(self) -> dict:
        return self.vertices


#this function returns a dictionary of all the vertices connected from id1
    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.edges.get(id1)

#this function returns a dictionary of all the vertices connected to id1
    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.r_edges.get(id1)
    
#this functionreturn the mod Counter 
    def get_mc(self) -> int:
        return self.modCounter

#this functions add an edge to the graph if the edge does not exist
    def get_edges(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self.vertices.keys() or id2 not in self.vertices.keys() and weight<=0:
            return False
        if id1 in self.edges.keys():
            if id2 in self.edges.get(id1):
                return False
            self.edges.get(id1).update({id2: weight})
            if id2 in self.r_edges.keys():
                self.r_edges.get(id2).update({id1:weight})
            else:
                self.r_edges[id2]={id1,weight}
            self.modCounter+=1
            return True
        else:
            self.edges[id1]={id2:weight}
            if id2 in self.r_edges.keys():
                self.r_edges.get(id2).update({id1: weight})
            else:
                self.r_edges[id2]= {id1: weight}
            self.modCounter+=1
            return True

