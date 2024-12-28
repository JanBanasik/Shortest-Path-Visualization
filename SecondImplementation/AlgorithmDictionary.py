from Algorithms.PathFindingAlgorithm import PathFindingAlgorithm
import pkgutil
import importlib
import Algorithms

import pygame


class AlgorithmWithName:
    def __init__(self, algorithm, name, letter):
        self.algorithm = algorithm
        self.name = name
        self.letter = letter



def create_key_mapping():
    pygame.init()  # Inicjalizacja Pygame, jeśli jeszcze tego nie zrobiłeś
    key_mapping = {}

    for letter in "abcdefghijklmnopqrstuvwxyz":
        key_constant = getattr(pygame, f"K_{letter}")
        key_mapping[letter] = key_constant

    return key_mapping


for _, module_name, _ in pkgutil.iter_modules(Algorithms.__path__):
    importlib.import_module(f"Algorithms.{module_name}")


class AlgorithmDictionary:
    def __init__(self):
        self.dictionary: dict[str, AlgorithmWithName] = {}
        self.keyMapping = create_key_mapping()
        self.constructDictionary()

    def constructDictionary(self):
        for subclass in PathFindingAlgorithm.__subclasses__():
            algorithm = subclass()
            for letter in subclass.__name__:
                if self.keyMapping[letter.lower()] not in self.dictionary:
                    self.dictionary[self.keyMapping[letter.lower()]] = AlgorithmWithName(algorithm, subclass.__name__, letter)
                    break


# Tworzenie instancji
r = AlgorithmDictionary()
