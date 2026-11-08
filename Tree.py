import random
import time
import pygame


class Tree:
    def __init__(self, x, y, growth_images):
        self.growth_images = growth_images
        self.planted_at = time.monotonic()
        self.growth_stage = 0

        self.scale = random.randint(8, 12) / 10 
        self.genetics = random.randint(8, 12) / 10

        self.images = [
            pygame.transform.smoothscale(
                image,
                (int(128 * self.scale),
                 int(128 * self.scale))
            )
            for image in growth_images
        ]

        self.image_rect = self.images[0].get_rect(midbottom=(x, y))

        self.hitbox = pygame.Rect(0, 0, 20, 20)
        self.hitbox.center = (x, y-15)

    def update(self):
        elapsed = time.monotonic() - self.planted_at

        time_before_stage_1 = 30 * self.scale
        time_before_stage_2 = 90 * self.scale

        if elapsed >= time_before_stage_2:
            self.growth_stage = 2
        elif elapsed >= time_before_stage_1:
            self.growth_stage = 1

    def draw(self, screen, hitboxes = False):
        self.update()
        screen.blit(self.images[self.growth_stage], self.image_rect)
        if hitboxes == True:
            pygame.draw.rect(screen, (255, 255, 255), self.hitbox, 2)

    def oxygen_rate(self):
        age = time.monotonic() - self.planted_at
        age_factor = 0.01 + 0.025 * min(age / 90, 1)
        return 0.01 * (self.scale ** 2) * age_factor * self.genetics
            