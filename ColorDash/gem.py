import pygame
from random import randint

class Gem(pygame.sprite.Sprite):
    def __init__(self, gem_image):
        super().__init__()
        self.image = pygame.image.load(gem_image)
        self.rect = self.image.get_rect()
        self.rect.x = randint(800, 1200)
        self.rect.y = randint(0, 600)

    def update(self):
        self.rect.x -= 5
        if self.rect.x < -self.rect.width:
            self.rect.x = randint(800, 1200)
            self.rect.y = randint(0, 600)

    def collectGem(self, player_character):
        if pygame.sprite.collide_rect(self, player_character):
            self.rect.x = randint(800, 1200)
            self.rect.y = randint(0, 600)
            return True
        return False