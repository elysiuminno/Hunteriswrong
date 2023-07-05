```python
import pygame
from ColorDash.settings import POWERUP_IMAGE

class Powerup(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.image = pygame.image.load(POWERUP_IMAGE[type])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type

    def update(self):
        self.rect.x -= 5  # Move the powerup leftwards

    def activate(self, player_character):
        if self.type == 'slow_time':
            player_character.slow_time()
        elif self.type == 'invincibility':
            player_character.become_invincible()

class SlowTimePowerup(Powerup):
    def __init__(self, x, y):
        super().__init__(x, y, 'slow_time')

    def activate(self, player_character):
        player_character.slow_time()

class InvincibilityPowerup(Powerup):
    def __init__(self, x, y):
        super().__init__(x, y, 'invincibility')

    def activate(self, player_character):
        player_character.become_invincible()
```