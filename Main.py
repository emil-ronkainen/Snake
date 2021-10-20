import sys, pygame
from Dir import Dir
from pygame import Rect
from Snake import Snake
from FoodSpawner import FoodSpawner
from TPSpawner import TPSpawner
from EnemySpawner import EnemySpawner
from Config import Config as C

class Main:
  # docstring

    def __init__(self):
        pygame.init()
        self.snake = Snake(C.WIDTH / (C.SQUARE_SIZE * 2), C.HEIGHT / (C.SQUARE_SIZE * 2))
        self.food_spawner = FoodSpawner()
        self.tp_spawner = TPSpawner()
        self.enemy_spawner = EnemySpawner()
        self.screen = pygame.display.set_mode(C.SIZE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.speedup = 0

    def main(self):

        while self.running:
            self.clock.tick(C.TICKRATE + self.speedup)

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.handleKeys(event.key)
            self.running = self.update()
            self.draw()

        text = pygame.font.Font.render(pygame.font.SysFont("arial", 64), "YOU LOSE", True, (255, 255, 255))
        self.screen.blit(text, (C.WIDTH / 2.85, C.HEIGHT / 3))
        pygame.display.flip()

        while not self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.running = True

        self.__init__()
        self.main()
    def update(self):
        crashed = self.snake.update(self.snake)
        was_killed = self.enemy_spawner.update(self.snake)
        if crashed or was_killed:
            return False

        did_eat = self.food_spawner.update(self.snake)

        if len(self.snake.body) % 3 == 0 and did_eat:
            self.speedup += 1

        did_teleport = self.tp_spawner.update(self.snake)

        if did_teleport:
            self.enemy_spawner.destroy()

        return True

    def draw(self):
        self.screen.fill(C.LIGHT_GRAY)

        self.snake.draw(self.screen)
        self.food_spawner.draw(self.screen)
        self.tp_spawner.draw(self.screen)
        self.enemy_spawner.draw(self.screen)

        content = f"{(len(self.snake.body) - 3) * 10 + self.enemy_spawner.destroyed_enemy_count}"
        text = pygame.font.Font.render(pygame.font.SysFont("arial", 64), content, True, (255, 255, 255))
        self.screen.blit(text, (C.WIDTH / 2, C.HEIGHT / 100))

        pygame.display.flip()

    def handleKeys(self, key):
        if key == pygame.K_UP and self.snake.dir != Dir.DOWN:
            self.snake.dir = Dir.UP
        elif key == pygame.K_DOWN and self.snake.dir != Dir.UP:
            self.snake.dir = Dir.DOWN
        elif key == pygame.K_LEFT and self.snake.dir != Dir.RIGHT:
          self.snake.dir = Dir.LEFT
        elif key == pygame.K_RIGHT and self.snake.dir != Dir.LEFT:
          self.snake.dir = Dir.RIGHT
        elif key == pygame.K_ESCAPE:
          sys.exit()

if __name__ == '__main__':
    Main().main()
