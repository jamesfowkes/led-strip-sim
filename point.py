class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def angleTo(self, other):
        return degrees(atan2(self.y-other.y, other.x-self.x))
    
    def distanceTo(self, other):
        return dist(self.x, self.y, other.x, other.y)
