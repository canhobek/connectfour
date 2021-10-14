from model.tile import Tile
from model.abstract_board import AbstractBoard
from exceptions.exceptions import RowIsOutOfBounds, ColumnIsOutOfBounds, PlayPointIsFull, WrongRowReturn


class Board(AbstractBoard):
    def __init__(self, board_x = 7, board_y = 6, tile_type=Tile.EMPTY):
        self.x = board_x
        self.y = board_y
        self.matrix = []
        i = 0
        j = 0
        while i < board_y:
            self.matrix.append([])
            while j < board_x:
                self.matrix[i].append(tile_type)
                j += 1
            i += 1

    @property
    def get_row_count(self) -> int:
        """

        :return:
        """
        board = Board()
        if(self.x != board.get_row_count):
            raise WrongRowReturn
        return self.x

    @property
    def get_col_count(self) -> int:
        """

        :return:
        """
        return self.y

    def play(self, row: int, col: int, tile: Tile) -> None:
        if(row < 1 or row > self.x + 1):
            raise RowIsOutOfBounds(row)

        if(col < 1 or col > self.y + 1):
            raise ColumnIsOutOfBounds(col)

        if(self.matrix[row][col] != tile.EMPTY):
            raise PlayPointIsFull(tile)

        pass
    #TODO : encapsulation is fragile
    def get_board(self) -> list:
        """for i in range(self.x):
            for j in range(self.y):
                print(self.matrix[i][j], end=' ')
            print('\n')"""
        print(self.matrix[0])

    def is_playable(self, row: int, col: int) -> bool:
        pass

    def is_win(self, tile: Tile) -> bool:
        pass

    def is_empty(self) -> bool:
        pass




