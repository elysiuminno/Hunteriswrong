```python
from src.game import Game
from src.path import Path

class Difficulty:
    def __init__(self):
        self.base_speed = 1.0
        self.speed_increment = 0.1
        self.max_speed = 5.0

    def updateDifficulty(self, game: Game, path: Path):
        if game.score % 10 == 0 and path.speed < self.max_speed:
            path.speed += self.speed_increment
```