from circular_entity import CircularEntity
from math import sqrt
import pygame


class Player(CircularEntity):
    def __init__(self, screen, difficulty):
        _size = 40
        _color = (255,0,0)
        _x = screen.get_width() // 2
        _y = screen.get_height()// 2
        CircularEntity.__init__(self, _size, _color, _x, _y)
        self.score = 0
        self.speed = 100
        self.max_speed = 500
        self.max_size = 200
        self.difficulty = difficulty

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.size)
        
        
    def increase_score(self):
        self.score += 1

    def increase_speed(self):
        if self.speed < self.max_speed:
            self.speed += 5

    def increase_size(self):
        if self.size < self.max_size:
            self.size += 2
            
    
            
            
    def collide(self, other_entity):
        #Distance between the player's center and the other entity's center
        dx = other_entity.pos_x - self.pos_x
        dy = other_entity.pos_y - self.pos_y
        distance = sqrt(dx ** 2 + dy ** 2)

        #Calculate the sum of the radii of the two entities 
        total_radius = self.size + other_entity.size + self.size // 3

        # If the distance is less than half the sum of the rays, the entities touch each other
        if distance < total_radius / 2:
            return True
        else:
            return False  
       
            
            
    def eat_food(self, foods):
        for food in foods:
            if self.collide(food):  #Check food-player collision
                self.increase_size()  
                self.increase_speed()
                foods.remove(food)  
                return True
        return False
    
    

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
            
    def move_mouse(self, mouse_pos, dt):
        #Distance between player current position & mouse
        dx = mouse_pos[0] - self.pos_x
        dy = mouse_pos[1] - self.pos_y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        # If distance !=null, moove player to mouse
        if distance > 0:
            speed = self.speed * dt
            dx_normalized = dx / distance
            dy_normalized = dy / distance
            move_x = speed * dx_normalized
            move_y = speed * dy_normalized

            #Update player position
            self.pos_x += move_x
            self.pos_y += move_y
