import copy
from led import LED
from task import Task
from point import Point
from collections import deque

class LEDStrip:
    
    def __init__(self, start, angle, nleds, spacing, task_period):
        self.start = start
        self.xstep = spacing * cos(radians(angle))
        # Invert Y because processing's coordinate system is backwards
        self.ystep = -(spacing * sin(radians(angle)))
        self.leds = [LED(5)] * nleds
        self.end = Point(self.start.x + (self.xstep * nleds), self.start.y + (self.ystep * nleds))
        self.next = None
        self.colours = deque([color(0)] * nleds)
        self.task = Task(task_period)
    
    def attach(self, second_strip):
        self.next = second_strip
        second_strip.start = self.end

    def fill(self, colour):
        self.colours = deque([colour] * len(self.leds))
        
    def setColours(self, colours):
        self.colours = copy.copy(colours)
        if self.next is not None:
            self.next.setColours(colours)
            
    def pushColour(self, colour):
        c = self.colours.pop()
        self.colours.appendleft(colour)
        if self.next is not None:
            self.next.pushColour(c)
    
    def run(self, next_colour):
        if self.task.run():
            self.pushColour(next_colour)
            
    def draw(self):
        x, y = self.start.x, self.start.y
        for led, led_color in zip(self.leds, self.colours):
            led.draw(x, y, led_color)
            x += self.xstep
            y += self.ystep
        
        if self.next is not None:
            self.next.draw()
            
    def ledCount(self):
        my_count = len(self.leds)
        if self.next is not None:
            my_count += self.next.ledCount()
        return my_count

    def setPeriod(self, period):
        self.task.setPeriod(period)
    
    @classmethod
    def pointToPoint(cls, p1, p2, spacing, task_period):
        nleds = int(p1.distanceTo(p2) / spacing)
        angle = p1.angleTo(p2)
        return cls(p1, angle, nleds, spacing, task_period)
        
