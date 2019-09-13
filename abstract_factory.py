"""
	Abstract Factory
		Car => Benz, Bmw => Suv, Coupe
			benz suv => gla, glc
			bmw suv => x1, x2

			benz coupe => cls, E-class
			bmw coupe => m2, m4
"""
from abc import ABC, abstractmethod


class Car(ABC):
	@abstractmethod
	def call_suv(self):
		pass

	@abstractmethod
	def call_coupe(self):
		pass
# ----------------------------------------------------
class Benz(Car):
	def call_suv(self):
		return Gla()

	def call_coupe(self):
		return Cls()
# ----------------------------------------------------
class Bmw(Car):
	def call_suv(self):
		return X1()

	def call_coupe(self):
		return M2()
# ----------------------------------------------------
class Suv(ABC):
	@abstractmethod
	def creating_suv(self):
		pass

class Coupe(ABC):
	@abstractmethod
	def creating_coupe(self):
		pass
# ----------------------------------------------------
class Gla(Suv):
	def creating_suv(self):
		print('This is your suv benz gla...')

class X1(Suv):
	def creating_suv(self):
		print('This is your suv bmw x1...')
# ----------------------------------------------------
class Cls(Coupe):
	def creating_coupe(self):
		print('This is your coupe benz cls...')

class M2(Coupe):
	def creating_coupe(self):
		print('This is your coupe bmw m2...')
# ----------------------------------------------------
def clientSuv(order):
	suv = order.call_suv()
	suv.creating_suv()

def clientCoupe(order):
	coupe = order.call_coupe()
	coupe.creating_coupe()
# ----------------------------------------------------



clientCoupe(Bmw())