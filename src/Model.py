import json
from types import SimpleNamespace

import pygame

from src.Button import Button


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

    def SplitPos(self, n):
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