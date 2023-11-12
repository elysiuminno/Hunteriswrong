```python
from src.character import Character
from src.obstacle import Obstacle
from src.gem import Gem
from src.score import updateScore

def detectCollision(character, game_elements):
    for element in game_elements:
        if isinstance(element, Obstacle):
            if character.position == element.position:
                character.health -= 1
                if character.health <= 0:
                    return True
        elif isinstance(element, Gem):
            if character.position == element.position:
                updateScore(character.score)
    return False
```