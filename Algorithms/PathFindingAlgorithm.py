from abc import ABC, abstractmethod


class PathFindingAlgorithm(ABC):

    @abstractmethod
    def findPath(self, draw, grid, start, end):
        pass
