#PENSER A METTRE LES COMMENTAIRES EN ANGLAIS
from player import Player
from food import Food
from trap import Trap
import pygame


class Game() :
    def __init__(self, isKeyboard = True):
        self.isKeyboard = isKeyboard
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(60) / 5000
        self.running = True 
        self.screen = pygame.display.set_mode((1280, 720))
        self.screen_width, self.screen_height = self.screen.get_width(), self.screen.get_height()  

        self.player = Player(self.screen)
        self.foods = [
            Food(self.screen),
            Food(self.screen)
        ]
        
        self.traps = [Trap(self.screen), Trap(self.screen)]
        
    def handle_player_boundary(self):
    # Si le joueur dépasse la bordure gauche ou droite de l'écran
        if self.player.pos_x < 0:
            self.player.pos_x = self.screen_width  # Téléporter à droite
        elif self.player.pos_x > self.screen_width:
            self.player.pos_x = 0  # Téléporter à gauche

    # Si le joueur dépasse la bordure supérieure ou inférieure de l'écran
        if self.player.pos_y < 0:
            self.player.pos_y = self.screen_height  # Téléporter en bas
        elif self.player.pos_y > self.screen_height:
            self.player.pos_y = 0  # Téléporter en haut

        
    def play(self):
        if self.isKeyboard :
            self.play_with_keyboard()
        else :
            self.play_with_mouse()
            
               
    def play_with_keyboard(self):
        pygame.init()
        
        self.player = Player(self.screen)

        while self.running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return  # Retour au menu

            self.screen.fill("white")
            self.player.draw(self.screen)
            self.player.move_keyboard(self)
            self.handle_player_boundary()

            # Générer de la nourriture
            
            if len(self.foods) < 10:
                self.foods.append(Food(self.screen))

            # Dessiner chaque instance de nourriture
            for self.food in self.foods:
                self.food.draw(self.screen)
                
            # Générer des pièges
            
            if len(self.traps) < 2:
                self.traps.append(Trap(self.screen))

            # Dessiner chaque instance de nourriture
            for self.trap in self.traps:
                self.trap.draw(self.screen)

            # Mettre à jour l'écran
            pygame.display.flip()


            

        pygame.quit()


    def play_with_mouse(self):
        pygame.init()
        
        self.player = Player(self.screen)

        while self.running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return  # Retour au menu

            self.screen.fill("white")
            self.player.draw(self.screen)
            self.player.move_mouse(pygame.mouse.get_pos(), self.dt)
            self.handle_player_boundary()


            # Générer de la nourriture
       
            if len(self.foods) < 10:
                self.foods.append(Food(self.screen))

            # Dessiner chaque instance de nourriture
            for self.food in self.foods:
                self.food.draw(self.screen)
                
            # Générer des pièges
            if len(self.traps) < 2:
                self.traps.append(Trap(self.screen))

            # Dessiner chaque instance de nourriture
            for self.trap in self.traps:
                self.trap.draw(self.screen)
                
                
                

            # Mettre à jour l'écran
            pygame.display.flip()

        pygame.quit()
