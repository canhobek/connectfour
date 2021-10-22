from model.board import Board
from model.tile import Tile
from model.player import Player
from view.console_view import ConsoleView
from controller.console_controller import ConsoleController

def main():
    board = Board()
    p1 = Player("Can", Tile.BLUE)
    p2 = Player("Onur", Tile.RED)
    console_view = ConsoleView(board, p1, p2)
    cont = ConsoleController(board, console_view)

    console_view.main_loop()

if __name__ == '__main__':
    main()