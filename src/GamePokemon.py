from src import Edge


class gamePokemon():

    def __init__(self,value,type,pos):
        self.value = value
        self.type = type
        self.pos = pos

    def get_value(self):
        return self.value

    def get_type(self):
        return self.type

    def get_pos(self):
        return self.pos

    def set_edge(self,edge):
        self.edge=edge

    def get_edge(self):
        return self.edge

    def get_src(self):
        return self.edge.src

    def get_dest(self):
        return self.edge.dest