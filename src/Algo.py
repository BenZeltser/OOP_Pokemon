import json


from src.DiGraph import DiGraph, Node
from src.main import myGraph


class Algo(myGraph):

    def __init__(self):
        self.__node_data = None
        self.__myGraph = None


    def init(self, g):
        self.myGraph=g

    def getGraph(self):
        return self.myGraph


    def isConnected(self):
        print("isConnected")
        if self.myGraph is None:
            return True
        c = self.myGraph.getV()
        if len(c) == 0 or len(c) == 1:
            return True
        #       print("edg size"+myGraph.edgeSize())
        #        print("ndsize"+myGraph.nodeSize())
        if self.__myGraph.edgeSize()< 2*self.__myGraph.nodeSize()-2:
            #            print("error")
            return False
        c_list = list(c)
        groupNodes = {}
        for i in c_list:
            groupNodes.update({i.getKey(): i}) #putting the collection in a hashmap
        first = c_list[0].getKey()
        if myGraph is None or myGraph.getV() is None or myGraph.getE(first) is None or not myGraph.getE(first).stream().findFirst().isPresent():
            #if there's no neighbor to the node than it's not a connected graph by definition,
            print("is mygraph== null "+myGraph is None)
            print("is mygraph.getV== null "+myGraph.getV() is None)
            print("is mygraph.getV== null "+myGraph.getE(first) is None)
            return False
        else:
            #NEEDED FIX DVI
            #             src = first
            #            value = myGraph.getE(first).stream().findFirst().get().getDest()
            #             dest = value
            node = None
            # check if graph is SC
            #Init the DFS on graph
            for node in myGraph.getV():
                ( node).setTagB(0) #meaning it has NOT been yet visited
            self.DFS(myGraph, first) # DFS
            for nodea in myGraph.getV():
                node= nodea
                print(node.getTagB())
                #this graph is not connected.
                if node.getTagB()!=1:
                    print("lala")
                    return False

            src =0
            dest =0
            newGraph = DiGraph()
            for nd in myGraph.getV():
                newGraph.addNode(nd) #add the nodes to the new graph
                for edge in myGraph.getE(nd.getKey()):
                    src=edge.getSrc()
                    dest=edge.getDest()
                    newGraph.connect(dest, src, 1) # default weight,no impact on this DFS algorithm

            for node in newGraph.getV():
                ( node).setTagB(0)

            self.DFS(newGraph, first) #Do DFS again
            for nodea in newGraph.getV():
                node= nodea
                if node.getTagB()!=1:
                    #                  print("lolo")
                    return False
        # iterate through the nodes in to check
        return True


        # DFS

    def DFS(directed_weighted_graph: DiGraph(),  vertex):
            neilist = []
            (myGraph.getNode(vertex)).setTagB(1) # 1- mark it as a VISITED node
            #initate a list of the neighbors of Vertex:
            for edge in myGraph.getE(vertex):
                #get node data from edge_data
                #           print("the node is "+vertex)
                #            print("the dest of edge is "+edge.getDest())
                neilist.append(myGraph.getNode(edge.getDest()))
            node = None
            for nodea in neilist:
                node= nodea
                if node.getTagB() != 1:
                    DiGraph.DFS(myGraph, node.getKey())

#Shortestpath
def shortestPathDist(self, src, dest):
    if src==dest:
        return 0
    aj =self.shortestPath(src,dest)
    #  print(aj.size())
    if not aj:
        #         print("empty")
        return -1 #EMPTY aj ===  NO PATH FROM SRC TO DEST
    weight = ((aj[len(aj) - 1])).getTagB()
    return weight

