import sys

from PyQt5.QtWidgets import QApplication

from controller.console.console_controller import ConsoleController
from controller.web.web_controller import WebView
from model.board import Board
from model.player import Player
from model.tile import Tile
from view.console.console_view import ConsoleView
from view.desktop.game_window import GameWindow


# TODO: add application factory pattern to implement different application
class Application:
    def __init__(self):
        self._board = Board()
        self._players = [Player("Deniz", Tile.BLUE), Player("Onur", Tile.RED)]

    def create_console_application(self):
        console_view = ConsoleView(self._board, self._players)
        cont = ConsoleController(self._board, console_view)

        # Start the event loop.
        console_view.main_loop()

    def create_desktop_application(self):
        app = QApplication(sys.argv)

        window = GameWindow(self._board, self._players)
        window.show()

        # Start the event loop.
        app.exec()

    def create_web_application(self):
        web_view = WebView(self._board, self._players)
        web_view.run()


if __name__ == '__main__':
    app = Application()
    #app.create_console_application()
    app.create_desktop_application()
    #app.create_web_application()
