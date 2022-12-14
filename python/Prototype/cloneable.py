from abc import ABCMeta, abstractmethod


class Cloneable(metaclass=ABCMeta):
    @abstractmethod
    def create_clone(self) -> None:
        raise NotImplementedError()