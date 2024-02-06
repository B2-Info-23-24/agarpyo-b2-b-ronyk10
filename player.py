from circular_entity import CircularEntity
import pygame

class Player(CircularEntity):
    def __init__(self, screen):
        _size = 40
        _color = (255,0,0)
        _x = screen.get_width() // 2
        _y = screen.get_height()// 2
        CircularEntity.__init__(self, _size, _color, _x, _y)
        self.score = 0
        self.speed = 100
        self.max_speed = 500
        self.max_size = 200

    def increase_score(self):
        self.score += 1

    def increase_speed(self):
        if self.speed < self.max_speed:
            self.speed += 5

    def increase_size(self):
        if self.size < self.max_size:
            self.size += 2

    def move_keyboard(self, game):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            self.pos_y -= self.speed * game.dt
        if keys[pygame.K_s]:
             self.pos_y += self.speed * game.dt
        if keys[pygame.K_q]:
             self.pos_x -= self.speed * game.dt
        if keys[pygame.K_d]:
            self.pos_x += self.speed * game.dt

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.size)