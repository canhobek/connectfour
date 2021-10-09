from abc import ABC, abstractmethod
from model.tile import Tile

class AbstractBoard(ABC):
    @abstractmethod
    def get_row_count(self)->int:
        raise NotImplementedError("get row count must be imlpemented")

    @abstractmethod
    def get_col_count(self)->int:
        raise NotImplementedError("get col count must be imlpemented")

    @abstractmethod
    def play(self, row:int, col:int, tile:Tile)->None:
        raise NotImplementedError("play method must be implemented")

    @abstractmethod
    def get_board(self)->list:
        raise NotImplementedError("get method must be implemented")

    @abstractmethod
    def is_playable(self, row:int, col:int)->bool:
        raise NotImplementedError("is playable must be implemented")

    @abstractmethod
    def is_win(self, tile:Tile)->bool:
        raise NotImplementedError("is win must be implemented")

    @abstractmethod
    def is_empty(self)->bool:
        raise NotImplementedError("is empty must be implemented")
