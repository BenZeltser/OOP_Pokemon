import json
from src import client
from src import GraphAlgoInterface
from src import GameAgent
from src import GamePokemon
from src import GraphInterface


class GameAlgo():
    '''
            '{"agent_id":0, "next_node_id":1}'.
    '''

    '''this function checks if each agent cought at least 1 pokemon'''

    def did_catch_first(self, pokemon_List, agent_List):
        for i in range(len(agent_List)):
            id = str(agent_List[i].get_id())
            dest = str(agent_List[i].get_target().get_dest())
            string = '{"agent_id":' + id + ', "next_node_id":' + dest + '}'
            client.choose_next_edge(string)
        client.move()
        for i in range(len(agent_List)):
            agent_List[i].set_target(pokemon_List[i])

    def arrange_pokemons(pokemon_List):
        new_pokemon_list = []
        max_value = 0
        print(max_value)
        max_index = 0
        for i in range(len(pokemon_List)):
            for j in range(len(pokemon_List)):
                if pokemon_List[j].get_value() > max_value:
                    max_value = pokemon_List[j].get_value()
                    max_index = j
            new_pokemon_list.append(pokemon_List[max_index])
            pokemon_List.pop(max_index)
            max_value = 0
        pokemon_List=new_pokemon_list
        return pokemon_List

    def catch_pokemons(self, pokemon_List, agent_List, algo):
        for i in range(len(agent_List)):
            dist = float('inf')
            target_index = 0
            for j in range(len(pokemon_List)):
                temp = algo.shortest_path(agent_List[i].get_src(), pokemon_List[j].get_src())
                if temp[0] < dist:
                    dist = temp[0]
                    target_index = j
            temp = algo.shortest_path(agent_List[i].get_src(), pokemon_List[target_index].get_src)
            agent_List[i].set_path(temp[1])
            agent_List[i].set_target(pokemon_List[target_index])
        for i in range(len(agent_List)):
            if len(agent_List[i].get_path()) == 1:
                id = str(agent_List[i].get_id())
                dest = str(agent_List[i].get_target().get_dest())
                string = '{"agent_id":' + id + ', "next_node_id":' + dest + '}'
                client.choose_next_edge(string)
            else:
                id = str(agent_List[i].get_id())
                dest = str(agent_List[i].get_path()[0].get_key())
                string = '{"agent_id":' + id + ', "next_node_id":' + dest + '}'
                client.choose_next_edge(string)
        client.move()

    def did_catch(self, agent_List):
        for i in range(len(agent_List)):
            if agent_List[i].get_dest != -1:
                return False
        return True



