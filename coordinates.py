class Coordinates():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
    def copy(self):
        return Coordinates(self.x, self.y)
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(object, Coordinates):
            return self.x == object.x and self.y == object.y
        return False