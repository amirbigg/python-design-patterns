"""
	Mediator
	- a behavioral design pattern that lets you reduce chaotic dependencies between objects.
	The pattern restricts direct communications between the objects and forces them to collaborate
	only via a mediator object.
"""
import abc


class AbstractMediator(abc.ABC):

	@abc.abstractmethod
	def notify(self, sender, event):
		pass


class ConcreteMediator(AbstractMediator):
	def __init__(self, comp_a, comp_b):
		self.comp_a = comp_a
		self.comp_a.set_mediator(self)
		self.comp_b = comp_b
		self.comp_b.set_mediator(self)

	def notify(self, sender, event):
		self.comp_b.receive(sender, event)


class AbstractComponent(abc.ABC):
	def __init__(self, mediator = None):
		self._mediator = mediator

	def set_mediator(self, mediator):
		self._mediator = mediator

	@abc.abstractmethod
	def receive(self, sender, event):
		pass

	@abc.abstractmethod
	def notify(self, event):
		pass


class Component1(AbstractComponent):
	def receive(self, sender, event):
		print(f'Component 1 received event ({sender.__class__.__name__} {event})')

	def notify(self, event):
		self._mediator.notify(self, event)

	def do_a(self):
		print('Component 1 does A.')
		self.notify('A')


class Component2(AbstractComponent):
	def receive(self, sender, event):
		print(f'Component 2 received event ({sender.__class__.__name__} {event})')

	def notify(self, event):
		self._mediator.notify(self, event)

	def do_b(self):
		print('Component 2 does B.')
		self.notify('B')


class Component3(AbstractComponent):
	def receive(self, sender, event):
		print(f'Component 3 received event ({sender.__class__.__name__} {event})')

	def notify(self, event):
		self._mediator.notify(self, event)

	def do_c(self):
		print('Component 3 does C.')
		self.notify('C')


c1 = Component1()
c2 = Component2()
c3 = Component3()

mediator = ConcreteMediator(c1, c2)

c1.do_a()
