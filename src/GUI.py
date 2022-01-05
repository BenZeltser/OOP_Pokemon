"""
@author AchiyaZigi
OOP - Ex4
Very simple GUI example for python client to communicates with the server and "play the game!"
"""
from types import SimpleNamespace
from client import Client
import json
from pygame import gfxdraw
import pygame
from pygame import *

# init pygame
from src import Button

WIDTH, HEIGHT = 1080, 720

# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'
pygame.init()
# Dont touch

screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()

# Create client API
client = Client()
client.start_connection(HOST, PORT)

pokemons = client.get_pokemons()  # get Pokemon Json
pokemons_obj = json.loads(pokemons, object_hook=lambda d: SimpleNamespace(**d))
# convert to a json and then print the pokemons
#print("Pokemon!" + pokemons)

graph_json = client.get_graph()  # Per Scenario

FONT = pygame.font.SysFont('Segoe UI Black', 20, bold=False)
# load the json string into SimpleNamespace Object

# Load the Graph
graph = json.loads(
    graph_json, object_hook=lambda json_dict: SimpleNamespace(**json_dict))

# Split pos (x,y)
for n in graph.Nodes:
    x, y, _ = n.pos.split(',')
    n.pos = SimpleNamespace(x=float(x), y=float(y))

# get data proportions
min_x = min(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
min_y = min(list(graph.Nodes), key=lambda n: n.pos.y).pos.y
max_x = max(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
max_y = max(list(graph.Nodes), key=lambda n: n.pos.y).pos.y


def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimentions
    """
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


# decorate scale with the correct values

def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height() - 50, min_y, max_y)


radius = 30

##Some cases have more than 1 agent - only high ones (11+)

client.add_agent("{\"id\":0}")
# client.add_agent("{\"id\":1}")
# client.add_agent("{\"id\":2}")
# client.add_agent("{\"id\":3}")

# this commnad starts the server - the game is running now
client.start()
client.log_in("313327579")
p = client.get_pokemons()

"""
The code below should be improved significantly:
The GUI and the "algo" are mixed - refactoring using MVC design pattern is required.
"""

###**********GUI BEGINS**********

while client.is_running() == 'true':
    # Refresh = movement
    # Load the pokemons - need to load everytime to get realtime-pos
    pokemons = json.loads(client.get_pokemons(),
                          object_hook=lambda d: SimpleNamespace(**d)).Pokemons
    pokemons = [p.Pokemon for p in pokemons]
    for p in pokemons:
        x, y, _ = p.pos.split(',')
        p.pos = SimpleNamespace(x=my_scale(
            float(x), x=True), y=my_scale(float(y), y=True))
        # Load the Agents - need to load everytime to get realtime-pos
    agents = json.loads(client.get_agents(),
                        object_hook=lambda d: SimpleNamespace(**d)).Agents
    agents = [agent.Agent for agent in agents]
    for a in agents:
        x, y, _ = a.pos.split(',')
        a.pos = SimpleNamespace(x=my_scale(
            float(x), x=True), y=my_scale(float(y), y=True))
    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    # refresh surface
    screen.fill(Color(133, 22, 55))
    bg = pygame.image.load("forest.jpg")
    screen.blit(bg, (0, 0))

    ''''''''''''''

    '''
    Show the elements at the GUI
    '''

    getinfo = client.get_info()
    info = json.loads(getinfo)
    getinfo = client.get_info()
    info = json.loads(getinfo)
    # info is dict

    # GET Info from the dict

    jpokemon = info['GameServer']['pokemons']
    jis_logged_in = info['GameServer']['is_logged_in']
    jmoves = info['GameServer']['moves']
    jgrade = info['GameServer']['grade']
    jgame_level = info['GameServer']['game_level']
    jmax_user_level = info['GameServer']['max_user_level']
    jid = info['GameServer']['id']
    jgraph = info['GameServer']['graph']
    jgraph = jgraph[5:]
    jagents = info['GameServer']['agents']

    # Set each info in variable
    # Info to the screen. Present to the screen. show the info
    pokemon_message = jpokemon
    is_logged_in_message = jis_logged_in
    moves_message = jmoves
    grade_message = jgrade
    game_level_message = jgame_level
    max_user_level_message = jmax_user_level
    id_message = jid
    graph_message = jgraph
    agents_message = jagents

    # Display text
    pokemon = FONT.render("Pokemons: " + str(pokemon_message), True, (34, 139, 34))
    rect = pygame.Rect(700, 5, 40, 40)
    screen.blit(pokemon, rect)

    jjislogged = FONT.render("isLoggedIn: " + str(is_logged_in_message), True, (34, 139, 34))
    rect = pygame.Rect(700, 25, 40, 40)
    screen.blit(jjislogged, rect)

    displayGraph = FONT.render("Graph: " + str(graph_message), True, (34, 139, 34))
    rect = pygame.Rect(700, 45, 40, 40)
    screen.blit(displayGraph, rect)

    level = FONT.render("Level: " + str(game_level_message), True, (34, 139, 34))
    rect = pygame.Rect(700, 65, 40, 40)
    screen.blit(level, rect)

    grade = FONT.render("Grade: " + str(grade_message), True, (34, 139, 34))
    rect = pygame.Rect(890, 5, 40, 40)
    screen.blit(grade, rect)

    moves = FONT.render("moves: " + str(moves_message), True, (34, 139, 34))
    rect = pygame.Rect(890, 25, 40, 40)
    screen.blit(moves, rect)

    jjagents = FONT.render("agents: " + str(agents_message), True, (34, 139, 34))
    rect = pygame.Rect(890, 45, 40, 40)
    screen.blit(jjagents, rect)

    jjmaxLevel = FONT.render("Max level: " + str(max_user_level_message), True, (34, 139, 34))
    rect = pygame.Rect(890, 65, 40, 40)
    screen.blit(jjmaxLevel, rect)



    # Print each value

    #print("Iterate\n\n\n")
    #print("Pokemon: " + str(jpokemon))
    # print("is_logged_in: " + str(jis_logged_in))
    # print("moves: " + str(jmoves))
    # print("grade: " + str(jgrade))
    # print("game_level: " + str(jgame_level))
    # print("max_user_level: " + str(jmax_user_level))
    # print("id: " + str(jid))
    # print("graph: " + str(jgraph))
    # print("agents: " + str(jagents))

    ''''''''''''''

    #Draw STOP Button

    stopImg = pygame.image.load('STOP.png').convert_alpha()
    stopButton = Button.Button(800,550,stopImg,0.25)
    drawn = stopButton.draw(screen)

    pos = pygame.mouse.get_pos()

    # check mouseover and clicked conditions
    if stopButton.rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:
            try:
                client.stop_connection()
                raise Exception("STOPPED")
            except Exception as err:
                print("STOPPED")
            finally:
                print("STOPPED")

    # draw nodes
    for n in graph.Nodes:
        x = my_scale(n.pos.x, x=True)
        y = my_scale(n.pos.y, y=True)

        # its just to get a nice antialiased circle
        gfxdraw.filled_circle(screen, int(x), int(y),
                              radius, Color(64, 80, 174))
        gfxdraw.aacircle(screen, int(x), int(y),
                         radius, Color(255, 255, 255))

        # draw the node id
        id_srf = FONT.render(str(n.id), True, Color(255, 255, 255))
        rect = id_srf.get_rect(center=(x, y))
        screen.blit(id_srf, rect)

    # draw edges
    for e in graph.Edges:
        # find the edge nodes
        src = next(n for n in graph.Nodes if n.id == e.src)
        dest = next(n for n in graph.Nodes if n.id == e.dest)

        # scaled positions
        src_x = my_scale(src.pos.x, x=True)
        src_y = my_scale(src.pos.y, y=True)
        dest_x = my_scale(dest.pos.x, x=True)
        dest_y = my_scale(dest.pos.y, y=True)

        # draw the line
        pygame.draw.line(screen, Color(0, 0, 0),
                         (src_x, src_y), (dest_x, dest_y), 2)

    pokeball = pygame.image.load("pokeball.png")

    # draw agents
    for agent in agents:
        screen.blit(pokeball,
                    (int(agent.pos.x), int(agent.pos.y)))
    # draw pokemons (note: should differ (GUI wise) between the up and the down pokemons (currently they are marked in the same way).

    sqruitle = pygame.image.load("squirtle.jpg")

    for p in pokemons:
        screen.blit(sqruitle, (int(p.pos.x), int(p.pos.y)))

    # update screen changes
    display.update()

    # refresh rate
    clock.tick(60)

    # choose next edge
    # ALGO PART

    for agent in agents:
        if agent.dest == -1:
            next_node = (agent.src - 1) % len(graph.Nodes)
            client.choose_next_edge(
                '{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(next_node) + '}')
            ttl = client.time_to_end()

            # print(ttl, client.get_info())
            #print(ttl)

    client.move()

# game over:
