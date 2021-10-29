from model.tile import Tile


class Player:
    def __init__(self, name: str, tile: Tile):
        self._name = name
        self._tile = tile

    @property
    def name(self):
        return self._name

    @property
    def tile(self):
        return self._tile

    def __str__(self):
        return f"{self._name} is player with tile {self._tile}."

    def __repr__(self):
        return self.__str__()


class CircularPlayerIterator:
    def __init__(self, player_data):
        self._data = player_data
        self._current = 0
        self._data_size = len(player_data)

    def __iter__(self):
        return self

    def __next__(self):
        player = self._data[self._current]
        self._current += 1
        self._current %= self._data_size
        return player
