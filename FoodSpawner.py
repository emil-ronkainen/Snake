import random, pygame
from Config import Config as C
from GameObject import GameObject
from pygame import Rect

class FoodSpawner(GameObject):
  # docstring

    def __init__(self):
        self.food = []

    def generate(self, snake_body):
        if random.randrange(0, 100) > 95 and len(self.food) < 3:
            x = random.randrange(0, C.WIDTH / C.SQUARE_SIZE)
            y = random.randrange(0, C.HEIGHT / C.SQUARE_SIZE)
            # Check for initial collisions because they can be weird
            while (x, y) in snake_body:
                x = random.randrange(0, C.WIDTH / C.SQUARE_SIZE)
                y = random.randrange(0, C.HEIGHT / C.SQUARE_SIZE)
            self.food.append((x, y))

    def check_collision(self, snake):
        head = snake.head
        snake_rect = Rect(head[0]*C.SQUARE_SIZE, head[1]*C.SQUARE_SIZE, C.SQUARE_SIZE, C.SQUARE_SIZE)

        # Gen and check collision rects for all pieces of food
        for food in self.food:
            food_rect = Rect(food[0]*C.SQUARE_SIZE, food[1]*C.SQUARE_SIZE, C.SQUARE_SIZE, C.SQUARE_SIZE)

            if Rect.colliderect(snake_rect, food_rect):
                self.food.remove(food)
                return True

        return False

    def update(self, snake):
        self.generate(snake.body)
        if self.check_collision(snake):
            snake.eat()
            return True
        return False

    def draw(self, screen):
        for f in self.food:
            rect = Rect(f[0]*C.SQUARE_SIZE, f[1]*C.SQUARE_SIZE, C.SQUARE_SIZE, C.SQUARE_SIZE)
            pygame.draw.rect(screen, C.DATAROSA, rect)
