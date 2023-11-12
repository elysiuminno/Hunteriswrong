```python
class Path:
    def __init__(self, segments):
        self.segments = segments
        self.speed = 1

    def updatePath(self):
        for segment in self.segments:
            segment.position[0] -= self.speed
            if segment.position[0] < 0:
                segment.position[0] = len(self.segments) - 1

class Segment:
    def __init__(self, position, color):
        self.position = position
        self.color = color
```