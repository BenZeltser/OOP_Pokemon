import json
import random
import matplotlib.pyplot as plt
import numpy as np


class Node:
    def __init__(self, id, pos: tuple):
        self.id = id
        self.pos = pos

    def __repr__(self):
        return f"id={self.id} pos={self.pos}"


class DiGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, id, pos=(0, 0)):
        self.nodes[id] = Node(id, pos)
        self.edges[id] = {}

    def connect(self, src, w, dest):
        if src in self.nodes and dest in self.nodes:
            # if src not in self.edges:
            #     self.edges[src] = {}
            self.edges[src][dest] = w

    def __str__(self):
        return f"nodes:{self.nodes}\nedges:{self.edges}"

    def get_all_v(self):
        return self.nodes

    def get_all_edges(self):
        return self.edges
'''def plot(g:DiGraph):
    for src in g.nodes.values():
        x,y=src.pos
        plt.plot(x,y,markersize=10,marker="o",color="blue")
        plt.text(x, y, str(src.id), color="red", fontsize=12)
        for dest,w in g.edges[src.id].items():
            his_x,his_y=g.nodes[dest].pos
            plt.annotate("",xy=(x,y),xytext=(his_x,his_y),arrowprops=dict(arrowstyle="<-"))
    plt.show()
'''

