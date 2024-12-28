from queue import PriorityQueue
import pygame

from Algorithms.PathFindingAlgorithm import PathFindingAlgorithm


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


class AStarAlgorithm(PathFindingAlgorithm):

    def findPath(self, draw, grid, start, end):
        for row in grid:
            for node in row:
                node.update_neighbors(grid)
        count = 0
        pq = PriorityQueue()
        pq.put((0, count, start))  # f_score, count, node
        came_from = {}
        g_score = {node: float('inf') for row in grid for node in row}
        g_score[start] = 0
        f_score = {node: float('inf') for row in grid for node in row}
        f_score[start] = h(start.get_pos(), end.get_pos())
        open_set_hash = {start}

        while not pq.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            current = pq.get()[2]
            open_set_hash.remove(current)
            if current == end:
                reconstruct_path(came_from, end, draw)
                end.make_end()
                start.make_start()
                return True

            for neighbor in current.neighbors:
                temp_g_score = g_score[current] + 1

                if temp_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                    if neighbor not in open_set_hash:
                        count += 1
                        pq.put((f_score[neighbor], count, neighbor))
                        open_set_hash.add(neighbor)
                        neighbor.make_open()
            draw()

            if current != start:
                current.make_closed()

        return False
