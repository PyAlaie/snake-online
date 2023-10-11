from snake import Snake
from coordinates import Coordinates

class Snake_map():
    def __init__(self, size) -> None:
        self.size = size
        self.map = []
        self.create_map()
        
    def create_map(self):
        for i in range(self.size[0]):
            self.map.append([0 for j in range(self.size[1])])
            
        # putting the walls
        for i in range(self.size[0]):
            self.map[i][0] = 1
            self.map[i][self.size[1]-1] = 1
        for i in range(self.size[1]):
            self.map[0][i] = 1
            self.map[self.size[0]-1][i] = 1
    
    def print_blank_map(self):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.map[i][j] == 0: #blank
                    print(' ', end='')
                elif self.map[i][j] == 1: #wall
                    print('X', end='')
            print()
            
    def print_full_map(self, snakes):
        pass
            

class Game():
    def __init__(self, clients, refresh_rate=0.5, map_size=(30,30)):
        self.clients = clients
        self.refresh_rate = refresh_rate
        self.map = Snake_map(map_size)
        
        self.map.print_blank_map()
    
    