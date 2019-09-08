"""
	Creational:
		Factory method:
			3 Component => 1.Creator, 2.Product, 3.Client
"""
from abc import ABC, abstractmethod


class Creator(ABC):
	@abstractmethod
	def make(self):
		pass

	def call_edit(self):
		product = self.make()
		result = product.edit()
		return result

class JsonCreator(Creator):
	def make(self):
		return Json()

class XmlCreator(Creator):
	def make(self):
		return Xml()

class PdfCreator(Creator):
	def make(self):
		return Pdf()
# ---------------------------------------
class Product(ABC):
	@abstractmethod
	def edit(self):
		pass

class Json(Product):
	def edit(self):
		return 'Editing Json File...'

class Xml(Product):
	def edit(self):
		return 'Editing Xml File...'

class Pdf(Product):
	def edit(self):
		return 'Editing Pdf File...'
# ---------------------------------------
def client(format):
	return format.call_edit()


print(client(PdfCreator()))