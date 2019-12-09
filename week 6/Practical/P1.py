class circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
    
    def getDesc(self):
        print("A", self.color, "cirlce with raiud", self.radius)
    
x = circle(10, "green")

x.getDesc()