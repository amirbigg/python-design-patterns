from abc import ABC, abstractmethod

class World(ABC):
	@abstractmethod
	def show(self): pass

class Being(World):
	def __init__(self, name):
		self.name = name
		self.children = []

	def add(self, object):
		self.children.append(object)

	def remove(self, object):
		self.children.remove(object)

	def show(self):
		print(f'Being Composite {self.name}')
		for child in self.children:
			child.show()

class Animal(World):
	def __init__(self, name):
		self.name = name
		self.children = []

	def add(self, object):
		self.children.append(object)

	def remove(self, object):
		self.children.remove(object)

	def show(self):
		print(f'\tAnimal Composite {self.name}')
		for child in self.children:
			child.show()

class Human(World):
	def __init__(self, name):
		self.name = name
		self.children = []

	def add(self, object):
		self.children.append(object)

	def remove(self, object):
		self.children.remove(object)

	def show(self):
		print(f'\tHuman Composite {self.name}')
		for child in self.children:
			child.show()

class Cat(World):
	def __init__(self, name):
		self.name = name

	def show(self):
		print(f'\t\tAnimal Leaf {self.name}')

class Dog(World):
	def __init__(self, name):
		self.name = name

	def show(self):
		print(f'\t\tAnimal Leaf {self.name}')

class Male(World):
	def __init__(self, name):
		self.name = name

	def show(self):
		print(f'\t\tHuman Leaf {self.name}')

class Female(World):
	def __init__(self, name):
		self.name = name

	def show(self):
		print(f'\t\tHuman Leaf {self.name}')

cat1 = Cat('Missy')
dog1 = Dog('Jack')

male1 = Male('Mark')
female1 = Female('Jane')

animal1 = Animal('animal1')
human1 = Human('human1')

animal1.add(cat1)
animal1.add(dog1)

human1.add(male1)
human1.add(female1)

being1 = Being('all')
being1.add(animal1)
being1.add(human1)

being1.show()

# Being Composite all
# 	Animal Composite animal1
# 		Animal Leaf Missy
# 		Animal Leaf Jack
# 	Human Composite human1
# 		Human Leaf Mark
# 		Human Leaf Jane