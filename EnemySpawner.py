import random, pygame
from Config import Config as C
from pygame import Rect
from GameObject import GameObject

class EnemySpawner(GameObject):
  # This is EnemySpawner()

    def __init__(self):
        self.enemies = []

    def generate(self, snake_body):
        if random.randrange(0, 100) > 90 and len(snake_body) % 5 == 0:
            x = random.randrange(0, C.WIDTH / C.SQUARE_SIZE)
            y = random.randrange(0, C.HEIGHT / C.SQUARE_SIZE)

            # Check for initial collisions because they can be weird
            while (x, y) in snake_body:
                x = random.randrange(0, C.WIDTH / C.SQUARE_SIZE)
                y = random.randrange(0, C.HEIGHT / C.SQUARE_SIZE)
            self.enemies.append((x, y))

    def check_collision(self, snake):
        head = snake.head
        snake_rect = Rect(head[0]*C.SQUARE_SIZE, head[1]*C.SQUARE_SIZE, C.SQUARE_SIZE, C.SQUARE_SIZE)

        # Gen and check collision rects for all pieces of food
        for enemy in self.enemies:
            enemy_rect = Rect(enemy[0]*C.SQUARE_SIZE, enemy[1]*C.SQUARE_SIZE, C.SQUARE_SIZE, C.SQUARE_SIZE)

            if Rect.colliderect(snake_rect, enemy_rect):
                self.enemies.remove(enemy)
                return True

        return False

    def update(self, snake):
        self.generate(snake.body)
        if self.check_collision(snake):
            return True
        return False

    def draw(self, screen):
        for e in self.enemies:
            rect = Rect(e[0]*C.SQUARE_SIZE, e[1]*C.SQUARE_SIZE, C.SQUARE_SIZE, C.SQUARE_SIZE)
            pygame.draw.rect(screen, C.RED, rect)

    def destroy(self):
        self.enemies = []
