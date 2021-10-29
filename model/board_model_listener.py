from abc import abstractmethod


class BoardModelListener:
    @abstractmethod
    def board_changed(self):
        raise NotImplementedError()
