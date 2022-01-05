import json
from types import SimpleNamespace


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

    def loadGraph(self):
        pass