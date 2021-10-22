class RowIsOutOfBounds(Exception):
    def __init__(self, row:int):
        super(RowIsOutOfBounds, self).__init__(f"{row} is out of bounds.")


class ColumnIsOutOfBounds(Exception):
    def __init__(self, column: int):
        super(ColumnIsOutOfBounds, self).__init__(f"{column} is out of bounds.")

class PlayPointIsFull(Exception):
    def __init__(self, tile_type):
        super(PlayPointIsFull, self).__init__(f"{tile_type} is already played there.")

class GameAbortedException(Exception):
    def __init__(self, player):
        super(GameAbortedException, self).__init__(f"{player} aborted the game. ")





class WrongRowReturn(Exception):
    def __init__(self, row:int):
        super(WrongRowReturn, self).__init__(f"{row} is not the true x dimension of board.")