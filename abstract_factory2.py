"""
	Abstract Factory:
		Car => 1.benz, 2.bmw  => 1.suv, 2.coupe
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
# ----------------------------------------------------------
class Benz(Car):
	@staticmethod
	def call_suv(model):
		return model

	@staticmethod
	def call_coupe(model):
		return model

class Bmw(Car):
	@staticmethod
	def call_suv(model):
		return model

	@staticmethod
	def call_coupe(model):
		return model
# ----------------------------------------------------------
class Suv(ABC):
	@abstractmethod
	def creating_suv(self):
		pass

class Coupe(ABC):
	@abstractmethod
	def creating_coupe(self):
		pass
# ----------------------------------------------------------
class Gla(Suv):
	def creating_suv(self):
		print('This is your suv Benz Gla...')

class Glc(Suv):
	def creating_suv(self):
		print('This is your suv Benz Glc...')

class X1(Suv):
	def creating_suv(self):
		print('This is your suv Bmw X1...')

class X2(Suv):
	def creating_suv(self):
		print('This is your suv Bmw X2...')
# ----------------------------------------------------------
class Cls(Coupe):
	def creating_coupe(self):
		print('This is your coupe Benz Cls...')

class Eclass(Coupe):
	def creating_coupe(self):
		print('This is your coupe Benz E-class...')

class M2(Coupe):
	def creating_coupe(self):
		print('This is your coupe Bmw M2...')

class M4(Coupe):
	def creating_coupe(self):
		print('This is your coupe Bmw M4...')
# ----------------------------------------------------------
def OrderSuv(corp, model):
	suv = corp().call_suv(model())
	suv.creating_suv()

def OrderCoupe(corp, model):
	coupe = corp().call_coupe(model())
	coupe.creating_coupe()

try:
	OrderCoupe(Bmw, M2)
except:
	print('Sorry, we dont have this model....')

try:
	OrderSuv(Bmw, M2)
except:
	print('Sorry, we dont have this model....')