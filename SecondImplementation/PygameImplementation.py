import pygame

from Algorithms.A_star import AStarAlgorithm
from Algorithms.BFS_algorithm import BFSAlgorithm
from Algorithms.DFS_algorithm import DFSAlgorithm
from Algorithms.Dijkstra_algorithm import DijkstraAlgorithm
from AlgorithmDictionary import AlgorithmDictionary
from Node import Node
from Colors import Color

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('Shortest Path Visualization')

pygame.font.init()
FONT = pygame.font.SysFont('Arial', 24)

def draw_label(win, text, x, y):
    label = FONT.render(text, True, Color.BLACK.value)
    win.blit(label, (x, y))


def make_grid(rows, width) -> list[list[Node]]:
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    return grid


def draw_grid(win, rows, width) -> None:
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, Color.BLACK.value, (0, i * gap), (width, i * gap))
        pygame.draw.line(win, Color.BLACK.value, (i * gap, 0), (i * gap, width))


def draw(win, grid, rows, width):
    win.fill(Color.WHITE.value)
    for row in grid:
        for node in row:
            node.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    x, y = pos
    return x // gap, y // gap


def clearBefore(grid: list[list[Node]]) -> None:
    for row in grid:
        for node in row:
            if node.is_open() or node.is_closed() or node.is_path():
                node.reset()


def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True

    current_algorithm = "None"  # Zmienna przechowująca nazwę algorytmu

    algorithmDictionary = AlgorithmDictionary()
    while run:
        draw(win, grid, ROWS, width)
        draw_label(win, f"Algorithm: {current_algorithm}", 10, 10)  # Wyświetlanie nazwy algorytmu
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node: Node = grid[row][col]

                if not start and node != end:
                    start = node
                    start.make_start()
                elif not end and node != start:
                    end = node
                    end.make_end()
                elif node != end and node != start:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key in algorithmDictionary.dictionary:
                    clearBefore(grid)
                    draw(win, grid, ROWS, width)
                    current_algorithm = algorithmDictionary.dictionary[event.key].name
                    algorithm = algorithmDictionary.dictionary[event.key].algorithm
                    algorithm.findPath(lambda: draw(win, grid, ROWS, width), grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    current_algorithm = "None"
                    grid = make_grid(ROWS, width)

    pygame.quit()


main(WIN, WIDTH)
