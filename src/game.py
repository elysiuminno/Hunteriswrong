```python
import pygame
from character import Character
from path import Path
from obstacle import Obstacle
from gem import Gem
from collision import detectCollision
from score import updateScore
from difficulty import updateDifficulty
from powerup import activatePowerup
from persistence import saveHighScore
from input import handleInput
from cross_platform import ensureCompatibility

class Game:
    def __init__(self):
        self.character = Character()
        self.path = Path()
        self.obstacles = []
        self.gems = []
        self.score = 0
        self.difficulty = 1
        self.powerups = []
        self.highScore = 0

    def gameLoop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    handleInput(event, self.character)

            self.path.updatePath(self.difficulty)
            self.character.updateCharacter()

            for obstacle in self.obstacles:
                obstacle.placeObstacle(self.path, self.difficulty)
                if detectCollision(self.character, obstacle):
                    self.character.health -= 1
                    if self.character.health <= 0:
                        running = False

            for gem in self.gems:
                gem.placeGem(self.path, self.difficulty)
                if detectCollision(self.character, gem):
                    self.score = updateScore(self.score, gem.value)

            for powerup in self.powerups:
                powerup.activatePowerup(self.character, self.path, self.score)

            self.difficulty = updateDifficulty(self.score)
            self.highScore = saveHighScore(self.score, self.highScore)

            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    ensureCompatibility()
    game = Game()
    game.gameLoop()
```