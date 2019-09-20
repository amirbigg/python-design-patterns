"""
	Prototype
"""
from copy import deepcopy


class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age


class Prototype:
	def __init__(self):
		self._objects = {}

	def register(self, name, obj):
		self._objects[name] = obj

	def unregister(self, name):
		del self._objects[name]

	def clone(self, name, **kwargs):
		clonedObj = deepcopy(self._objects.get(name))
		clonedObj.__dict__.update(kwargs)
		return clonedObj



p1 = Person('amir', 34)

pro1 = Prototype()
pro1.register('person1', p1)
personCopy = pro1.clone('person1', age=43)


print(personCopy.__dict__)

