class Food:
    def __init__(self, x, y):
        """
        Initializes the Food object.
        Args:
            x (int): x-coordinate of the food.
            y (int): y-coordinate of the food.
        """
        self.position = (x, y)

    def relocate(self, x, y):
        """
        Changes the food's position.
        Args:
            x (int): New x-coordinate.
            y (int): New y-coordinate.
        """
        self.position = (x, y)