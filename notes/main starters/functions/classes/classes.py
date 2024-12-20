class Point:
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.y = 1
print(point2.y)
#print(point2.x) # AttributeError: 'Point' object has no attribute 'x' completley diffrent from other