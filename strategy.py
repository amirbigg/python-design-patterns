"""
    Strategy
"""
from abc import ABC, abstractmethod


class Context:
    def __init__(self, direction, sentence):
        self._direction = direction
        self.sentence = sentence

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, dir):
        self._direction = dir

    def sorting(self):
        return self._direction.direct(self.sentence)


class Direction(ABC):
    @abstractmethod
    def direct(self, data):
        pass

class Right(Direction):
    def direct(self, data):
        print(data[::-1])

class Left(Direction):
    def direct(self, data):
        print(data)

c1 = Context(Left(), 'Hello World...')
c1.sorting()