import time
import GraphInterface
import json
from matplotlib import pyplot as plt

from src.Edge import Edge

start = time.time()

from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph

'''Graph Algo class implements GraphAlgoInterface'''

class GraphAlgo(GraphAlgoInterface):

    '''Constructor'''

    def __init__(self, myGraph: DiGraph = DiGraph()):
        '''New Graph'''
        self.myGraph = myGraph
        print(start-time.time())

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


    '''Save'''

    def save_to_json(self, file_name: str) -> bool:

        try:
            start = time.time()
            '''Create Dict parameters (dynamic ds)'''
            jdict = {'Edges': [], 'Nodes': []}

            '''Open (create) Json file as write'''
            with open(file_name, 'w') as f:

                '''Iterate in a nested loop. \n
                   Append edges.'''

                for i in self.get_graph().get_all_v().keys():
                    for j,k in self.get_graph().all_in_edges_of_node(i).items():
                        jdict['Edges'].append(
                            {'src': i, 'dest': j, 'w': k})


                '''append nodes'''

                for i in self.get_graph().get_all_v().values():
                    jdict['Nodes'].append(
                        {'id':i.key}
                    )

                '''Apply the data to the file'''
                size = len(jdict)
                out = json.dumps(jdict, allow_nan=True, indent=size)
                f.write(out)

                '''-> Condit'''
                print("save:")
                print(start - time.time())
                return True

        except:
            raise NotImplementedError

    '''Plot Graph'''

    def plot_graph(self) -> None:
        X = []
        Y = []
        all_nodes = self.myGraph.get_all_v()
        for x in range(len(self.myGraph.get_all_v())):
            node = all_nodes[x]
            X.append(node.getX())
            Y.append(node.getY())
        plt.plot(X, Y)
        plt.plot(X, Y, 'ro')
        plt.show()


