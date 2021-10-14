import unittest
from model.board import Board
from model.tile import Tile
from exceptions.exceptions import RowIsOutOfBounds, ColumnIsOutOfBounds, PlayPointIsFull, WrongRowReturn

class TestBoard(unittest.TestCase):
    """
    def test_something(self):
        self.assertEqual(True, False)
    """

    def test_invalid_row_to_play_board(self):
        """
        Invalid row index to play board, expects RowIndexOutOfBounds exception
        :return:
        """
        board = Board()
        self.assertRaises(RowIsOutOfBounds, lambda: board.play(20, 4, Tile.BLUE))

    def test_invalid_column_to_play_board(self):
        """
        Invalid column index to play board, excepts ColumnIndexOutOfBounds exception
        :return:
        """
        board = Board()
        self.assertRaises(ColumnIsOutOfBounds, lambda: board.play(2, 20, Tile.RED))

    def test_point_ot_play_is_full(self):
        """
        Looking for if the place of play on board is full.
        :return:
        """
        board = Board(tile_type=Tile.BLUE)
        self.assertRaises(PlayPointIsFull, lambda: board.play(5, 5, Tile.BLUE))

    def test_get_board(self):
        board = Board()
        board.get_board()






"""
    def test_if_row_count_true(self):
        
        Invalid return value of x dimension of board.
        :return:
        
        board = Board()
        a = board.get_row_count
        b = board.x
        self.assertEqual(a, b)

        #count = self.assertRaises(WrongRowReturn, lambda: board.get_row_count)
"""







if __name__ == '__main__':
    unittest.main()
