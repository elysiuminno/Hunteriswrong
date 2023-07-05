import pygame
from pygame.locals import *

class CharacterSchema:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.jump = False
        self.slide = False

class Character:
    def __init__(self, character_schema, character_image):
        self.character_schema = character_schema
        self.character_image = pygame.image.load(character_image)

    def moveCharacter(self):
        keys = pygame.key.get_pressed()

        if keys[K_UP] and not self.character_schema.jump:
            self.character_schema.jump = True
        if keys[K_DOWN] and not self.character_schema.slide:
            self.character_schema.slide = True

        if self.character_schema.jump:
            self.character_schema.y -= self.character_schema.speed * 4
            self.character_schema.speed -= 1
            if self.character_schema.speed < -10:
                self.character_schema.jump = False
                self.character_schema.speed = 10

        if self.character_schema.slide:
            self.character_schema.y += self.character_schema.speed * 2
            self.character_schema.speed -= 1
            if self.character_schema.speed < -10:
                self.character_schema.slide = False
                self.character_schema.speed = 10

    def drawCharacter(self, window):
        window.blit(self.character_image, (self.character_schema.x, self.character_schema.y))