"""
	Builder
"""
class Director:
	__builder = None

	def setBuilder(self, builder):
		self.__builder = builder

	def getCar(self):
		car = Car()

		body = self.__builder.getBody()
		car.setBody(body)

		wheel = self.__builder.getWheel()
		car.setWheel(wheel)

		engine = self.__builder.getEngine()
		car.setEngine(engine)
		return car
# ----------------------------------------
class Car:
	def __init__(self):
		self.__wheel = None
		self.__engine = None
		self.__body = None

	def setWheel(self, wheel):
		self.__wheel = wheel

	def setBody(self, body):
		self.__body = body

	def setEngine(self, engine):
		self.__engine = engine

	def detail(self):
		print(f'Body: {self.__body.shape}')
		print(f'Engine: {self.__engine.hp}')
		print(f'Wheel: {self.__wheel.size}')
# ----------------------------------------
class Builder:
	def getEngine(self): pass
	def getWheel(self): pass
	def getBody(self): pass

class Benz(Builder):
	def getBody(self):
		body = Body()
		body.shape = 'Suv'
		return body

	def getEngine(self):
		engine = Engine()
		engine.hp = 500
		return engine

	def getWheel(self):
		wheel = Wheel()
		wheel.size = 22
		return wheel

class Bmw(Builder):
	def getBody(self):
		body = Body()
		body.shape = 'Sedan'
		return body

	def getEngine(self):
		engine = Engine()
		engine.hp = 340
		return engine

	def getWheel(self):
		wheel = Wheel()
		wheel.size = 18
		return wheel
# ----------------------------------------
class Wheel: size = None
class Body:	shape = None
class Engine: hp = None
# ----------------------------------------


car1 = Bmw()
director = Director()
director.setBuilder(car1)
b1 = director.getCar()
b1.detail()