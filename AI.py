from Snake import Snake
from Dir import LEFT, UP, RIGHT, DOWN

class AI:
  # docstring

    def __init__(self, snake: Snake):
        self.snake = snake
        self.dir: Dir = DOWN

    def update(self):
        evalCont = 0
        evalLeft = 0
        evalRight = 0
        head = self.snake.head

        if (head[0] + self.dir[0], head[1] + self.dir[1]) in self.snake.body:
            eval -= 100
