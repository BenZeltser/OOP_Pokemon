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
    def v_size (self):
        return len(self.vertices)




