

'''
this class will hold all the information for an agent in the game:
id: the id of the agent
value:the value of the agent
src:where the agent currently is
dest: where the agent is currently headed, stores -1 if the agent has no destenation
speed: the speed of the agent
pos: where the agent is currntly positioned in the graph
'''
class GameAgent():
    def __init__(self,id, value,src,dest,speed,pos):
        self.id=id
        self.value=value
        self.src=src
        self.dest=dest
        self.speed=speed
        self.pos=pos
        self.my_target=None

    def get_id(self):
        return self.id

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest

    def get_speed(self):
        return self.speed

    def get_pos(self):
        return self.pos

    def set_target(self,pokemon):
        self.my_target=pokemon

    def get_target(self):
        return self.my_target

    def set_path(self,path):
        self.my_path = path

    def get_path(self):
        return self.my_path



