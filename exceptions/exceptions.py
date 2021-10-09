class RowIsOutOfBounds(Exception):
    def __init__(self, row:int):
        super(RowIsOutOfBounds, self).__init__(f"{row} is out of bounds.")