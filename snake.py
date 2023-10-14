class Snake():
    def __init__(self, coordinates, direction='a', lives=3):
        self.coordinates = coordinates
        self.direction = direction
        self.lives = lives
        
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
        
        print(head)
        self.coordinates.insert(0, head)
        self.coordinates.pop(-1)
        
    def size(self):
        return len(self.coordinates)
    
    def change_direction(self, new_direction):
        if new_direction == 'w':
            self.direction = 'w'
        elif new_direction == 'd':
            self.direction = 'd'
        elif new_direction == 's':
            self.direction = 's'
        elif new_direction == 'a':
            self.direction = 'a'