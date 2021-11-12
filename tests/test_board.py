import unittest

from model.exceptions.exceptions import ColumnIsOutOfBounds, PlayPointIsFull
from model.board import Board
from model.tile import Tile
from model.player import Player


class TestBoard(unittest.TestCase):
    """
    def test_something(self):
        self.assertEqual(True, False)
    """

    blue_player = Player("bluePlayer", Tile.BLUE)

    def test_invalid_column_to_play_board(self):
        """
        Invalid column index to play board, excepts ColumnIndexOutOfBounds exception
        :return:
        """
        board = Board()
        self.assertRaises(ColumnIsOutOfBounds, lambda: board.play(20, Tile.RED))

    def test_point_ot_play_is_full(self):
        """
        Looking for if the place of play on board is full.
        :return:
        """
        board = Board(tile_type=Tile.BLUE)
        self.assertRaises(PlayPointIsFull, lambda: board.play(5, Tile.BLUE))

    def test_is_win_blue_wins_horizontal(self):
        board = Board()
        board.play(0, Tile.BLUE)
        board.play(0, Tile.RED)
        board.play(1, Tile.BLUE)
        board.play(5, Tile.RED)
        board.play(2, Tile.BLUE)
        board.play(1, Tile.RED)
        board.play(3, Tile.BLUE)

        self.assertTrue(board.is_win(TestBoard.blue_player))

    def test_row_blue_wins(self):
        game = Board()
        game.play(1, Tile.BLUE)
        game.play(2, Tile.BLUE)
        game.play(3, Tile.BLUE)
        game.play(4, Tile.BLUE)

        self.assertTrue(game.is_win(TestBoard.blue_player))

    def test_row_blue_have_four_but_not_consecutive(self):
        game = Board()
        game.play(1, Tile.BLUE)
        game.play(2, Tile.BLUE)
        game.play(5, Tile.BLUE)
        game.play(6, Tile.BLUE)

        self.assertFalse(game.is_win(TestBoard.blue_player))

    def test_col_blue_wins(self):
        game = Board()
        game.play(2, Tile.BLUE)
        game.play(2, Tile.BLUE)
        game.play(2, Tile.BLUE)
        game.play(2, Tile.BLUE)

        self.assertTrue(game.is_win(TestBoard.blue_player))

    def test_col2_blue_stopped(self):
        game = Board()
        game.play(2, Tile.RED)
        game.play(2, Tile.BLUE)
        game.play(2, Tile.BLUE)
        game.play(2, Tile.BLUE)
        game.play(2, Tile.RED)
        game.play(2, Tile.BLUE)

        self.assertTrue(game.is_win(TestBoard.blue_player))

    def test_diagonal_blue_wins(self):
        game = Board()
        game.play(1, Tile.BLUE)
        game.play(2, Tile.BLUE)
        game.play(2, Tile.BLUE)
        game.play(3, Tile.RED)
        game.play(3, Tile.RED)
        game.play(3, Tile.BLUE)
        game.play(4, Tile.RED)
        game.play(4, Tile.BLUE)
        game.play(4, Tile.RED)
        game.play(4, Tile.BLUE)

        self.assertTrue(game.is_win(TestBoard.blue_player))

    def test_if_row_and_col__default_count_true(self):
        """
        Invalid return value of x dimension of board.
        :return:
        """

        board = Board()

        self.assertEqual(6, board.row_count)
        self.assertEqual(7, board.column_count)

    def test_create_board(self):
        board = Board()

        self.assertEqual(6, len(board.get_board()))
        self.assertEqual(7, len(board.get_board()[0]))


if __name__ == '__main__':
    unittest.main()
