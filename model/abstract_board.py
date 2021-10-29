from abc import ABC, abstractmethod

from model.tile import Tile


class AbstractBoard(ABC):
    @abstractmethod
    def row_count(self)->int:
        raise NotImplementedError("get row count must be imlpemented")

    @abstractmethod
    def column_count(self)->int:
        raise NotImplementedError("get col count must be imlpemented")

    @abstractmethod
    def play(self, col:int, tile:Tile)->None:
        raise NotImplementedError("play method must be implemented")

    #@abstractmethod
    #def get_board(self)->list:
    #    raise NotImplementedError("get method must be implemented")

    @abstractmethod
    def is_playable(self, col:int)->bool:
        raise NotImplementedError("is playable must be implemented")

    @abstractmethod
    def is_win(self, tile:Tile)->bool:
        raise NotImplementedError("is win must be implemented")

    @abstractmethod
    def is_full(self)->bool:
        raise NotImplementedError("is empty must be implemented")

