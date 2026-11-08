import pygame
from Buttons import Button
import time

pygame.init()
screen_w = (1062)
screen_h = (649)
screen = pygame.display.set_mode((screen_w, screen_h))

running = True
FPS = 30
menu = 1
coins = 10

mouse_pos = pygame.mouse.get_pos()

bg_image = pygame.image.load("sop.png").convert_alpha()
play_button = pygame.image.load("play_button.png").convert_alpha()
play_button_light = pygame.image.load("play_button_light.png").convert_alpha()
loading_screen = pygame.image.load("loading.png").convert_alpha()
loading_screen_2 = pygame.image.load("loading2.png").convert_alpha()
loading_screen_3 = pygame.image.load("loading3.png").convert_alpha()
image = pygame.image.load("image.jpg").convert_alpha()
planet_bg_image = pygame.image.load("planet_bg.png").convert_alpha()
desert = pygame.image.load("desert icon.png").convert_alpha()
forest = pygame.image.load("forest icon.png").convert_alpha()
river = pygame.image.load("river icon.png").convert_alpha()
cross = pygame.image.load("cross.png").convert_alpha()

play_button = Button(531, 400, play_button, 1)
play_button_light = Button(531, 400, play_button_light,1)
desert_button = Button(100, 100, desert, 1)
forest_button = Button(100, 200, forest, 1)
river_button = Button(100, 300, river, 1)
cross_button = Button(980, 100, cross, 1)

while running == True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu == 1:
                if play_button.rect.collidepoint(event.pos) == True:
                    print("playing")
                    menu = 2
            if menu == 4:
                if cross_button.rect.collidepoint(event.pos) == True:
                    print("cross pressed")
                    menu = 1


    if menu == 1:
        screen.blit(bg_image)
        screen.blit(play_button.image, play_button.rect)

        mouse_pos = pygame.mouse.get_pos()

        if play_button.rect.collidepoint(mouse_pos):
            screen.blit(play_button_light.image, play_button_light.rect)
        else:
            screen.blit(play_button.image, play_button.rect)

    elif menu == 2:
        screen.blit(loading_screen)
        pygame.display.flip()
        time.sleep(0.3)
        screen.blit(loading_screen_2)
        pygame.display.flip()
        time.sleep(0.3)
        screen.blit(loading_screen_3)
        pygame.display.flip()
        time.sleep(0.3)
        menu = 3

    elif menu == 3:
        screen.blit(image)
        pygame.display.flip()
        time.sleep(1)
        menu = 4

    elif menu == 4:
        screen.blit(planet_bg_image)
        screen.blit(desert_button.image, desert_button.rect)
        screen.blit(forest_button.image, forest_button.rect)
        screen.blit(river_button.image, river_button.rect)
        screen.blit(cross_button.image, cross_button.rect)
        pygame.display.flip()

    pygame.display.update()
pygame.quit()
