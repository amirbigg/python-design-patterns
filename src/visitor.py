"""
	Visitor
	- a behavioral design pattern that allows adding new behaviors to existing class hierarchy
	without altering any existing code.
"""
import abc


class PublicVehicle(abc.ABC): # Abstract Element
	def __init__(self, dest):
		self.dest = dest

	@abc.abstractmethod
	def order_ticket(self, ordering):
		pass


class Train(PublicVehicle): # Concrete Element
	def order_ticket(self, ordering):
		ordering.train_ticket(self)


class Bus(PublicVehicle): # Concrete Element
	def order_ticket(self, ordering):
		ordering.bus_ticket(self)


class Plane(PublicVehicle): # Concrete Element
	def order_ticket(self, ordering):
		ordering.plane_ticket(self)


class Ticket(abc.ABC): # Abstract Visitor

	@abc.abstractmethod
	def train_ticket(self, train):
		pass

	@abc.abstractmethod
	def bus_ticket(self, bus):
		pass

	@abc.abstractmethod
	def plane_ticket(self, plane):
		pass


class Order(Ticket): # Concrete Visitor
	def train_ticket(self, train):
		print(f'This is a train ticket to {train.dest}')

	def bus_ticket(self, bus):
		print(f'This is a bus ticket to {bus.dest}')

	def plane_ticket(self, plane):
		print(f'This is a plane ticket to {plane.dest}')


o = Order()
Train('Tehran').order_ticket(o)
