"""
	Iterator => 1.Iterable, 2.Iteration
		__iter__, __next__
"""

class Iteration:
	def __init__(self, value):
		self.value = value

	def __next__(self):
		if self.value == 0:
			raise StopIteration('End of sequence...')
		for i in range(0, self.value):
			value = self.value
			self.value -= 1
			return value

class Iterable:
	def __init__(self, value):
		self.value = value

	def __iter__(self):
		return Iteration(self.value)

f1 = Iterable(9)
f2 = iter(f1)


print(next(f2))
print(next(f2))
print(next(f2))
print(next(f2))
print(next(f2))
print(next(f2))
print(next(f2))
print(next(f2))
print(next(f2))
print(next(f2))