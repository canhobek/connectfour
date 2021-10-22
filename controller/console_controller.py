from view.console_view_listener import ConsoleViewListener
from model.player import Player
from model.board import Board
from view.console_view import ConsoleView
from exceptions.exceptions import ColumnIsOutOfBounds, PlayPointIsFull

class ConsoleController(ConsoleViewListener):
    def __init__(self, board: Board, view: ConsoleView):
        self._board = board
        self._view = view

        self._view.add_listener(self)









    def input_recieved(self, col: int, player: Player):
        try:
            self._board.play(col, player.tile)
        except ColumnIsOutOfBounds as ciob:
            raise ciob

        except PlayPointIsFull as ppif:
            raise ppif
