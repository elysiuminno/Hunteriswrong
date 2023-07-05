```python
class Character:
    def __init__(self):
        self.position = [0, 0]
        self.health = 100
        self.score = 0
        self.state = "idle"

    def jump(self):
        if self.state != "jumping":
            self.state = "jumping"
            # Add code here to animate the jump

    def slide(self):
        if self.state != "sliding":
            self.state = "sliding"
            # Add code here to animate the slide

    def updateCharacter(self, input):
        if input == "jump":
            self.jump()
        elif input == "slide":
            self.slide()
        else:
            self.state = "idle"

    def get_position(self):
        return self.position

    def get_health(self):
        return self.health

    def get_score(self):
        return self.score

    def set_position(self, position):
        self.position = position

    def set_health(self, health):
        self.health = health

    def set_score(self, score):
        self.score = score
```