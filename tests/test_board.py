import unittest
from model.board import Board
from model.tile import Tile
from exceptions.exceptions import RowIsOutOfBounds

class TestBoard(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


    def test_invalid_row_to_play_board(self):
        """
        Invalid row index to play board, expects RowIndexOutOfBounds exception
        :return:
        """
        board = Board()
        self.assertRaises(RowIsOutOfBounds, lambda: board.play(20, 4, Tile.BLUE))










if __name__ == '__main__':
    unittest.main()
