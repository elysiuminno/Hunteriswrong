```python
import pygame
from ColorDash.game import Game
from ColorDash.settings import Settings

def main():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Color Dash")

    game = Game(screen, settings)

    while True:
        game.check_events()
        game.update_screen()
        game.update_score()
        game.check_game_over()

if __name__ == "__main__":
    main()
```