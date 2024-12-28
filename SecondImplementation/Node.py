import pygame
from Colors import Color


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = Color.WHITE.value
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == Color.RED.value

    def is_open(self):
        return self.color == Color.GREEN.value

    def is_barrier(self):
        return self.color == Color.BLACK.value

    def is_start(self):
        return self.color == Color.ORANGE.value

    def is_end(self):
        return self.color == Color.PURPLE.value

    def is_path(self):
        return self.color == Color.BLUE.value

    def reset(self):
        self.color = Color.WHITE.value

    def make_start(self):
        self.color = Color.ORANGE.value

    def make_closed(self):
        self.color = Color.RED.value

    def make_open(self):
        self.color = Color.GREEN.value

    def make_barrier(self):
        self.color = Color.BLACK.value

    def make_end(self):
        self.color = Color.PURPLE.value

    def make_path(self):
        self.color = Color.BLUE.value

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for a, b in DIRECTIONS:
            newX = self.row + a
            newY = self.col + b
            if 0 <= newX < self.total_rows and 0 <= newY < self.total_rows and not grid[newX][newY].is_barrier():
                self.neighbors.append(grid[newX][newY])

    def __lt__(self, other):
        return False

    def __hash__(self):
        return hash((self.x, self.y))
