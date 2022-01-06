import json
from types import SimpleNamespace

import pygame

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src import Model
from src.client import Client
from src import GUI

"""
    This class is represents the Controller
    within the MVC Design Pattern

    MVC Explained in 4 Minutes:
    https://www.youtube.com/watch?v=DUg2SWWK18I&t=150s
"""
# Create a Graph instance
myGraph = DiGraph()
# Create a Graph Algo instance
algo = GraphAlgo(myGraph)
# Set and Connect to the server
PORT = 6666
HOST = '127.0.0.1'
client = Client()
client.start_connection(HOST, PORT)

# Get data from the server
pokemons = client.get_pokemons()  # get Pokemon Json ####
pokemons_obj = json.loads(pokemons, object_hook=lambda d: SimpleNamespace(**d))  ####
graph_json = client.get_graph()  # Per Scenario
graph = json.loads(graph_json, object_hook=lambda json_dict: SimpleNamespace(**json_dict))  #####
FONT = pygame.font.SysFont('Segoe UI Black', 20, bold=False)

pokemons = client.get_pokemons()  # get Pokemon Json ####
pokemons_obj = json.loads(pokemons, object_hook=lambda d: SimpleNamespace(**d))  ####
graph_json = client.get_graph()  # Per Scenario
graph = json.loads(graph_json, object_hook=lambda json_dict: SimpleNamespace(**json_dict))

# Split pos (x,y)
for n in graph.Nodes:
    x, y, _ = n.pos.split(',')
    n.pos = SimpleNamespace(x=float(x), y=float(y))

# Get data proportions
min_x = min(list(graph.Nodes), key=lambda n: n.pos.x).pos.x  ###
min_y = min(list(graph.Nodes), key=lambda n: n.pos.y).pos.y  ###
max_x = max(list(graph.Nodes), key=lambda n: n.pos.x).pos.x  ###
max_y = max(list(graph.Nodes), key=lambda n: n.pos.y).pos.y  ###

# Add agent(s)
client.add_agent("{\"id\":0}")
# client.add_agent("{\"id\":1}")
# client.add_agent("{\"id\":2}")
# client.add_agent("{\"id\":3}")

# this command starts the server - the game is running now
client.start()  ####
client.log_in("313327579")  ###
p = client.get_pokemons()  ###
g = GUI.GUI(client)
