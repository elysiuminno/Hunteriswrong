```python
class Score:
    def __init__(self):
        self.score = 0

    def updateScore(self, increment):
        self.score += increment

    def decreaseScore(self, decrement):
        self.score -= decrement
        if self.score < 0:
            self.score = 0

    def getScore(self):
        return self.score

    def resetScore(self):
        self.score = 0
```