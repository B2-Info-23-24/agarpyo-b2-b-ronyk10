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
        self.player = Player(self.screen)
        self.foods = [
            Food(self.screen),
            Food(self.screen)
        ]
        
        self.traps = [Trap(self.screen), Trap(self.screen)]
        
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

            # Générer de la nourriture
            # Par exemple, générer 10 instances de nourriture
            if len(self.foods) < 10:
                self.foods.append(Food(self.screen))

            # Dessiner chaque instance de nourriture
            for self.food in self.foods:
                self.food.draw(self.screen)

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

            # Générer de la nourriture
            # Par exemple, générer 10 instances de nourriture
            if len(self.foods) < 10:
                self.foods.append(Food(self.screen))

            # Dessiner chaque instance de nourriture
            for self.food in self.foods:
                self.food.draw(self.screen)

            # Mettre à jour l'écran
            pygame.display.flip()

        pygame.quit()
