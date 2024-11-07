import pygame
from constants import *

class Grid:
    def __init__(self):
        self.grid = self.create_empty_grid()
        self.locked_positions = {}

    def create_empty_grid(self):
        return [[(0, 0, 0) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    def is_valid_position(self, piece):
        accepted_positions = [[(x, y) for x in range(GRID_WIDTH) 
                             if self.grid[y][x] == (0, 0, 0)] 
                             for y in range(GRID_HEIGHT)]
        accepted_positions = [pos for row in accepted_positions for pos in row]

        for pos in piece.get_positions():
            if pos not in accepted_positions and pos[1] > -1:
                return False
        return True

    def lock_position(self, position, color):
        self.locked_positions[position] = color
        self.update_grid()

    def update_grid(self):
        self.grid = self.create_empty_grid()
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if (x, y) in self.locked_positions:
                    self.grid[y][x] = self.locked_positions[(x, y)]

    def clear_full_rows(self):
        inc = 0
        for i in range(len(self.grid)-1, -1, -1):
            row = self.grid[i]
            if (0, 0, 0) not in row:
                inc += 1
                ind = i
                for j in range(len(row)):
                    try:
                        del self.locked_positions[(j, i)]
                    except:
                        continue

        if inc > 0:
            for key in sorted(list(self.locked_positions), key=lambda x: x[1])[::-1]:
                x, y = key
                if y < ind:
                    newKey = (x, y + inc)
                    self.locked_positions[newKey] = self.locked_positions.pop(key)
        
        self.update_grid()

    def draw(self, surface):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                pygame.draw.rect(surface, self.grid[y][x], 
                               (x * BLOCK_SIZE, y * BLOCK_SIZE, 
                                BLOCK_SIZE, BLOCK_SIZE), 0)

        # Draw grid lines
        for i in range(GRID_HEIGHT):
            pygame.draw.line(surface, (128, 128, 128), 
                           (0, i * BLOCK_SIZE), 
                           (SCREEN_WIDTH, i * BLOCK_SIZE))
        for j in range(GRID_WIDTH):
            pygame.draw.line(surface, (128, 128, 128), 
                           (j * BLOCK_SIZE, 0), 
                           (j * BLOCK_SIZE, SCREEN_HEIGHT)) 