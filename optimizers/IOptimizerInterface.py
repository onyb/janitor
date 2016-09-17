from abc import ABCMeta
from abc import abstractmethod


class IOptimizerInterface(object, metaclass=ABCMeta):
    """
    Interface to be implemented by every Optimizer
    """
    @abstractmethod
    def process(self, code: str) -> str:
        raise NotImplementedError
