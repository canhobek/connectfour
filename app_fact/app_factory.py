import sys
from enum import Enum, auto, unique

from PyQt5.QtWidgets import QApplication

from controller.console.console_controller import ConsoleController
from controller.web.web_controller import WebView
from model.board import Board
from model.player import Player
from model.tile import Tile
from view.console.console_view import ConsoleView
from view.desktop.game_window import GameWindow


@unique
class AppType(Enum):
    CONSOLE = auto()
    DESKTOP = auto()
    WEB = auto()


class AppFactory:
    @staticmethod
    def startApp(app_type:AppType):
        func = AppFactory.app_dict[app_type]
        func(None, Board(), [Player("Can", Tile.BLUE), Player("Onur", Tile.RED)])


    def __getConsoleApp(self, board, players):
        console_view = ConsoleView(board, players)
        cont = ConsoleController(board, console_view)

        # Start the event loop.
        console_view.main_loop()


    def __getDesktopApp(self, board, players):
        app = QApplication(sys.argv)

        window = GameWindow(board, players)
        window.show()

        # Start the event loop.
        app.exec()



    def __getWebApp(self, board, players):
        web_view = WebView(board, players)
        web_view.run()

    app_dict = {AppType.CONSOLE: __getConsoleApp, AppType.DESKTOP: __getDesktopApp, AppType.WEB: __getWebApp}

