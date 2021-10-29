from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPaintEvent, QMouseEvent, QPainter
from PyQt5.QtWidgets import QMainWindow

from model.board_model_listener import BoardModelListener
from controller.desktop.mouse_controller import MouseController

class GameWindow(QMainWindow, BoardModelListener):
    WIDTH = 700
    HEIGHT = 600

    def __init__(self, board, *players, title="Connect Four"):
        super(GameWindow, self).__init__()
        self.setWindowTitle(title)
        self.setFixedSize(QSize(GameWindow.WIDTH, GameWindow.HEIGHT))
        self._board = board
        self.mouseController = MouseController(board, self)


        self

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)

        for x in range(100, GameWindow.WIDTH, 100):
            painter.drawLine(x, 0, x, GameWindow.HEIGHT)

    def mouseDoubleClickEvent(self, mouseEvent: QMouseEvent) -> None:
        self.mouseController.mouseDoubleClickEvent(mouseEvent)

    def board_changed(self):
        """
        abstract method imp. model listener
        """
        pass
