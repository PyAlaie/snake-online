from snake import Snake
from coordinates import Coordinates
import time, random

class Snake_map():
    def __init__(self, size) -> None:
        self.size = size
        self.map = []
        self.create_map()
        self.apple = None
        
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
            
    def print_map(self, snake_map, *args, **kwargs):
        for i in snake_map:
            for j in i:
                print(j, end='')
            print()
        print(args, kwargs)        
    
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
            print(snake.coordinates[0])
            for coord in snake.coordinates:
                res[coord.x][coord.y] = "S"
        
        if self.apple != None:
            res[self.apple.x][self.apple.y] = 'A'
                
        return res

class Game():
    def __init__(self, clients, refresh_rate=0.2, map_size=(25,30)):
        self.clients = clients
        self.refresh_rate = refresh_rate
        self.map = Snake_map(map_size)
        
    def check_any_collision(self):
        snakes = [client.snake for client in self.clients]
        
        # checking if there is a collision with wall
        for snake in snakes:
            head = snake.head()
            if self.map.map[head.x][head.y] == 1:
                print('snake died')
                snake.die()
                
        # checking if there is a collision with other snakes
        all_coords = []
        for snake in snakes:
            for coord in snake.coordinates:
                all_coords.append(coord)
                
        def good_count(head):
            res = 0
            for c in all_coords:
                if c.x == head.x and c.y == head.y:
                    res += 1
            return res
        for snake in snakes:
            head = snake.head()
            if good_count(head) >= 2:
                print('snake died')
                snake.die()
    
    def generate_apple(self):
        # generate apple if there is none
        all_coords = [client.snake.coordinates for client in self.clients]
        all_coords = [coord for coord in all_coords]
        
        while 1:
            rand_x = random.randint(2, self.map.size[0]-2)
            rand_y = random.randint(2, self.map.size[1]-2)
            
            if Coordinates(rand_x, rand_y) not in all_coords:
                self.map.apple = Coordinates(rand_x, rand_y)
                break
        
    
    def eat_apple(self):
        if self.map.apple != None:
            snakes = [client.snake for client in self.clients]
            for snake in snakes:
                head = snake.head()
                print(self.map.apple)
                print(head)
                if head.x == self.map.apple.x and head.y == self.map.apple.y:
                    self.map.apple = None
                    snake.point += 1
                    snake.grow_size += 1
                    break
    
    def run_game(self):
        while(1):
            snakes = [client.snake for client in self.clients]
            generated_map = self.map.generate_full_map(snakes)
            self.map.print_map(generated_map, self.clients[0].snake.direction)
            
            # broadcasting the map
            for client in self.clients:
                client.send_map_to_client(generated_map)
                
            # making the snakes move, and other events to happen
            for snake in snakes:
                snake.move_snake()
            self.check_any_collision()
            self.eat_apple()
            if self.map.apple == None:
                self.generate_apple()
                
            # sleeping
            time.sleep(self.refresh_rate)
    