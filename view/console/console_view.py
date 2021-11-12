from typing import List

from model.exceptions.exceptions import GameAbortedException
from model.board import Board
from model.board_model_listener import BoardModelListener
from model.player import CircularPlayerIterator
from model.player import Player
from view.console.console_view_listener import ConsoleViewListener


class ConsoleView(BoardModelListener):
    def __init__(self, board: Board, players: List[Player]):
        self._board = board
        self._board.addListener(self)
        self._subscribeList = []
        self._player_iter = CircularPlayerIterator(players)

    @property
    def board(self):
        return self._board

    def display_board(self) -> None:
        print()
        for row in reversed(self.board.get_board()):
            print(end="|")
            for item in row:
                print(item.get_display_str(), end="|")
            print()
        print("_" * int(self.board.row_count * 2 + 1))

    def get_console_input(self, player):
        try:
            column = int(input(f"{player} please enter col to play [-1 aborts game]"))
            if column == -1:
                raise GameAbortedException(player)
            column -= 1
            self.notify(column, player)
        except ValueError:
            print("Invalid column number")
            return False
        except Exception as ce:
            print(ce)
            return False

        return True

    def main_loop(self):
        self.display_board()
        for current_player in self._player_iter:
            try:
                while not self.get_console_input(current_player):
                    pass

            except GameAbortedException as ge:
                print(ge)
                break

            # TODO: game end break
            if self.__isGameEnd(current_player):
                print(current_player, "wins")
                break

    def __isGameEnd(self, currentPlayer):
        if self._board.is_win(currentPlayer):
            print(f"{currentPlayer.name} wins")
            currentPlayer.score += 1
            return True
        if self._board.is_full():
            print("TIE")
            return True
        return False

    def add_listener(self, listener: ConsoleViewListener):
        self._subscribeList.append(listener)

    def notify(self, col: int, player: Player):
        [i.input_received(col, player) for i in self._subscribeList]

    def board_changed(self):
        self.display_board()
