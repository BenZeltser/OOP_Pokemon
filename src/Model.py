import json
from types import SimpleNamespace
from src import GamePokemon
import pygame
from src import GameAgent
from src.Button import Button
from src import GeoLocation


class Model:

    def __init__(self, client):
        self.client = client

    def loadPokemons(self):
        pokemons = json.loads(self.client.get_pokemons(), object_hook=lambda d: SimpleNamespace(**d)).Pokemons
        pokemons = [p.Pokemon for p in pokemons]
        return pokemons
        # Load the Agents - need to load everytime to get realtime-pos

    def loadAgents(self):
        agents = json.loads(self.client.get_agents(), object_hook=lambda d: SimpleNamespace(**d)).Agents
        agents = [agent.Agent for agent in agents]
        return agents

    def SplitPos(n):
        x, y, _ = n.pos.split(',')
        n.pos = SimpleNamespace(x=float(x), y=float(y))  #####

    def getInfo(client):
        getinfo = client.get_info()
        info = json.loads(getinfo)
        getinfo = client.get_info()
        info = json.loads(getinfo)

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

        pokemon_message = jpokemon
        is_logged_in_message = jis_logged_in
        moves_message = jmoves
        grade_message = jgrade
        game_level_message = jgame_level
        max_user_level_message = jmax_user_level
        id_message = jid
        graph_message = jgraph
        agents_message = jagents

        ans = []
        ans.append(pokemon_message)
        ans.append('')
        ans.append(moves_message)
        ans.append(grade_message)
        ans.append(game_level_message)
        ans.append(max_user_level_message)
        ans.append(id_message)
        ans.append(agents_message)
        ans.append(graph_message)

        return ans

    def stopGUI(client, upload: bool, stopButton):
        pos = pygame.mouse.get_pos()
        if stopButton.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                if not upload:
                    client.stop_connection()
                else:
                    client.stop()

    def sendAgents(client):
        """
        returns: json str of agents. for example:\n
        {
            "Agents":[
                {
                    "Agent":
                    {
                        "id":0,
                        "value":0.0,
                        "src":0,
                        "dest":1,
                        "speed":1.0,
                        "pos":"35.18753053591606,32.10378225882353,0.0"
                    }
                }
            ]
        }
        """
        clients = client.get_agents()  # get Agents Json ####
        client_obj = json.loads(clients)
        ans = {'id': client_obj['Agents'][0]['Agent']['id'],
               'value': client_obj['Agents'][0]['Agent']['value'],
               'src': client_obj['Agents'][0]['Agent']['src'],
               'dest': client_obj['Agents'][0]['Agent']['dest'],
               'speed': client_obj['Agents'][0]['Agent']['speed'],
               'pos': client_obj['Agents'][0]['Agent']['pos']}
        return ans

    def sendPokemons(client):
        pokemons = client.get_pokemons()  # get Agents Json ####
        pokemon_obj = json.loads(pokemons)
        ans = []
        i = 0
        for p in pokemons:
            ans[i] = {'value': pokemon_obj['Pokemons'][0]['Pokemon']['value'],
                   'type': pokemon_obj['Pokemons'][0]['Pokemon']['type'],
                   'pos': pokemon_obj['Pokemons'][0]['Pokemon']['pos']}
            i = i+1
        return ans

    def Json2List(client):
        ans = []
        xrPokemons = client.get_pokemons()
        d = json.loads(xrPokemons)

        #Add all pokemons to list
        for pokemon in d["Pokemons"]:
            value = pokemon['Pokemon']['value']
            type = pokemon['Pokemon']['type']
            pos = pokemon['Pokemon']['pos']

            current = GamePokemon(value,type,pos)

    def buildAgents(self, agents):
        agnetList = []
        for agent in agents:
            '''New Agent'''
            id = agent.id
            value = agent.value
            src = agent.src
            dest = agent.dest
            speed = agent.speed
            pos = agent.pos

            coordinates = pos.split(',')
            location = GeoLocation.GeoLocation(coordinates[0],coordinates[1],coordinates[2])
            #Agent instance

            current = GameAgent.GameAgent(id,value,src,dest,speed,location)
            agnetList.append(current)
        return agnetList

    def buildPokemons(pokemons):
        pokemonList = []
        pokemons=client.get_pokemons()
        ans = json.loads(pokemons)
        for i in ans["Pokemons"]:
            tempDict=i.get("Pokemon")
            value = tempDict.get('value')
            ttype = tempDict.get('type')
            pos = tempDict.get('pos')

            coordinates = pos.split(',')
            location = GeoLocation.GeoLocation(coordinates[0],coordinates[1],coordinates[2])
            #Agent instance

            current = GamePokemon.gamePokemon(value,ttype,location)
            pokemonList.append(current)
        return pokemonList

    def placeAgents(client, agentList ,pokemonList):
        for i in range(len(agentList)):
            client.add_agent("{\"id\":"+pokemonList[i].get_src()+"}")
        for i in range(len(agentList)):
            agentList[i].set_target(pokemonList[i])

