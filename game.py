from player import Player
from food import Food
from trap import Trap
import pygame
import time


class Game():
    def __init__(self, isKeyboard, difficulty):
        self.isKeyboard = isKeyboard
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(60) / 5000
        self.running = True
        self.screen = pygame.display.set_mode((1280, 720)) #Screen size
        self.screen_width, self.screen_height = self.screen.get_width(), self.screen.get_height()
        self.font = pygame.font.Font(None, 36)
        self.difficulty = difficulty

        self.player = Player(self.screen, self.difficulty)
        self.foods = [
            Food(self.screen),
            Food(self.screen)
        ]

        self.traps = [Trap(self.screen), Trap(self.screen)]

    def handle_player_boundary(self):
        #We're checking right & left borders
        if self.player.pos_x < 0:
            self.player.pos_x = self.screen_width - 1  # Teleported to the right
        elif self.player.pos_x > self.screen_width - 1:
            self.player.pos_x = 0  # Teleported to the left 

        # We're checking top & bottom borders
        if self.player.pos_y < 0:
            self.player.pos_y = self.screen_height - 1  # Teleported to the bottom
        elif self.player.pos_y > self.screen_height - 1:
            self.player.pos_y = 0  # Teleported to the top

    def play(self, start_time):
        #Game start in coordination with the choice of the player
        if self.isKeyboard:
            self.play_with_keyboard(start_time)
        else:
            self.play_with_mouse(start_time)

    def check_food_collision(self):
        if self.player.eat_food(self.foods):  #We're checking food-player collisions 
            self.foods.append(Food(self.screen))
            self.player.score += 1  #Updating score
            


    def handle_collisions(self, traps):
        traps_to_keep = []  # List to get traps to keep 
        for trap in traps:
            if not self.player.collide(trap) or self.player.size <= trap.size:
                traps_to_keep.append(trap)  
            elif self.player.size > trap.size:
            #Divide player size & speed 
             self.player.size /= self.difficulty
             self.player.speed /= self.difficulty
        
        traps.clear()  #Clear the list
        traps.extend(traps_to_keep)  # Add traps to keep to original list

    def play_with_keyboard(self, start_time):
        pygame.init()

        while self.running:
            
            current_time = time.time()
            elapsed_time = current_time - start_time
            remaining_time = 60 - elapsed_time  
            
            if remaining_time <= 0:  #If times'up
                self.game_over_screen(self.player.score)
                return

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return  #Back to the menu

       
    

            self.screen.fill("white")
            self.player.move_keyboard(self)
            self.handle_player_boundary()
            self.check_food_collision()
            self.handle_collisions(self.traps)
            
            #Top left screen informations
            score_text = self.font.render(f"Score: {self.player.score}", True, (0, 0, 0))
            self.screen.blit(score_text, (10, 10))
            speed_text = self.font.render(f"Speed: {self.player.speed}", True, (0, 0, 0))
            self.screen.blit(speed_text, (10, 30))
            difficulty_text = self.font.render(f"Difficulty: {self.player.difficulty}", True, (0, 0, 0))
            self.screen.blit(difficulty_text, (10, 50))
            size_text = self.font.render(f"Size: {self.player.size}", True, (0, 0, 0))
            self.screen.blit(size_text, (10, 70))
            time_text = self.font.render(f"Time remaining: {round(remaining_time)} seconds", True, (0, 0, 0))
            self.screen.blit(time_text, (10, 90))
         

            #Food generation
            if self.difficulty == 2:
                if len(self.foods) < 5:
                    self.foods.append(Food(self.screen))
            elif self.difficulty == 3:
                if len(self.foods) < 3:
                    self.foods.append(Food(self.screen))
            elif self.difficulty == 4:
                if len(self.foods) < 2:
                    self.foods.append(Food(self.screen))
                
            

            #Drawing all foods
            for food in self.foods:
                food.draw(self.screen)

            #Traps generation 
            if len(self.traps) < self.difficulty:
                self.traps.append(Trap(self.screen))

            draw_player = False
            for trap in self.traps:
                if trap.size > self.player.size and draw_player != True:
                    self.player.draw(self.screen)
                    draw_player = True
                trap.draw(self.screen)
            
            if draw_player == False:
                self.player.draw(self.screen)

            # Mettre à jour l'écran
            pygame.display.flip()

        pygame.quit()
        
        
    #Same as play_with_keyboard, but with mouse option
    def play_with_mouse(self, start_time):
        pygame.init()

        while self.running:
            
            current_time = time.time()
            elapsed_time = current_time - start_time
            remaining_time = 60 - elapsed_time  

            if remaining_time <= 0:  
                self.game_over_screen(self.player.score)
                return
            
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 


            self.screen.fill("white")
            self.player.move_mouse(pygame.mouse.get_pos(), self.dt)
            self.handle_player_boundary()
            self.check_food_collision()
            self.handle_collisions(self.traps)
            score_text = self.font.render(f"Score: {self.player.score}", True, (0, 0, 0))
            self.screen.blit(score_text, (10, 10))
            speed_text = self.font.render(f"Speed: {self.player.speed}", True, (0, 0, 0))
            self.screen.blit(speed_text, (10, 30))
            size_text = self.font.render(f"Size: {self.player.size}", True, (0, 0, 0))
            self.screen.blit(size_text, (10, 50))
            difficulty_text = self.font.render(f"Difficulty: {self.player.difficulty}", True, (0, 0, 0))
            self.screen.blit(difficulty_text, (10, 70))
            time_text = self.font.render(f"Time remaining: {round(remaining_time)} seconds", True, (0, 0, 0))
            self.screen.blit(time_text, (10, 90))
            

            if self.difficulty == 2:
                if len(self.foods) < 5:
                    self.foods.append(Food(self.screen))
            elif self.difficulty == 3:
                if len(self.foods) < 3:
                    self.foods.append(Food(self.screen))
            elif self.difficulty == 4:
                if len(self.foods) < 2:
                    self.foods.append(Food(self.screen))
                
        
            for food in self.foods:
                food.draw(self.screen)

            if len(self.traps) < self.difficulty:
                self.traps.append(Trap(self.screen))

            draw_player = False
            for trap in self.traps:
                if trap.size > self.player.size and draw_player != True:
                    self.player.draw(self.screen)
                    draw_player = True
                trap.draw(self.screen)
            
            if draw_player == False:
                self.player.draw(self.screen)

            pygame.display.flip()

        pygame.quit()
        
    def game_over_screen(self, score):
        #Display of game over scren
        game_over = True
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        #Back to the menu
                        return

            self.screen.fill("white")
            
            #Final score display
            score_text = self.font.render(f"Score: {score}", True, (0, 0, 0))
            score_rect = score_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 50))
            self.screen.blit(score_text, score_rect)

            #Dispaly back button
            button_text = self.font.render("Press Enter to return to main menu", True, (0, 0, 0))
            button_rect = button_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 50))
            self.screen.blit(button_text, button_rect)

            pygame.display.flip()
