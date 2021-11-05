from exceptions.exceptions import ColumnIsOutOfBounds, PlayPointIsFull
from model.abstract_board import AbstractBoard
from model.board_model_listener import BoardModelListener
from model.tile import Tile
from model.player import Player

from typing import Tuple


class Board(AbstractBoard):
    def __init__(self, board_row=6, board_col=7, tile_type=Tile.EMPTY):
        self._row = board_row
        self._col = board_col
        self.__playable_column = [0] * self._col
        self.__subscribeList = []
        self.__current_row = 0
        self._board = [[tile_type for _ in range(self._col)] for _ in range(self._row)]

    def get_board(self):
        return self._board

    @property
    def row_count(self) -> int:
        """
        return the row count of board
        :return: int
        """
        return self._row

    @property
    def column_count(self) -> int:
        """
        return the row count of board
        :return: int
        """
        return self._col

    def play(self, col: int, tile: Tile) -> None:
        self._checkBounds(col)
        if not self.is_playable(col):
            raise PlayPointIsFull(tile)
        # play
        self._board[self.__playable_column[col]][col] = tile
        self.__playable_column[col] += 1
        self.notify()

    def _checkBounds(self, col):
        if col < 0 or col > self._col:
            raise ColumnIsOutOfBounds(col)
        if self.__playable_column[col] > self._row:
            raise ColumnIsOutOfBounds(col)

    def is_playable(self, col: int) -> bool:
        """
        :param col:
        :return:
        """
        self._checkBounds(col)
        return self._board[self.__playable_column[col]][col] == Tile.EMPTY

    def is_win(self, player: Player) -> Tuple[bool, Player]:
        tile = player.tile
        def rows():
            for r in range(self.row_count):
                for c in range(self.column_count - 3):
                    if self._board[r][c] == tile.value and \
                            self._board[r][c + 1] == tile.value and \
                            self._board[r][c + 2] == tile.value and \
                            self._board[r][c + 3] == tile.value:
                        return True
            return False

        def cols():
            for c in range(self.column_count):
                for r in range(self.row_count - 3):
                    if self._board[r][c] == tile.value and \
                            self._board[r + 1][c] == tile.value and \
                            self._board[r + 2][c] == tile.value and \
                            self._board[r + 3][c] == tile.value:
                        return True
            return False

        def diagonal():
            # Check positively sloped diaganols
            for c in range(self.column_count - 3):
                for r in range(self.row_count - 3):
                    if self._board[r][c] == tile.value and \
                            self._board[r + 1][c + 1] == tile.value and \
                            self._board[r + 2][c + 2] == tile.value and \
                            self._board[r + 3][c + 3] == tile.value:
                        return True
            return False

        def antiDiagonal():
            # Check negatively sloped diaganols
            for c in range(self.column_count - 3):
                for r in range(3, self.row_count):
                    if self._board[r][c] == tile.value and \
                            self._board[r - 1][c + 1] == tile.value and \
                            self._board[r - 2][c + 2] == tile.value and \
                            self._board[r - 3][c + 3] == tile.value:
                        return True
            return False

        return rows() or cols() or diagonal() or antiDiagonal(), player

    def is_full(self) -> bool:
        for row in self._board:
            if row.count(Tile.EMPTY.value) > 0:
                return False
        return True

    def addListener(self, listener: BoardModelListener):
        """
        adding listeners to subscirber list
        :param listener:
        :return:
        """
        self.__subscribeList.append(listener)

    def notify(self):
        """
        notifiyng subscribers
        :return:
        """
        [modellistener.board_changed() for modellistener in self.__subscribeList]

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_row == self.row_count:
            self.__current_row = 0
            raise StopIteration()
        row = self._board[self.__current_row]
        self.__current_row += 1
        return row
