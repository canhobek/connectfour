from enum import Enum, auto

class Tile(Enum):
    EMPTY = auto()
    RED = auto()
    BLUE = auto()

    #TODO
    def print_label(self):
        pass