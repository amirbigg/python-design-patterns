"""
	State
	- a behavioral design pattern that lets an object alter its behavior when its internal state changes.
	It appears as if the object changed its class.
"""
import abc


class Elevator: # Context
	_state = None

	def __init__(self, state):
		self.set_state(state)

	def set_state(self, state):
		self._state = state
		self._state.set_elevator(self)

	def show_state(self):
		print(f'Elevator is in {self._state.__class__.__name__}')

	def go_up(self):
		self._state.push_up_btn()

	def go_down(self):
		self._state.push_down_btn()



class Floor(abc.ABC): # Abstract State
	_elevator = None

	def set_elevator(self, elevator):
		self._elevator = elevator

	@abc.abstractmethod
	def push_down_btn(self):
		pass

	@abc.abstractmethod
	def push_up_btn(self):
		pass


class FirstFloor(Floor): # Concrete State
	def push_down_btn(self):
		print('Already in the bottom floor')

	def push_up_btn(self):
		print('Elevator moving upward one floor')
		self._elevator.set_state(SecondFloor())


class SecondFloor(Floor): # Concrete State
	def push_down_btn(self):
		print('Elevator moving down a floor')
		self._elevator.set_state(FirstFloor())

	def push_up_btn(self):
		print('Already in the top floor')


e = Elevator(FirstFloor())
e.show_state()
e.go_up()
e.show_state()
e.go_up()
e.go_down()
e.show_state()
e.go_down()
