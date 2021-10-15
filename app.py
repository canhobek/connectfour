from model.board import Board
from model.tile import Tile
from model.player import Player

def main():
    board = Board()
    p1 = Player("Can", Tile.BLUE)
    p2 = Player("Onur", Tile.RED)
    console_view = ConsoleView(board, p1, p2)

    console_view.game_loop()

if __name__ == '__main__':
    main()