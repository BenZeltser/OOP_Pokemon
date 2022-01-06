import time
import GraphInterface
import json

from src.Edge import Edge


from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph

'''Graph Algo class implements GraphAlgoInterface'''

class GraphAlgo(GraphAlgoInterface):

    myGraph=DiGraph()
    TL_Sort=[]
    SSC=[]
    '''Constructor'''

    def __init__(self,Digraph=myGraph):
        '''New Graph'''
        self.myGraph = DiGraph()
        self.myGraph= Digraph
        self.TL_Sort=[]
        self.SSC=[]

    '''Get'''

    def get_graph(self) -> GraphInterface:
        return self.myGraph


    '''Load'''

    def load_from_json(self, file_name: str) -> bool:
        try:
            '''Open file as read'''
            with open(file_name, 'r') as f:
                load = json.load(f)
                '''Init graph instance'''
                self.__init__()
                self.myGraph=DiGraph()
                '''Iterate through nodes'''
                for i in load.get("Nodes"):
                    self.myGraph.add_node(i.get("id"), i.get("pos"))
                for i in load.get("Edges"):
                    self.myGraph.add_edge(i.get("src"), i.get("dest"),i.get("w"))
                return True
        except Exception as e:
            return False

    '''Save'''
    def save_to_json(self, file_name:str)-> bool:
        try:
            with open(file_name,"w") as f:
                json.dump(self.myGraph.to_dictionary(),indent=4,fp=f)
            return True
        except Exception as e:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        v_List=self.shortest_path_list(id1,id2)
        vertices_keys=[]
        for v in v_List:
            vertices_keys.append(v.id)
        distance=self.shortest_path_distance(id1,id2)
        return distance,vertices_keys






