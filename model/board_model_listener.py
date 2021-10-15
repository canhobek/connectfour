from abc import ABC, abstractmethod

class BoardModelListener(ABC):
    @abstractmethod
    def board_changed(self):
        pass