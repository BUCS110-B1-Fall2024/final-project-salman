class Snake:
    def __init__(self, x, y, length=3, direction="RIGHT"):
        self.body = [(x, y - i) for i in range(length)]  # List of (x, y) positions for the snake body
        self.direction = direction

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == "UP":
            new_head = (head_x, head_y - 1)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + 1)
        elif self.direction == "LEFT":
            new_head = (head_x - 1, head_y)
        elif self.direction == "RIGHT":
            new_head = (head_x + 1, head_y)
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def set_direction(self, direction):
        self.direction = direction