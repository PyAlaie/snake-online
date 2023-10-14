from snake import Snake
from coordinates import Coordinates
import time

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
    
    def print_raw_map(self):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.map[i][j] == 0: #blank
                    print(' ', end='')
                elif self.map[i][j] == 1: #wall
                    print('X', end='')
            print()
            
    def print_map(self, snake_map):
        for i in snake_map:
            for j in i:
                print(j, end='')
            print()
    
    def generate_full_map(self, snakes):
        res = []
        for row in self.map:
            temp = []
            for col in row:
                if col == 0:
                    temp.append(" ")
                elif col == 1:
                    temp.append("X")
            res.append(temp)
        
        for snake in snakes:
            for coord in snake.coordinates:
                res[coord.x][coord.y] = "S"
                
        return res
            

class Game():
    def __init__(self, clients, refresh_rate=0.5, map_size=(30,30)):
        self.clients = clients
        self.refresh_rate = refresh_rate
        self.map = Snake_map(map_size)
        
    
    def run_game(self):
        while(1):
            snakes = [snake.coordinates for snake in self.clients]
            self.map.print_map(self.map.generate_full_map(snakes))
            time.sleep(self.refresh_rate)
    