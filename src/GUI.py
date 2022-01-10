"""
@author AchiyaZigi
OOP - Ex4
Very simple GUI example for python client to communicates with the server and "play the game!"
"""

'''

Within the MVC Design pattern, this class represents the 'View' Section.

Wikipedia:
https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller

Brief Video via Youtube about the subject:
https://www.youtube.com/watch?v=DUg2SWWK18I&t=4s

'''

from types import SimpleNamespace
from client import Client
import json
from pygame import gfxdraw
import pygame
from pygame import *

# init pygame
from src import Button
from src.Model import Model

WIDTH, HEIGHT = 1080, 720

PORT = 6666
HOST = '127.0.0.1'

'''
    *** Important Note to Code Reviewer ***
    
    small parts of the class are not Directly GUI related hence
    they implement the MVC Design Pattern with a positive required addition.
    
    that is due to the fact that In exercise 12 with Mr. Amichai Kafka
    he instructed to not change any of the code that is above this very
    doc that you are reading. 
    
    However, the MVC Design Pattern is respected by the separation below:
    -----------------------------------------------------------------------
    -Model - Primarily handles Data and Algorithm logic W
    -View - essentially the GUI
    -Controller - Handles the requests and user interaction (mostly main)
    -------------------------------------------------------------------------
'''
pygame.init()

screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()

# Begin Connection to init GUI - due to instructions in Row 35
client = Client()  ####
client.start_connection(HOST, PORT)  ####
'''Get elements to present them to the UI'''
pokemons = client.get_pokemons()  # get Pokemon Json ####
pokemons_obj = json.loads(pokemons, object_hook=lambda d: SimpleNamespace(**d))  ####
graph_json = client.get_graph()  # Per Scenario
graph = json.loads(graph_json, object_hook=lambda json_dict: SimpleNamespace(**json_dict))  #####
FONT = pygame.font.SysFont('Segoe UI Black', 20, bold=False)
#MODEL CLIENT
c = client.get_agents()
print("CLIENT AGENTS")
print(c)
client.add_agent("{\"id\":0}")
client.add_agent("{\"id\":1}")
client.add_agent("{\"id\":2}")
client.add_agent("{\"id\":3}")

# getinfo = client.get_info()
# info = json.loads(getinfo)

clients = client.get_agents()  # get Agents Json ####
client_obj = json.loads(clients)

                        # agent         attribute

for n in graph.Nodes:
    Model.SplitPos(n)

# Small snippet - can stay at the View despite being Model related
min_x = min(list(graph.Nodes), key=lambda n: n.pos.x).pos.x  ###
min_y = min(list(graph.Nodes), key=lambda n: n.pos.y).pos.y  ###
max_x = max(list(graph.Nodes), key=lambda n: n.pos.x).pos.x  ###
max_y = max(list(graph.Nodes), key=lambda n: n.pos.y).pos.y  ###


# Scale - Uses SCREEN hence GUI (View) Related by MVC StandPoint.

