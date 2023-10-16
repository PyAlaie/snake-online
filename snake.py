from coordinates import Coordinates

snakes_number = {
    1: [Coordinates(5,6), Coordinates(5,5), Coordinates(5,4)],
    2: [Coordinates(10,6), Coordinates(10,5), Coordinates(10,4)]
}

class Snake():
    def __init__(self, number, direction='d', lives=3):
        self.number = number
        self.coordinates = snakes_number[number].copy()
        self.direction = direction
        self.lives = lives
        self.point = 0
        self.grow_size = 0
        
    def move_snake(self):
        head = self.coordinates[0].copy()
            
        # Finding new head location
        if self.direction == 'w':
            head.x -= 1
        elif self.direction == 's':
            head.x += 1
        elif self.direction == 'd':
            head.y += 1
        elif self.direction == 'a':
            head.y -= 1
        
        self.coordinates.insert(0, head)
        
        if self.grow_size != 0:
            self.grow_size -= 1
        else:
            self.coordinates.pop(-1)
        
    def size(self):
        return len(self.coordinates)
    
    def change_direction(self, new_direction):
        if new_direction == 'w' and self.direction != "s":
            self.direction = 'w'
        elif new_direction == 'd' and self.direction != "a":
            self.direction = 'd'
        elif new_direction == 's' and self.direction != "w":
            self.direction = 's'
        elif new_direction == 'a' and self.direction != "d":
            self.direction = 'a'
            
    def head(self):
        return self.coordinates[0]
    
    def die(self):
        # should respawn and decrease live
        print("hit the wall")
        self.lives -= 1
        self.respawn()
    
    def respawn(self):
        self.coordinates = snakes_number[self.number].copy()