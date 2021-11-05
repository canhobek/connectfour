from abc import ABC, abstractmethod

from model.tile import Tile
from model.player import Player
from typing import Tuple


class AbstractBoard(ABC):
    @abstractmethod
    def get_board(self):
        pass

    @abstractmethod
    def row_count(self) -> int:
        raise NotImplementedError("get row count must be implemented")

    @abstractmethod
    def column_count(self) -> int:
        raise NotImplementedError("get col count must be implemented")

    @abstractmethod
    def play(self, col: int, tile: Tile) -> None:
        raise NotImplementedError("play method must be implemented")

    # @abstractmethod
    # def get_board(self)->list:
    #    raise NotImplementedError("get method must be implemented")

    @abstractmethod
    def is_playable(self, col: int) -> bool:
        raise NotImplementedError("is playable must be implemented")

    @abstractmethod
    def is_win(self, player: Player) -> Tuple[bool, Player]:
        raise NotImplementedError("is win must be implemented")

    @abstractmethod
    def is_full(self) -> bool:
        raise NotImplementedError("is empty must be implemented")
