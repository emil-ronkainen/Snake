import random, pygame
from pygame import Rect
from Config import Config as C
from GameObject import GameObject

class TPSpawner(GameObject):
  # docstring

    def __init__(self):
        self.positions = []

    def generate(self, snake_body):
        if random.randrange(0, 100) > 95 and len(self.positions) == 0:
            x1 = random.randrange(0, C.WIDTH / C.SQUARE_SIZE)
            y1 = random.randrange(0, C.HEIGHT / C.SQUARE_SIZE)
            pos1 = (x1, y1)

            x2 = random.randrange(0, C.WIDTH / C.SQUARE_SIZE)
            y2 = random.randrange(0, C.HEIGHT / C.SQUARE_SIZE)
            pos2 = (x2, y2)

            # Check that we do not generate inside of snake
            while pos1 in snake_body:
                x1 = random.randrange(0, C.WIDTH / C.SQUARE_SIZE)
                y1 = random.randrange(0, C.HEIGHT / C.SQUARE_SIZE)
                pos1 = (x1, y1)

            while pos2 in snake_body:
                x2 = random.randrange(0, C.WIDTH / C.SQUARE_SIZE)
                y2 = random.randrange(0, C.HEIGHT / C.SQUARE_SIZE)
                pos2 = (x2, y2)


            self.positions.append(pos1)
            self.positions.append(pos2)

    def check_collision(self, snake):
        if len(self.positions) == 0: # If there are no generated positions, break
            return (0, 0)
        head = snake.head

        # Create collision rects for snake and random positions
        snake_rect = Rect(head[0]*C.SQUARE_SIZE, head[1]*C.SQUARE_SIZE, C.SQUARE_SIZE, C.SQUARE_SIZE)
        rect_1 = Rect(self.positions[0][0]*C.SQUARE_SIZE, self.positions[0][1]*C.SQUARE_SIZE, C.SQUARE_SIZE, C.SQUARE_SIZE)
        rect_2 = Rect(self.positions[1][0]*C.SQUARE_SIZE, self.positions[1][1]*C.SQUARE_SIZE, C.SQUARE_SIZE, C.SQUARE_SIZE)

        # Check if we collide with any rect and if we do, jump to the other
        if Rect.colliderect(snake_rect, rect_1):
            res = self.positions[1]
            self.positions = []
            return res
        elif Rect.colliderect(snake_rect, rect_2):
            res = self.positions[0]
            self.positions = []
            return res

        return (0, 0)

    def update(self, snake):
        self.generate(snake.body)
        pos = self.check_collision(snake)

        if pos != (0, 0):
            snake.jump_to(pos)
            return True
        return False

    def draw(self, screen):
        for tp in self.positions:
            rect = Rect(tp[0]*C.SQUARE_SIZE, tp[1]*C.SQUARE_SIZE, C.SQUARE_SIZE, C.SQUARE_SIZE)
            pygame.draw.rect(screen, C.DARK_GRAY, rect)
