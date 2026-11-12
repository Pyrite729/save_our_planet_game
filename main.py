import pygame
from Buttons import Button
import time
import Tree

pygame.init()
screen_w = (1062)
screen_h = (649)
screen = pygame.display.set_mode((screen_w, screen_h))

running = True
FPS = 30
menu = 1
coins = 10
clock = pygame.time.Clock()
oxygen_level = 0.05
inventory_trees = 10
font = pygame.font.Font(None, 32)
last_milestone = int(oxygen_level * 100) // 5


mouse_pos = pygame.mouse.get_pos()

bg_image = pygame.image.load("Images/sop.png").convert_alpha()
play_button = pygame.image.load("Images/play_button.png").convert_alpha()
play_button_light = pygame.image.load("Images/play_button_light.png").convert_alpha()
loading_screen = pygame.image.load("Images/loading.png").convert_alpha()
loading_screen_2 = pygame.image.load("Images/loading2.png").convert_alpha()
loading_screen_3 = pygame.image.load("Images/loading3.png").convert_alpha()
image = pygame.image.load("Images/image.jpg").convert_alpha()
planet_bg_image = pygame.image.load("Images/planet_bg.png").convert_alpha()
desert = pygame.image.load("Images/desert icon.png").convert_alpha()
forest = pygame.image.load("Images/forest icon.png").convert_alpha()
river = pygame.image.load("Images/river icon.png").convert_alpha()
cross = pygame.image.load("Images/cross.png").convert_alpha()
hb_false = pygame.image.load("Images/hitbox false.png").convert_alpha()
hb_true = pygame.image.load("Images/hitbox true.png").convert_alpha()
bg_grassy = pygame.image.load("Images/grassy.png").convert_alpha()
oxygen_images = [
    pygame.image.load(f"Images/oxygen{x}.png").convert_alpha()
    for x in range(5, 101, 5)
]
## ngl that felt cool cause i cba to write allat

hb_showing = hb_false


growth_images = [
    pygame.image.load("Images/tree1.png").convert_alpha(),
    pygame.image.load("Images/tree2.png").convert_alpha(),
    pygame.image.load("Images/tree3.png").convert_alpha()
]

trees = []

play_button = Button(531, 400, play_button, 1)
play_button_light = Button(531, 400, play_button_light,1)
desert_button = Button(100, 100, desert, 1)
forest_button = Button(100, 200, forest, 1)
river_button = Button(100, 300, river, 1)
cross_button = Button(980, 100, cross, 1)
hb_button = Button(70, 600, hb_showing, 1)

while running == True:

    spf = clock.tick(FPS) / 1000    

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
                if forest_button.rect.collidepoint(event.pos) == True:
                    print("forest button pressed")
                    menu = 5

            if menu == 1:
                if hb_button.rect.collidepoint(event.pos) == True:
                    print("Hb pressed")
                    if hb_showing == hb_false:
                        hb_showing = hb_true
                        print("hb is true")
                    elif hb_showing == hb_true:
                        hb_showing = hb_false
                        print("hb is false")
                    hb_button.image = hb_showing
                    hb_button.rect = hb_button.image.get_rect(center=(70, 600))


            if menu == 5:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if event.button == 1:
                            
                            if inventory_trees > 0:
                                if cross_button.rect.collidepoint(event.pos) == False:
                                    if not any(tree.hitbox.collidepoint(mouse_pos) for tree in trees):
                                        trees.append(Tree.Tree(mouse_pos[0], mouse_pos[1], growth_images))
                                        inventory_trees = inventory_trees - 1
                            
                    elif event.button == 3: 
                        for tree in trees:
                            if tree.hitbox.collidepoint(mouse_pos):
                                trees.remove(tree)
                                inventory_trees = inventory_trees +1
                                break
                if cross_button.rect.collidepoint(event.pos) == True:
                    print("cross pressed")
                    menu = 1



    if menu == 1:
        screen.blit(bg_image)
        screen.blit(play_button.image, play_button.rect)
        screen.blit(hb_button.image, hb_button.rect)

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
        time.sleep(0.1)
        menu = 4

    elif menu == 4:
        screen.blit(planet_bg_image)
        screen.blit(desert_button.image, desert_button.rect)
        screen.blit(forest_button.image, forest_button.rect)
        screen.blit(river_button.image, river_button.rect)
        screen.blit(cross_button.image, cross_button.rect)
        pygame.display.flip()
    
    elif menu == 5:
        oxygen_level += sum(tree.oxygen_rate() for tree in trees) * spf

        screen.blit(bg_grassy) 
        screen.blit(cross_button.image, cross_button.rect)

        if hb_showing == hb_false:
            for tree in trees:
                tree.draw(screen, hitboxes = False)

        elif hb_showing == hb_true:
            for tree in trees:
                tree.draw(screen, hitboxes = True)

        bar_index = int(oxygen_level * 20) - 1

        if bar_index < 0:
            bar_index = 0

        last_index = len(oxygen_images) - 1
        if bar_index > last_index:
            bar_index = last_index

        screen.blit(oxygen_images[bar_index], (955, 150))
        inventory_text = font.render(f"Trees: {inventory_trees}", True, (0, 0, 0))
        screen.blit(inventory_text, (20, 60))
        oxygen_level_rounded = round(oxygen_level, 2)
        oxygen_level_text = font.render(f"Oxygen level: {oxygen_level_rounded*100}%", True, (0,0,0))
        screen.blit (oxygen_level_text, (20, 120))

        milestone = int(oxygen_level * 100) // 5

        if milestone > last_milestone:
            inventory_trees += milestone - last_milestone
            last_milestone = milestone


    pygame.display.update()
pygame.quit()
