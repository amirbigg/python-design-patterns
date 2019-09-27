"""
	Facade
"""
class Raw:
	def raw(self):
		print('Buying raw foods from market...')

class Transfer:
	def transfer(self):
		print('Transfering raw foods to restaurant...')

class Cook:
	def cook(self):
		print('Cooking raw foods by chief...')

class Serve:
	def server(self):
		print('Serving food to client...')


class ItalianRestaurant:
	def get(self):
		r = Raw()
		r.raw()

		t = Transfer()
		t.transfer()

		c = Cook()
		c.cook()

		s = Serve()
		s.server()

def order():
	i = ItalianRestaurant()
	i.get()


order()