```python
import pygame
from character import Character

class InputHandler:
    def __init__(self, character):
        self.character = character

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.character.jump()
                elif event.key == pygame.K_DOWN:
                    self.character.slide()

        return True
```