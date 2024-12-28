from collections import deque
import pygame

from Algorithms.PathFindingAlgorithm import PathFindingAlgorithm


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


class BFSAlgorithm(PathFindingAlgorithm):

    def findPath(self, draw, grid, start, end):
        for row in grid:
            for node in row:
                node.update_neighbors(grid)
        q = deque([start])
        came_from = {}
        visited = set()
        visited.add(start)

        while q:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            currentNode = q.popleft()

            if currentNode == end:
                reconstruct_path(came_from, end, draw)
                end.make_end()
                start.make_start()
                return True

            for neighbor in currentNode.neighbors:
                if neighbor not in visited:
                    came_from[neighbor] = currentNode
                    visited.add(neighbor)
                    q.append(neighbor)
                    neighbor.make_open()

            draw()

            if currentNode != start:
                currentNode.make_closed()

        print("No path found!")
        return False