#Dijkstra algo
def shortestPath(self, src, dest):

    c =myGraph.getV()
    parents = {}
    myListg = []
    list = list(c)
    groupNodes = {}
    for i in list:
        groupNodes.update({i.getKey(): i})

    if dest== src:
        myListg.append(groupNodes[src])
        return myListg

    if src not in groupNodes.keys() or dest not in groupNodes.keys():
        #         print("doesnt exist")
        return myListg

    for key in groupNodes.keys():
        groupNodes[key].setInfo("")
        ((groupNodes[key])).setTagB(float('inf'))
        parents.update({key: None})

    ((groupNodes[src])).setTagB(0)
    q = []
    for key in groupNodes.keys():
        q.add(groupNodes[key])
    minDist =float('inf')
    minKey =-1
    dist =0
    minNode =None

    while not q.isEmpty():
        for node in q:
            if ((node)).getTagB()<=minDist:
                minDist=((node)).getTagB()
                minKey=node.getKey()
                minNode=node
        q.remove(minNode)
        for edge in myGraph.getE(minKey):
            def __init__(self):
                self.myListg = None

          ###Needed Fix DVI
            if neighbor_node in q:
                dist = minDist + myGraph.getEdge(minKey,
                                                 neighbor_node.getKey()).getWeight()  #dist
                if dist < neighbor_node.getTagB():
                    (neighbor_node).setTagB(dist)  # it's the path's weight sum, why is it double?
                    # because it's requested like that. TO GO THROUGH LATER
                    neighbor_node.setInfo(str(minKey))
                #   }

            minDist = float('inf')
              # finished while
            desty = dest

            while (groupNodes.get(desty)).getTagB() != 0 and groupNodes.get(desty).getInfo() != "":
                # of 0 from itself.
                self.myListg.add(groupNodes.get(desty))
                desty = int(groupNodes.get(desty).getInfo())  # get the "father"
            self.myListg.add(groupNodes.get(src))
            #                for (int i=0; i<myListg.size(); i++) {
            #                        print(myListg.get(i).getKey())
            #                }

            '''[::-1] REVERSE THE LIST'''

            myListg[::-1]
            if self.myListg.get(self.myListg.size() - 1).getKey() != dest:
                self.myListg.clear()

            return self.myListg
            #NEEDED FIX DVI
            def save(file):
            try:
                graph = JSONObject()
                allNodes = JSONArray()
                allEdges = JSONArray()
                if myGraph.getV() is not None:
                    for node in myGraph.getV():
                        n = JSONObject()
                        n.put("id", node.getKey())
                        n.put("pos",
                              node.getLocation().x() + "," + node.getLocation().y() + "," + node.getLocation().z())
                        allNodes.put(n)
                    graph.put("Nodes", allNodes) #Map nodes
                    for node in myGraph.getV():
                        if myGraph.getE(node.getKey()) is not None:
                            for edge in myGraph.getE(node.getKey()):
                                e = JSONObject()
                                e.put("src", edge.getSrc())
                                e.put("dest", edge.getDest())
                                e.put("w", edge.getWeight())
                                allEdges.put(e)
                    graph.put("Edges", allEdges)
                saved = FileWriter(file)
                saved.write(str(graph)) #Write to graph
                saved.flush()
                saved.close()
            except:
                return False
            return True

def load(self, file):
    try:
        g = DiGraph()
        file = input("enter file name")
        jsonString = file.useDelimiter("\\A").next()
        file.close()
        graph = JSONObject(jsonString)
        allNodes = graph.getJSONArray("Nodes")
        allEdges = graph.getJSONArray("Edges")
        i = 0
        while i< allNodes.length():
            n = allNodes.getJSONObject(i)
            node = Node(n.getInt("id"))
            str = n.getString("pos")
            arr = str.split(",")
            x = float(arr[0])
            y = float(arr[1])
            z = float(arr[2])
            geo = self(x, y, z)
            node.setLocation(geo)
            g.addNode(node)
            i += 1
        i = 0
        while i< allEdges.length():
            e = allEdges.getJSONObject(i)
            g.connect(e.getInt("src"), e.getInt("dest"), e.getDouble("w"))
            i += 1
        self.init(g)
    except:
        return False
    return True