class Score:
    def __init__(self):
        self.score = 0

    def update_score(self, gem_value):
        self.score += gem_value

    def reset_score(self):
        self.score = 0

    def get_score(self):
        return self.score