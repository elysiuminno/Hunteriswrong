```python
import os
import json

class Persistence:
    def __init__(self, filename='high_score.json'):
        self.filename = filename

    def save_high_score(self, score):
        data = {'high_score': score}
        with open(self.filename, 'w') as f:
            json.dump(data, f)

    def load_high_score(self):
        if not os.path.exists(self.filename):
            return 0

        with open(self.filename, 'r') as f:
            data = json.load(f)
            return data.get('high_score', 0)
```