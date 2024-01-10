"""
	Abstract Factory
	- Abstract Factory Pattern serves to provide an interface for creating related/dependent
	 objects without need to specify their actual class.

	 Car => Benz, Bmw => Suv, Coupe
			benz suv => gla
			bmw suv => x1
			benz coupe => cls
			bmw coupe => m2
"""
from abc import ABC, abstractmethod


class Car(ABC): # Abstract Factory
	@abstractmethod
	def call_suv(self):
		pass

	@abstractmethod
	def call_coupe(self):
		pass


class Benz(Car): # Concrete Factory1
	def call_suv(self):
		return Gla()

	def call_coupe(self):
		return Cls()


class Bmw(Car): # Concrete Factory2
	def call_suv(self):
		return X1()

	def call_coupe(self):
		return M2()


class Suv(ABC): # Abstract Product A
	@abstractmethod
	def create_suv(self):
		pass


class Coupe(ABC): # Abstract Product B
	@abstractmethod
	def create_coupe(self):
		pass


class Gla(Suv): # Concrete Product A1
	def create_suv(self):
		print('This is your suv benz gla...')


class X1(Suv): # Concrete Product A2
	def create_suv(self):
		print('This is your suv bmw x1...')


class Cls(Coupe): # Concrete Product B1
	def create_coupe(self):
		print('This is your coupe benz cls...')


class M2(Coupe): # Concrete Product B2
	def create_coupe(self):
		print('This is your coupe bmw m2...')


def client_suv(order): # Client
	brands = {
		'benz': Benz,
		'bmw': Bmw
	}
	suv = brands[order]().call_suv()
	suv.create_suv()

def client_coupe(order): # Client
	brands = {
		'benz': Benz,
		'bmw': Bmw
	}
	coupe = brands[order]().call_coupe()
	coupe.create_coupe()


client_coupe('benz')
