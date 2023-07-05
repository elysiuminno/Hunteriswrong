```python
import random
from src.path import Path
from src.character import Character

class Obstacle:
    def __init__(self, path: Path, character: Character):
        self.path = path
        self.character = character
        self.obstacles = []

    def placeObstacle(self):
        # Randomly decide the position of the obstacle on the path
        obstacle_position = random.randint(0, len(self.path.segments) - 1)

        # Ensure the obstacle is not placed too close to the character
        while abs(obstacle_position - self.character.position) < 5:
            obstacle_position = random.randint(0, len(self.path.segments) - 1)

        # Place the obstacle on the path
        self.path.segments[obstacle_position] = 'obstacle'
        self.obstacles.append(obstacle_position)

    def updateObstacles(self):
        # Move the obstacles along with the path
        for i in range(len(self.obstacles)):
            self.obstacles[i] -= 1

            # If the obstacle has moved off the screen, remove it
            if self.obstacles[i] < 0:
                self.path.segments[self.obstacles[i]] = 'empty'
                self.obstacles.pop(i)

        # Place a new obstacle
        self.placeObstacle()
```