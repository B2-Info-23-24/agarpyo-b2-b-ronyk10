import pygame

class CircularEntity:
     def __init__(self, size, color, x, y):
         self.size = size
         self.color = color
         self.pos_x = x
         self.pos_y = y

     def set_position(self, pos_x, pos_y):
                self.pos_x = pos_x
                self.pos_y = pos_y

     def set_size(self, size):
                self.size = size

     def set_color(self, color):
                self.color = color

     def get_position(self):
                return self.pos_x, self.pos_y

     def get_size(self):
                return self.size

     def get_color(self):
                return self.color
                 
     def draw(self, screen):
                pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.size)
                