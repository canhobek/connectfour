from abc import abstractmethod

from model.player import Player


class ConsoleViewListener:
    @abstractmethod
    def input_received(self, col: int, player: Player):
        raise NotImplementedError()
