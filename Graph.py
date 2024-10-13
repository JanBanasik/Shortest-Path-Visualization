from abc import ABC, abstractmethod


class Graph(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_edge(self, u, v, weight=1):
        pass

    @abstractmethod
    def remove_edge(self, u, v):
        pass

    @abstractmethod
    def traverse(self, algorithm, source, destination):
        pass
