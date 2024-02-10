import pygame
import sys
import time
from button import Button
from game import Game

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Roro.io")

BG = pygame.image.load("assets/Background.png")


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


def main_menu():
    difficulty = 2

    MENU_TEXT = get_font(55).render("Roro.io - Menu", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

    PLAY_MOUSE_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                                text_input="PLAY MOUSE", font=get_font(30), base_color="#d7fcd4",
                                hovering_color="White")
    PLAY_KEYBOARD_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                    text_input="PLAY KEYBOARD", font=get_font(30), base_color="#d7fcd4",
                                    hovering_color="White")
    QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                            text_input="QUIT", font=get_font(55), base_color="#d7fcd4", hovering_color="White")

    EASY_BUTTON = Button(image=None, pos=(100, 300), text_input="Easy", font=get_font(30), base_color="White",
                            hovering_color="White")
    MEDIUM_BUTTON = Button(image=None, pos=(100, 350), text_input="Medium", font=get_font(30),
                            base_color="#000000", hovering_color="White")
    HARD_BUTTON = Button(image=None, pos=(100, 400), text_input="Hard", font=get_font(30), base_color="#000000",
                         hovering_color="White")
    
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
    
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_MOUSE_BUTTON, PLAY_KEYBOARD_BUTTON, QUIT_BUTTON, EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_MOUSE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    start_time= time.time()
                    game = Game(False, difficulty)
                    game.play(start_time)
                if PLAY_KEYBOARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    start_time= time.time()
                    game = Game(True, difficulty)
                    game.play(start_time)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if EASY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    MEDIUM_BUTTON.base_color = "#000000"
                    HARD_BUTTON.base_color = "#000000"
                    EASY_BUTTON.base_color = "White"
                    difficulty = 2
                if MEDIUM_BUTTON.checkForInput(MENU_MOUSE_POS):
                    EASY_BUTTON.base_color = "#000000"
                    HARD_BUTTON.base_color = "#000000"
                    MEDIUM_BUTTON.base_color = "White"
                    difficulty = 3
                if HARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    MEDIUM_BUTTON.base_color = "#000000"
                    EASY_BUTTON.base_color = "#000000"
                    HARD_BUTTON.base_color = "White"
                    difficulty = 4

        pygame.display.update()


main_menu()
