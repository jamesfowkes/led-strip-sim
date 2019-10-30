class LED:
    
    def __init__(self, r):
        self.r = r
        
    def draw(self, x, y, colorval):
        fill(colorval)
        circle(x, y, self.r)
        
