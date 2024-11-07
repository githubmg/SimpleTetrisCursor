import random
from constants import *
from shapes import SHAPES
import pygame

class Tetromino:
    def __init__(self):
        self.x = GRID_WIDTH // 2
        self.y = 0
        self.shape = random.choice(SHAPES)
        self.color = random.choice(SHAPE_COLORS)
        self.rotation = 0

    def get_positions(self):
        positions = []
        shape_format = self.shape[self.rotation % len(self.shape)]

        for i, line in enumerate(shape_format):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    positions.append((self.x + j - 2, self.y + i - 4))
        return positions

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_down(self):
        self.y += 1

    def move_up(self):
        self.y -= 1

    def rotate(self):
        self.rotation += 1

    def rotate_back(self):
        self.rotation -= 1

    def draw(self, surface, grid):
        positions = self.get_positions()
        for pos in positions:
            if pos[1] > -1:
                pygame.draw.rect(surface, self.color,
                               (pos[0] * BLOCK_SIZE, 
                                pos[1] * BLOCK_SIZE,
                                BLOCK_SIZE, BLOCK_SIZE), 0) 