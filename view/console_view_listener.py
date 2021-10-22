from abc import ABC, abstractmethod
from model.player import Player

class ConsoleViewListener(ABC):
    @abstractmethod
    def input_recieved(self, col: int, player: Player):
        pass