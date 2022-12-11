"""
	Singleton
		- Ensure a class only has one instance, and provide a global point of access to it.
"""

class Singleton(type):
	_instance = None

	def __call__(self, *args, **kwargs):
		if self._instance is None:
			self._instance = super().__call__()
		return self._instance


class A(metaclass=Singleton):
	pass


one = A()
two = A()

print(id(one))
print(id(two))
