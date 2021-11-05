from PyQt5.QtCore import QSize, Qt, QRect
from PyQt5.QtGui import QPaintEvent, QMouseEvent, QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from model.board_model_listener import BoardModelListener
from controller.desktop.mouse_controller import MouseController
from model.tile import Tile
from model.player import CircularPlayerIterator


class GameWindow(QMainWindow, BoardModelListener):
    WIDTH = 700
    HEIGHT = 600
    COL_WIDTH = 100
    TILE_DIAMETER = 100

    def __init__(self, board, players, title="Connect Four"):
        super(GameWindow, self).__init__()
        self.setWindowTitle(title)
        self.setFixedSize(QSize(GameWindow.WIDTH, GameWindow.HEIGHT))
        self._board = board

        self._board.addListener(self)

        self._player_iter = CircularPlayerIterator(players)
        self._current_player = None

        self.mouseController = MouseController(board, self)

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)

        for x in range(GameWindow.COL_WIDTH, GameWindow.WIDTH, GameWindow.COL_WIDTH):
            painter.drawLine(x, 0, x, GameWindow.HEIGHT)

        self._draw_board(painter)

    def mouseDoubleClickEvent(self, mouseEvent: QMouseEvent) -> None:
        if mouseEvent.button() == Qt.LeftButton:
            self._current_player =  next(self._player_iter);
            self.mouseController.mouseDoubleClickEvent(mouseEvent, self._current_player.tile)

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            # self.pressPos = event.pos()
            pass

    def _draw_board(self, painter):
        r = 0
        for row in self._board:
            c = 0
            for elem in row:
                if elem == Tile.EMPTY:
                    c += GameWindow.COL_WIDTH
                    continue

                if elem == Tile.RED:
                    painter.setBrush(QColor(183, 0, 0))
                elif elem == Tile.BLUE:
                    painter.setBrush(QColor(0, 0, 160))

                painter.drawEllipse(QRect(c, GameWindow.HEIGHT - GameWindow.TILE_DIAMETER + r,
                                          GameWindow.TILE_DIAMETER, GameWindow.TILE_DIAMETER))

                c += GameWindow.COL_WIDTH
            r -= GameWindow.COL_WIDTH

    def board_changed(self):
        """
        abstract method imp. model listener
        """
        game_status, msg = self.__isGameEnd(self._current_player)
        if game_status:
            QMessageBox.information(self, "Game Over", msg)

        self.update()  # trigger paintEvent



    def __isGameEnd(self, currentPlayer):
        if self._board.is_win(currentPlayer):
            currentPlayer.score += 1
            return True, f"{currentPlayer.name} wins"
        if self._board.is_full():
            return True, f"Board is full - TIE"
        return False, ""