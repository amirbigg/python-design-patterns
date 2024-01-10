"""
	Facade
	- a structural design pattern that provides a simplified interface to a library,
	a framework, or any other complex set of classes.
"""

class CPU: # Subsystem 1
	def execute(self):
		print('Executing')


class Memory: # Subsystem 2
	def load(self):
		print('Loading data.')


class SSD: # Subsystem 3
	def read(self):
		print('Some data from ssd')


class Computer: # Facade
	def __init__(self, sub1, sub2):
		self.cpu = sub1()
		self.memory = sub2()

	def start(self):
		self.memory.load()
		self.cpu.execute()


def client_facade():
	computer_facade = Computer(CPU, Memory)
	computer_facade.start()


client_facade()
