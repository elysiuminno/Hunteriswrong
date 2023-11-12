```python
import random
from src.path import Path
from src.character import Character

class Gem:
    def __init__(self, path: Path, character: Character):
        self.path = path
        self.character = character
        self.position = self.place_gem()

    def place_gem(self):
        # Place the gem at a random position on the path within reachable height
        gem_position = [random.randint(0, self.path.length), random.randint(0, self.character.jump_height)]
        return gem_position

    def collect_gem(self):
        # Check if the character's position matches the gem's position
        if self.character.position == self.position:
            self.character.score += 1
            self.position = self.place_gem()
```
