```python
import pygame
from character import Character
from path import Path
from obstacle import Obstacle
from gem import Gem
from powerup import Powerup
from score import Score
from settings import Settings

class ColorDash:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Color Dash")
        self.character = Character(self)
        self.path = Path(self)
        self.obstacles = pygame.sprite.Group()
        self.gems = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.score = Score(self)

    def run_game(self):
        while True:
            self._check_events()
            self.character.update()
            self._update_path()
            self._update_obstacles()
            self._update_gems()
            self._update_powerups()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.character.jump()
                elif event.key == pygame.K_DOWN:
                    self.character.slide()

    def _update_path(self):
        self.path.scroll()
        if not self.path.rect.right:
            self.path = Path(self)

    def _update_obstacles(self):
        self.obstacles.update()
        for obstacle in self.obstacles.copy():
            if obstacle.rect.left <= 0:
                self.obstacles.remove(obstacle)
        self._check_obstacle_collision()

    def _update_gems(self):
        self.gems.update()
        for gem in self.gems.copy():
            if gem.rect.left <= 0:
                self.gems.remove(gem)
        self._check_gem_collision()

    def _update_powerups(self):
        self.powerups.update()
        for powerup in self.powerups.copy():
            if powerup.rect.left <= 0:
                self.powerups.remove(powerup)
        self._check_powerup_collision()

    def _check_obstacle_collision(self):
        if pygame.sprite.spritecollideany(self.character, self.obstacles):
            self._end_game()

    def _check_gem_collision(self):
        gems_collided = pygame.sprite.spritecollide(self.character, self.gems, True)
        if gems_collided:
            self.score.update(len(gems_collided))

    def _check_powerup_collision(self):
        powerup_collided = pygame.sprite.spritecollide(self.character, self.powerups, True)
        if powerup_collided:
            powerup_collided[0].activate()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.path.blitme()
        self.character.blitme()
        for obstacle in self.obstacles.sprites():
            obstacle.blitme()
        for gem in self.gems.sprites():
            gem.blitme()
        for powerup in self.powerups.sprites():
            powerup.blitme()
        self.score.show_score()
        pygame.display.flip()

    def _end_game(self):
        pygame.quit()
        exit()

if __name__ == '__main__':
    cd = ColorDash()
    cd.run_game()
```