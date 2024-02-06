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
        # Calculer la distance entre la position actuelle du joueur et la position de la souris
        dx = mouse_pos[0] - self.pos_x
        dy = mouse_pos[1] - self.pos_y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        # Si la distance n'est pas nulle, déplacer le joueur vers la position de la souris
        if distance > 0:
            # Calculer le déplacement en fonction de la vitesse et de la durée du tick
            speed = self.speed * dt
            dx_normalized = dx / distance
            dy_normalized = dy / distance
            move_x = speed * dx_normalized
            move_y = speed * dy_normalized

            # Mettre à jour la position du joueur
            self.pos_x += move_x
            self.pos_y += move_y
