"""
	Strategy
	- a behavioral design pattern that lets you define a family of algorithms,
	put each of them into a separate class, and make their objects interchangeable.
"""
import abc


class Read: # Context
	def __init__(self, sentence):
		self.sentence = sentence
		self._direction = None # strategy instance

	def set_direction(self, direction): # set_strategy
		self._direction = direction

	def read(self):
		return self._direction.direct(self.sentence)


class Direction(abc.ABC): # Abstract Strategy

	@abc.abstractmethod
	def direct(self, data):
		pass


class Right(Direction): # Concrete Strategy
	def direct(self, data):
		print(data[::-1])


class Left(Direction): # Concrete Strategy
	def direct(self, data):
		print(data[::1])


c = Read('Hello world')
c.set_direction(Right())
c.read()

c.set_direction(Left())
c.read()

