"""
	Decorator
		decorator pattern != python decorator
"""
class Article:
	def show(self):
		print('All Articles...')

class Login:
	def check_login(self, name, password):
		if name == 'admin' and password == 'amir':
			return True

def outer_login(func):
	def inner_login():
		name = input('Enter your name...')
		password = input('Enter your password...')
		l = Login()
		result = l.check_login(name, password)
		if result:
			func()
		else:
			print('Wrong username or password')
	return inner_login


@outer_login
def show_all_articles():
	a = Article()
	a.show()


show_all_articles()