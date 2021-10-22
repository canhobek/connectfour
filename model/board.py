from model.tile import Tile
from model.abstract_board import AbstractBoard
from exceptions.exceptions import RowIsOutOfBounds, ColumnIsOutOfBounds, PlayPointIsFull, WrongRowReturn
from model.board_model_listener import BoardModelListener


class Board(AbstractBoard):
    def __init__(self, board_row = 6, board_col = 7, tile_type=Tile.EMPTY):
        self._row = board_row
        self._col = board_col
        self._playable_column = [0 if tile_type == Tile.EMPTY else board_row for i in range(self._col)] # [0] * self_col
        self._subscribeList = []
        self.current_row = 0

        """
        self.matrix = []
        i = 0
        j = 0
        while i < board_y:
            self.matrix.append([])
            j = 0
            while j < board_x:
                self.matrix[i].append(tile_type)
                j += 1
            i += 1
        """
        self._matrix = [[tile_type for _ in range(self._row)] for _ in range(self._col)]

    @property
    def get_row_count(self) -> int:
        """
        return the row count of board
        :return: int
        """
        return self._row

    @property
    def get_col_count(self) -> int:
        """
        return the row count of board
        :return: int
        """
        return self._col

    def play(self, col: int, tile: Tile) -> None:
        self._checkBounds(col)
        if not self.is_playable(col):
            raise PlayPointIsFull(tile)
        #play
        self._matrix[self._playable_column[col]][col] = tile
        self._playable_column[col] += 1
        self.notify()

    def _checkBounds(self, col):
        if col < 0 or col > self._col:
            raise ColumnIsOutOfBounds(col)
        if self._playable_column[col] > self._row:
            raise ColumnIsOutOfBounds(col)



    #TODO : encapsulation is fragile
    #def get_board(self) -> list:
    #    return self._matrix

    def is_playable(self, col: int) -> bool:
        """

        :param row:
        :param col:
        :return:
        """
        """if self._matrix[row][col] != Tile.EMPTY:
            return False
        else:
            return True
        """
        self._checkBounds(col)
        return self._matrix[self._playable_column[col]][col] == Tile.EMPTY




    def is_win(self, tile: Tile) -> bool:
        return True

    def is_empty(self) -> bool:
        pass


    def addListener(self, listener: BoardModelListener):
        """
        adding listeners to subscirber list
        :param listener:
        :return:
        """
        self._subscribeList.append(listener)

    def notify(self):
        """
        notifiyng subscribers
        :return:
        """
        [modellistener.board_changed() for modellistener in self._subscribeList]


    def __iter__(self):
        return self

    def __next__(self):
        if self.current_row == self.get_row_count:
            self.current_row = 0
            raise StopIteration()
        row = self._matrix[self.current_row]
        self.current_row += 1
        return row





