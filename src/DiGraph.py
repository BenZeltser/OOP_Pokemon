from src.GraphInterface import GraphInterface
from src.Vertices import Vertices


#this is the class that represent Directed Weight Graph
class DiGraph(GraphInterface):
    global vertices
    global edges
    global modCounter


#this is the Digraph contructor
    def __init__(self):
        self.vertices = {}
        self.edges = {}
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


#this function returns a dictionary of the all vertices connected from id1
    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.edges.get(id1)


