from enum import Enum, auto, unique


@unique
class Tile(Enum):
    EMPTY = auto()
    RED = auto()
    BLUE = auto()

    def get_display_str(self):
        if self == Tile.EMPTY:
            return "_"
        elif self == Tile.RED:
            return "R"
        else:
            return "B"
