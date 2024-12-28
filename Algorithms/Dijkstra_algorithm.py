import pygame
import heapq  # Do priorytetowej kolejki

from Algorithms.PathFindingAlgorithm import PathFindingAlgorithm


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


class DijkstraAlgorithm(PathFindingAlgorithm):
    def findPath(self, draw, grid, start, end):
        for row in grid:
            for node in row:
                node.update_neighbors(grid)

        # Priorytetowa kolejka (koszt, węzeł)
        priority_queue = []
        heapq.heappush(priority_queue, (0, start))

        came_from = {}
        cost_so_far = {node: float('inf') for row in grid for node in row}
        cost_so_far[start] = 0

        while priority_queue:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Pobierz węzeł o najmniejszym koszcie
            current_cost, current_node = heapq.heappop(priority_queue)

            # Jeśli dotarliśmy do celu
            if current_node == end:
                reconstruct_path(came_from, end, draw)
                end.make_end()
                start.make_start()
                return True

            # Aktualizuj sąsiadów
            for neighbor in current_node.neighbors:
                new_cost = cost_so_far[current_node] + 1  # Załóżmy, że wagi krawędzi to 1
                if new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    came_from[neighbor] = current_node
                    heapq.heappush(priority_queue, (new_cost, neighbor))
                    neighbor.make_open()

            draw()

            if current_node != start:
                current_node.make_closed()

        print("No path found!")
        return False
