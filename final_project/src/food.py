class Food:
    def __init__(self, x, y):
        self.position = (x, y)

    def relocate(self, x, y):
        self.position = (x, y)