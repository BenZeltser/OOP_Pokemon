import json
from src import client
from src import GraphAlgoInterface
from src import GameAgent
from src import GamePokemon
from src import GraphInterface
from src import GeoLocation
from src.Edge import Edge


class GameAlgo():
    EPS1 = 0.001
    EPS2 = EPS1 * EPS1
    EPS = EPS2

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

    def arrange_pokemons(self, pokemon_List):
        new_pokemon_list = []
        max_value = pokemon_List[0].get_value()
        max_index = 0
        for i in range(len(pokemon_List)):
            for j in range(len(pokemon_List)):
                if pokemon_List[j].get_value > max_value:
                    max_value = pokemon_List[j].get_value
                    max_index = j
            new_pokemon_list.append(pokemon_List[max_index])
            pokemon_List.pop(max_index)
            max_value = pokemon_List[0].get_value()
        return new_pokemon_list

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

    def update_pokemon_edge(self,pokemon,graph):
        node_dict=graph.get_all_v()
        for i in node_dict.keys():
            edge_dict=graph.all_out_edges_of_node(node_dict.get(i).get_id)
            for j in edge_dict.keys():
                if (node_dict.get(i).get_id<edge_dict.get(j).get_id() and pokemon.get_type>0) or (node_dict.get(i).get_id>edge_dict.get(j).get_id() and pokemon.get_type<0):
                    src_pos=node_dict.get(i).pos
                    dest_pos=edge_dict.get(j).pos
                    src_geoLoc=GeoLocation.__init__(src_pos[0],src_pos[1],src_pos[2])
                    dest_geoLoc=GeoLocation.__init__(dest_pos[0],dest_pos[1],dest_pos[2])
                    total_distance=src_geoLoc.distance(dest_geoLoc)
                    distance1=src_geoLoc.distance(pokemon.get_pos())
                    distance2=pokemon.get_pos().distance(dest_geoLoc)
                    if total_distance> ((distance1+distance2)-self.EPS):
                        edge_added=Edge.__init__(node_dict.get(i).get_id,edge_dict.get(j).get_weight(),edge_dict.get(j).get_id())
                        pokemon.set_edge(edge_added)
                        return





