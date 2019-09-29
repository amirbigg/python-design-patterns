"""
	Proxy
"""

class Db:
	def work(self):
		print('you are admin so you can work with database...')

class Proxy:
	admin_password = 'secret'
	def check_admin(self, password):
		if password == self.admin_password:
			d1 = Db()
			d1.work()
		else:
			print('You are not admin so you cant work with database...')



p1 = Proxy()
p1.check_admin('secret')