def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimensions
    """
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


def scalePokemon(pokemons):
    for p in pokemons:
        x, y, _ = p.pos.split(',')
        p.pos = SimpleNamespace(x=my_scale(
            float(x), x=True), y=my_scale(float(y), y=True))


def scaleAgents(agents):
    for agent in agents:
        x, y, _ = agent.pos.split(',')
        agent.pos = SimpleNamespace(x=my_scale(
            float(x), x=True), y=my_scale(float(y), y=True))


def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height() - 50, min_y, max_y)


radius = 30

##Some cases have more than 1 agent - only high ones (11+)

# Add agent
client.add_agent("{\"id\":0}")
client.add_agent("{\"id\":1}")
# client.add_agent("{\"id\":2}")
# client.add_agent("{\"id\":3}")

# this command starts the server - the game is running now
client.start()  ####
# client.log_in("313327579")  ###
p = client.get_pokemons()  ###

"""
The code below should be improved significantly:
The GUI and the "algo" are mixed - refactoring using MVC design pattern is required.
"""

while client.is_running() == 'true':
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    # Model Instance - MVC related!
    model = Model(client)

    pokemons = model.loadPokemons()
    agents = model.loadAgents()

    # scale pokemons, agents

    scalePokemon(pokemons)
    scaleAgents(agents)

    # refresh surface
    screen.fill(Color(133, 22, 55))
    bg = pygame.image.load("forest.jpg")
    screen.blit(bg, (0, 0))

    '''
    Show the elements at the GUI as print (if needed)
    '''
    #
    # getinfo = client.get_info()
    # info = json.loads(getinfo)
    # getinfo = client.get_info()
    # info = json.loads(getinfo)
    # # info is dict
    #
    # # GET Info from the dict
    #
    # jpokemon = info['GameServer']['pokemons']
    # jis_logged_in = info['GameServer']['is_logged_in']
    # jmoves = info['GameServer']['moves']
    # jgrade = info['GameServer']['grade']
    # jgame_level = info['GameServer']['game_level']
    # jmax_user_level = info['GameServer']['max_user_level']
    # jid = info['GameServer']['id']
    # jgraph = info['GameServer']['graph']
    # jgraph = jgraph[5:]
    # jagents = info['GameServer']['agents']
    #
    # # Set each info in variable
    # # Info to the screen. Present to the screen. show the info
    # pokemon_message = jpokemon
    # is_logged_in_message = jis_logged_in
    # moves_message = jmoves
    # grade_message = jgrade
    # game_level_message = jgame_level
    # max_user_level_message = jmax_user_level
    # id_message = jid
    # graph_message = jgraph
    # agents_message = jagents

    # Model gets the information while GUI presents it
    Messages = Model.getInfo(client)
    MessagesHeaders = ['Pokemons: ', 'isLogged: ', 'Moves: ', 'Grade: ', 'Level: ', 'MaxLevel: ', 'ID(Server)  ', 'Agents: ',
                       'Graph: ']
    # Client is attached to GUI according to Amichai Kafka
    ttl = client.time_to_end()

    for i in range(0, 4):
        SMessage = FONT.render(str(MessagesHeaders[i]) +str(Messages[i]), True, (34, 139, 34))
        rect = pygame.Rect(700, 5 + (i * 25), 40, 40)
        screen.blit(SMessage, rect)
    for i in range(5, 8):  # Shit X-Axis
        SMessage = FONT.render(str(MessagesHeaders[i]) + ": " + str(Messages[i]), True, (34, 139, 34))
        rect = pygame.Rect(840, (i - 4) * 25, 40, 40)
        screen.blit(SMessage, rect)

    SMessage = FONT.render("Time to end(ms): " + str(client.time_to_end()), True, (34, 139, 34))
    rect = pygame.Rect(840, 5, 40, 40)
    screen.blit(SMessage, rect)

    # Print each value

    # print("Iterate\n\n\n")
    # print("Pokemon: " + str(jpokemon))
    # print("is_logged_in: " + str(jis_logged_in))
    # print("moves: " + str(jmoves))
    # print("grade: " + str(jgrade))
    # print("game_level: " + str(jgame_level))
    # print("max_user_level: " + str(jmax_user_level))
    # print("id: " + str(jid))
    # print("graph: " + str(jgraph))
    # print("agents: " + str(jagents))

    # Draw STOP Button

    stopImg = pygame.image.load('STOP.png').convert_alpha()
    stopButton = Button.Button(800, 550, stopImg, 0.25)
    drawn = stopButton.draw(screen)

    Model.stopGUI(client, False, stopButton)

    # if button is clicked - stop the program
    # also, to send the results set mid param to True

    # draw nodes
    for n in graph.Nodes:
        x = my_scale(n.pos.x, x=True)
        y = my_scale(n.pos.y, y=True)

        # its just to get a nice antialiasing circle
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
        rect = pygame.Rect(int(agent.pos.x) - 25, int(agent.pos.y) - 25, 40, 40)
        jj = FONT.render("ID: " + str(agent.id), True, (0, 0, 0))
        screen.blit(jj, rect)
    # draw pokemons (note: should differ (GUI wise) between the up and the down pokemons (currently they are marked in the same way).

    sqruitle = pygame.image.load("squirtle.jpg")
    upArrow = pygame.image.load("UP.png")
    downArrow = pygame.image.load("DOWN.png")
    # Algo - REMOVE
    for p in pokemons:
        screen.blit(sqruitle, (int(p.pos.x), int(p.pos.y)))
        rect = pygame.Rect(int(p.pos.x) - 25, int(p.pos.y) - 25, 40, 40)
        jjj = FONT.render("Value: " + str(p.value), True, (0, 0, 255))
        screen.blit(jjj, rect)
        if (p.type > 0):
            # UP
            screen.blit(upArrow, ((int(p.pos.x) - 22), (int(p.pos.y)) + 10))
        else:
            # Down
            screen.blit(downArrow, ((int(p.pos.x) - 22), (int(p.pos.y)) + 10))

        # Up or Down:

        print(p.type)
    # update screen changes
    display.update()

    # refresh rate
    clock.tick(60)

    #choose next edge
    #ALGO PART

    for agent in agents:
        if agent.dest == -1:
            next_node = (agent.src - 1) % len(graph.Nodes)
            client.choose_next_edge(
                '{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(next_node) + '}')



            ttl = client.time_to_end()

            # print(ttl, client.get_info())

    client.move()

    '''
        Algo Call
    '''


# game over
