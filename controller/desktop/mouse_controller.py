from model.board import Board
from PyQt5.QtGui import QMouseEvent


class MouseController:
    def __init__(self, board: Board, view):
        self._board = board
        self._view = view

    def mouseDoubleClickEvent(self, mouseEvent: QMouseEvent, tile) -> None:
        currentPos = mouseEvent.pos()
        col = currentPos.x() // 100
        print(col)
        self._board.play(col, tile)


