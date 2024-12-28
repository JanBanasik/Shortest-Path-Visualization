from Algorithms.PathFindingAlgorithm import PathFindingAlgorithm
import pkgutil
import importlib
import Algorithms

import pygame


class AlgorithmWithName:
    def __init__(self, algorithm, name):
        self.algorithm = algorithm
        self.name = name


def create_key_mapping():
    pygame.init()  # Inicjalizacja Pygame, jeśli jeszcze tego nie zrobiłeś
    key_mapping = {}

    # Iteracja po literach alfabetu
    for letter in "abcdefghijklmnopqrstuvwxyz":
        key_constant = getattr(pygame, f"K_{letter}")  # Pobieramy stałą pygame.K_a, pygame.K_b, itd.
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
            print(f"Name: {subclass.__name__}")
            for letter in subclass.__name__:
                if self.keyMapping[letter.lower()] not in self.dictionary:
                    self.dictionary[self.keyMapping[letter.lower()]] = AlgorithmWithName(algorithm, subclass.__name__)
                    break


# Tworzenie instancji
r = AlgorithmDictionary()
for el in r.dictionary:
    print(r.dictionary[el].name)
