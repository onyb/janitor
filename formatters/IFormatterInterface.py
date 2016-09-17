from abc import ABCMeta
from abc import abstractmethod


class IFormatterInterface(object, metaclass=ABCMeta):
    """
    Interface to be implemented by every Formatter
    """
    @abstractmethod
    def process(self, code: str) -> str:
        raise NotImplementedError
