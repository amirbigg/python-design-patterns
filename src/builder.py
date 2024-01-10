"""
	builder
	- Builder is a creational design pattern that lets you construct complex objects step by step.
	The pattern allows you to produce different types and representations of an object using the same
	construction code.
"""
import abc


class Car: # Product
	def __init__(self):
		self._wheel = None
		self._engine = None
		self._body = None

	def set_wheel(self, wheel):
		self._wheel = wheel

	def set_body(self, body):
		self._body = body

	def set_engine(self, engine):
		self._engine = engine

	def detail(self):
		print(f'Body: {self._body.shape}')
		print(f'Engine: {self._engine.hp}')
		print(f'Wheel: {self._wheel.size}')


class AbstractBuilder(abc.ABC): # Abstract Builder

	@abc.abstractmethod
	def get_engine(self): pass

	@abc.abstractmethod
	def get_wheel(self): pass

	@abc.abstractmethod
	def get_body(self): pass


class Benz(AbstractBuilder): # Concrete Builder 1
	def get_body(self):
		body = Body()
		body.shape = 'Suv'
		return body

	def get_engine(self):
		engine = Engine()
		engine.hp = 500
		return engine

	def get_wheel(self):
		wheel = Wheel()
		wheel.size = 22
		return wheel


class Bmw(AbstractBuilder): # Concrete Builder 2
	def get_body(self):
		body = Body()
		body.shape = 'Sedan'
		return body

	def get_engine(self):
		engine = Engine()
		engine.hp = 340
		return engine

	def get_wheel(self):
		wheel = Wheel()
		wheel.size = 20
		return wheel


class Director:
	_builder = None

	def set_builder(self, builder):
		self._builder = builder

	def construct(self):
		car = Car()

		body = self._builder.get_body()
		car.set_body(body)

		wheel = self._builder.get_wheel()
		car.set_wheel(wheel)

		engine = self._builder.get_engine()
		car.set_engine(engine)

		return car


class Wheel: size = None
class Body: shape = None
class Engine: hp = None


def client_builder(builder):
	builders = {
		'bmw': Bmw,
		'benz': Benz
	}

	car = builders[builder]()
	director = Director()
	director.set_builder(car)
	result = director.construct()
	return result.detail()


client_builder('bmw')
