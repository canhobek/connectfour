
from PyQt5.QtCore import QSize, Qt, QRect
from PyQt5.QtGui import QPaintEvent, QMouseEvent, QPainter, QColor
from PyQt5.QtWidgets import QMainWindow

from model.board_model_listener import BoardModelListener
from controller.desktop.mouse_controller import MouseController
from model.tile import Tile


class GameWindow(QMainWindow, BoardModelListener):
    WIDTH = 700
    HEIGHT = 600
    COL_WIDTH = 100
    TILE_DIAMETER = 90

    def __init__(self, board, *players, title="Connect Four"):
        super(GameWindow, self).__init__()
        self.setWindowTitle(title)
        self.setFixedSize(QSize(GameWindow.WIDTH, GameWindow.HEIGHT))
        self._board = board

        self._board.addListener(self)

        self.mouseController = MouseController(board, self)


    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)

        for x in range(GameWindow.COL_WIDTH, GameWindow.WIDTH, GameWindow.COL_WIDTH):
            painter.drawLine(x, 0, x, GameWindow.HEIGHT)

        tile_list = []
        r = 0
        for row in self._board:
            c = 0

            for elem in row:
                if elem == Tile.EMPTY:
                    c += GameWindow.COL_WIDTH
                    continue

                if elem == Tile.RED:
                    painter.setPen(QColor(255, 0, 0))
                elif elem == Tile.BLUE:
                   painter.setPen(QColor(0, 0, 255))

                tile_list.append(QRect(c, GameWindow.HEIGHT - GameWindow.TILE_DIAMETER + r,
                                    GameWindow.TILE_DIAMETER, GameWindow.TILE_DIAMETER))

                c += GameWindow.COL_WIDTH
            r -= GameWindow.COL_WIDTH


        for rect in tile_list:
            painter.drawEllipse(rect)

    def mouseDoubleClickEvent(self, mouseEvent: QMouseEvent) -> None:
        if mouseEvent.button() == Qt.LeftButton:
            self.mouseController.mouseDoubleClickEvent(mouseEvent, Tile.RED)

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            #self.pressPos = event.pos()
            pass

    def _draw_board(self):
        """
        painter = QPainter()
        r = 0
        for row in self._board:
            c = 0

            for elem in row:
                if elem == Tile.EMPTY:
                    c += GameWindow.COL_WIDTH
                    continue

                #if elem == Tile.RED:
                #    painter.setPen(QColor(255, 0, 0))
                #elif elem == Tile.BLUE:
                #    painter.setPen(QColor(0, 0, 255))

                painter.drawEllipse(c, GameWindow.HEIGHT - GameWindow.TILE_DIAMETER + r,
                                    GameWindow.TILE_DIAMETER, GameWindow.TILE_DIAMETER)

                c += GameWindow.COL_WIDTH
            r += GameWindow.COL_WIDTH
        """

    def board_changed(self):
        """
        abstract method imp. model listener
        """
        print("board changedmiş")
        GameWindow.R = 0

        self.update()
        #self.repaint()


