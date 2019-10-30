from led_strip import LEDStrip
from point import Point

TOTAL_TIME = 2000

led_strips = [LEDStrip(Point(50, y), 0, 15, 1000/60, 100) for y in range(100, 800, 100)]

START_COLOUR = color(192,0,0)
END_POINT = Point(600-50, 400)

for led_strip in led_strips:
    angled_strip = LEDStrip.pointToPoint(led_strip.end, Point(600-50, 400), 1000/60, 0)
    led_strip.attach(angled_strip)
    led_strip.fill(START_COLOUR)
    angled_strip.fill(START_COLOUR)
    led_strip.setPeriod(TOTAL_TIME/led_strip.ledCount())
    
def setup():
    size(620, 820)
        
def draw():
    background(205)
    fill(128)
    rect(10,10,600,800)
    translate(10,10)
    
    for strip in led_strips:
        strip.run(color(0, 192, 32))
        strip.draw()
        
    fill(255)
    circle(END_POINT.x, END_POINT.y, 80)
