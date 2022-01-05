import time
import GraphInterface
import json

from src.Edge import Edge


from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph

'''Graph Algo class implements GraphAlgoInterface'''

class GraphAlgo(GraphAlgoInterface):

    '''Constructor'''

    def __init__(self, myGraph: DiGraph = DiGraph()):
        '''New Graph'''
        self.myGraph = myGraph

    '''Get'''

    def get_graph(self) -> GraphInterface:
        start = time.time()
        return self.myGraph
        print(get)
        print(start - time.time())

    '''Load'''

    def load_from_json(self, file_name: str) -> bool:
        try:
            start = time.time()
            '''Open file as read'''
            with open(file_name, 'r') as f:
                print("Loaded")
                load = json.load(f)
                '''Init graph instance'''
                myGraph= DiGraph()

                '''Iterate through nodes'''
                Nodes = load['Nodes']
                for node in Nodes:
                    print("***added Node***\n")
                    print("pos: " + str(node["pos"]))
                    print("id: " + str(node["id"]))
                    print("\n")
                    if "pos" not in node:
                        myGraph.add_node(node["id"])

                '''Iterate through edges'''
                for edge in load['Edges']:
                    current = Edge(edge["src"],edge["dest"],edge["w"])
                    src = current.getSRC()
                    w = current.getWeight()
                    dest = current.getDest()
                    myGraph.connect(src,dest,w)
                    print("***added Edge***\n")
                    print("Src: "+str(src))
                    print("Weight: " + str(w))
                    print("Dest: " + str(dest))
                    print("\n")
                '''Attribute the graph'''
                self.myGraph = myGraph
                f.close()
                return True
        except:
            raise NotImplementedError


