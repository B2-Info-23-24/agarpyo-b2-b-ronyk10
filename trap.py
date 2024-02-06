from circular_entity import CircularEntity
import random

class Trap(CircularEntity):
    def __init__(self, screen):
        _size = 60
        _color = (0,0,255)
        _x = random.randint(0, screen.get_width())
        _y = random.randint(0, screen.get_height())
        CircularEntity.__init__(self, _size, _color, _x, _y)