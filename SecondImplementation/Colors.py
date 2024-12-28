from enum import Enum

class Color(Enum):
    RED = (255, 87, 87)       # Zamknięte węzły (intensywnie czerwony)
    GREEN = (144, 238, 144)   # Otwarte węzły (jasnozielony)
    BLUE = (30, 144, 255)     # Ścieżka (niebieski)
    WHITE = (255, 255, 255)   # Puste pola (biały)
    BLACK = (50, 50, 50)      # Bariery (ciemnoszary)
    YELLOW = (255, 255, 153)  # Obszar tymczasowy (bladożółty)
    PURPLE = (138, 43, 226)   # Węzeł końcowy (fioletowy)
    ORANGE = (255, 165, 0)    # Węzeł startowy (pomarańczowy)
