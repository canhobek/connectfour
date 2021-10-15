from model.tile import Tile
class Player:
    def __init__(self, name: str, tile: Tile):
        self._name = name
        self._tile = tile

    @property
    def name (self):
        return self._name

    @property
    def tile(self):
        return self._tile

    def __str__(self):
        return f"{self._name} is player with tile {self._tile}."