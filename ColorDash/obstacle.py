```python
import pygame
from random import randint

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > 800:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > 600:
            self.speed[1] = -self.speed[1]

    def draw(self, surface):
        surface.blit(self.image, self.rect)

def generate_obstacle():
    obstacle_image_file = "assets/obstacle.png"
    obstacle_location = [randint(0, 800), randint(0, 600)]
    obstacle_speed = [randint(-10, 10), randint(-10, 10)]
    obstacle = Obstacle(obstacle_image_file, obstacle_location, obstacle_speed)
    return obstacle
```