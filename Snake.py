import pygame
from pygame import Rect
from Dir import Dir
from Config import Config as C
from GameObject import GameObject

class Snake(GameObject):
    # Class Snake models a snake

    def __init__(self, x, y):
        self.num_squares = (C.WIDTH / C.SQUARE_SIZE, C.HEIGHT / C.SQUARE_SIZE)
        self.dir: Dir = Dir.UP
        self.head = (x, y)
        self.body = [
            self.head,
            (self.head[0], self.head[1] + 1),
            (self.head[0], self.head[1] + 2)
        ]

    def move(self):
        self.body.pop(len(self.body) - 1)
        self.head = ((self.head[0] + self.dir[0]), (self.head[1] + self.dir[1]))
        self.wrap()

        if self.head in self.body:
            return True

        self.body.insert(0, self.head)
        return False

    def jump_to(self, pos):
        self.head = pos
        self.wrap()

    def wrap(self):
        if self.head[0] >= C.WIDTH / C.SQUARE_SIZE:
            self.head = (0, self.head[1])
        elif self.head[0] < 0: # Don't check for =0 since we draw from top-left
            self.head = (C.WIDTH / C.SQUARE_SIZE, self.head[1])
        elif self.head[1] >= C.HEIGHT / C.SQUARE_SIZE:
            self.head = (self.head[0], 0)
        elif self.head[1] < 0:
            self.head = (self.head[0], C.HEIGHT / C.SQUARE_SIZE)

    def eat(self): # "Move" backwards without erasing a square
        new_pos = (self.body[-1][0] + self.dir[0], self.body[-1][1] + self.dir[1])
        self.body.append(new_pos)

    def update(self, snake):
        return self.move()

    def draw(self, screen):
        for sq in self.body:
            rect = Rect(sq[0]*C.SQUARE_SIZE, sq[1]*C.SQUARE_SIZE, C.SQUARE_SIZE, C.SQUARE_SIZE)
            pygame.draw.rect(screen, C.GREEN, rect)
