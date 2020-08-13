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
		print(f'\t\tCat Leaf {self.name}')

class Dog(World):
	def __init__(self, name):
		self.name = name

	def show(self):
		print(f'\t\tDog Leaf {self.name}')

class Male(World):
	def __init__(self, name):
		self.name = name

	def show(self):
		print(f'\t\tMale Leaf {self.name}')

class Female(World):
	def __init__(self, name):
		self.name = name

	def show(self):
		print(f'\t\tFemale Leaf {self.name}')

cat = Cat('Missy')
dog = Dog('Jack')

male = Male('Mark')
female = Female('Jane')

animal = Animal('animal1')
human = Human('human1')

animal.add(cat)
animal.add(dog)

human.add(male)
human.add(female)

being = Being('all')
being.add(animal)
being.add(human)

being.show()

# Being Composite all
# 	Animal Composite animal
# 		Animal Leaf Missy
# 		Animal Leaf Jack
# 	Human Composite human
# 		Human Leaf Mark
# 		Human Leaf Jane
