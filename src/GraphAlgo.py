import time
from collections import deque

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


    '''returns a list of the shortest path'''
    def shortest_path_list(self,s,d):
        group_Vertices=self.myGraph.vertices
        p={}
        result=[]
        tempD=d
        if s==d:
            result.append(group_Vertices.get(s))
            return result
        if s not in group_Vertices.keys() or d not in group_Vertices.keys():
            return result
        group_Vertices_Keys=group_Vertices.keys()
        for k in  group_Vertices_Keys:
            (group_Vertices.get(k).setTB(float('inf')))
            group_Vertices.get(k).set_info("")
            p[k]=None
        (group_Vertices.get(s)).set_TB(0)
        q= deque()
        group_Vertices_Keys=group_Vertices.keys()
        for k in group_Vertices_Keys:
            q.append(group_Vertices.get(k))
        min_Dist=float('inf')
        min_id= -1
        distance=0
        min_vertice=None
        while q:
            for v in q:
                if v.getTB()<= min_Dist:
                    min_Dist=v.getTB()
                    min_id=v.getId()
                    min_vertice=v
            q.remove(min_vertice)
            if (self.myGraph.all_out_edges_of_node(min_id)):
                for k in self.myGraph.all_out_edges_of_node(min_id).keys():
                    neighbor_vertice=self.myGraph.vertices.get(k)
                    if (neighbor_vertice in q):
                        distance=min_Dist+self.myGraph.all_out_edges_of_node(min_id).get(k)
                        if(distance<neighbor_vertice.get_TB()):
                            (neighbor_vertice.set_info(str(min_id)))
            min_Dist= float('inf')
        tempD=d
        while group_Vertices.get(tempD).getTB()!= 0 and group_Vertices.get(tempD).getInfo()!="":
            result.append(group_Vertices.get(tempD))
            tempD=int(group_Vertices.get(tempD).getInfo())
        result.append(group_Vertices.get(s))
        result.reverse()
        if result[len(result)-1].getID()!=d:
            result.clear()
        return result

    '''returns the weight of the shortest path'''
    def shortest_path_distance(self,s,d):
        if s==d:
            return 0
        SP_list=self.shortest_path_list(s,d)
        if not (SP_list):
            return float('inf')
        w= SP_list.pop(len(SP_list)-1).getTB()
        return w

    '''returns a distance and a list of the shortest path'''
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        v_List=self.shortest_path_list(id1,id2)
        vertices_keys=[]
        for v in v_List:
            vertices_keys.append(v.id)
        distance=self.shortest_path_distance(id1,id2)
        return distance,vertices_keys






