from enum import Enum, auto, unique


@unique
class Tile(Enum):
    EMPTY = auto()
    RED = auto()
    BLUE = auto()

    '''
    def __str__(self):
        if self == Tile.EMPTY:
            return "_"
        elif self == Tile.RED:
            return "R"
        else:
            return "B"

    def __repr__(self):
        return self.__str__()
    '''
