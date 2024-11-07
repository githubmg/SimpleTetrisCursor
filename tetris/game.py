import pygame
from grid import Grid
from tetromino import Tetromino
from constants import *

class TetrisGame:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Tetris')
        
        self.grid = Grid()
        self.current_piece = Tetromino()
        self.clock = pygame.time.Clock()
        self.fall_time = 0
        self.fall_speed = 0.27

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.current_piece.move_left()
                    if not self.grid.is_valid_position(self.current_piece):
                        self.current_piece.move_right()

                elif event.key == pygame.K_RIGHT:
                    self.current_piece.move_right()
                    if not self.grid.is_valid_position(self.current_piece):
                        self.current_piece.move_left()

                elif event.key == pygame.K_DOWN:
                    self.current_piece.move_down()
                    if not self.grid.is_valid_position(self.current_piece):
                        self.current_piece.move_up()

                elif event.key == pygame.K_UP:
                    self.current_piece.rotate()
                    if not self.grid.is_valid_position(self.current_piece):
                        self.current_piece.rotate_back()
        return True

    def update(self):
        self.fall_time += self.clock.get_rawtime()
        self.clock.tick()

        if self.fall_time / 1000 >= self.fall_speed:
            self.fall_time = 0
            self.current_piece.move_down()
            if not self.grid.is_valid_position(self.current_piece) and self.current_piece.y > 0:
                self.current_piece.move_up()
                self.lock_piece()

    def lock_piece(self):
        positions = self.current_piece.get_positions()
        for pos in positions:
            self.grid.lock_position(pos, self.current_piece.color)
        self.current_piece = Tetromino()
        self.grid.clear_full_rows()

    def draw(self):
        self.window.fill((0, 0, 0))
        self.grid.draw(self.window)
        self.current_piece.draw(self.window, self.grid)
        pygame.display.update()

    def run(self):
        running = True
        while running:
            running = self.handle_input()
            self.update()
            self.draw()
        pygame.quit() 