```python
class PowerUp:
    def __init__(self, type, duration):
        self.type = type
        self.duration = duration
        self.active = False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

def activatePowerup(powerup):
    powerup.activate()

def deactivatePowerup(powerup):
    powerup.deactivate()
```