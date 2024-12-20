class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass
        
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

point1 = point(10, 20)
point.x = 11 # This will change the value of x for all instances of the class
print(point1.x) 