"""
	Decorator
	- a structural pattern that allows adding new behaviors to objects dynamically
	by placing them inside special wrapper objects, called decorators.
"""
import abc


class Page(abc.ABC): # Abstract Component

	@abc.abstractmethod
	def show(self):
		pass


class AuthPage(Page): # Concrete Component 1
	def show(self):
		print('Welcome to authenticated page')


class AnonPage(Page): # Concrete Component 2
	def show(self):
		print('Welcome to anonymous page')



class PageDecorator(Page, abc.ABC): # Abstract Decorator
	def __init__(self, component):
		self._component = component

	@abc.abstractmethod
	def show(self):
		pass


class PageAuthDecorator(PageDecorator): # Concrete Decorator
	def show(self):
		username = input('Enter your username... ')
		password = input('Enter your password... ')
		if username == 'admin' and password == 'secret':
			self._component.show()
		else:
			print('you are not authenticated')


def client_decorator():
	page = AuthPage()
	authenticated = PageAuthDecorator(page)
	authenticated.show()

client_decorator()
