from model.tile import Tile
from model.abstract_board import AbstractBoard
from exceptions.exceptions import RowIsOutOfBounds

class Board(AbstractBoard):
    def __init__(self, board_x = 7, board_y = 6):
        self.x = board_x
        self.y = board_y
        self.matrix = []
        i = 0
        j = 0
        while i < board_y:
            self.matrix.append([])
            while j < board_x:
                self.matrix[i].append(Tile.EMPTY)
                j += 1
            i += 1

    @property
    def get_row_count(self) -> int:
        """

        :return:
        """
        pass

    @property
    def get_col_count(self) -> int:
        pass

    def play(self, row: int, col: int, tile: Tile) -> None:
        if(row < 1 or row > self.x + 1):
            raise RowIsOutOfBounds(row)

        pass
    #TODO : encapsulation is fragile
    def get_board(self) -> list:
        pass

    def is_playable(self, row: int, col: int) -> bool:
        pass

    def is_win(self, tile: Tile) -> bool:
        pass

    def is_empty(self) -> bool:
        pass




