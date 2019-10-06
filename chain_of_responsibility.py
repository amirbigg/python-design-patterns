"""
	Behavioral
		Chain Of Responsibility
"""
from abc import ABC, abstractmethod


class AbstractHandler(ABC):
	def __init__(self, successor):
		self._successor = successor

	def handle(self, request):
		handled = self.processRequest(request)
		if not handled:
			self._successor.handle(request)

	@abstractmethod
	def processRequest(self, request):
		pass
# -----------------------------------------------------------------
class HandlerOne(AbstractHandler):
	def processRequest(self, request):
		if 0 < request <= 10:
			print(f'Handler One is processing this request... {request}')
			return True

class HandlerTwo(AbstractHandler):
	def processRequest(self, request):
		if 10 < request <= 20:
			print(f'Handler Two is processing this request... {request}')
			return True

class DefaultHandler(AbstractHandler):
	def processRequest(self, request):
		print(f'This request has no handler so default handler is processing this request... {request}')
		return True
# -----------------------------------------------------------------
class Client:
	def __init__(self):
		self.handler = HandlerOne(HandlerTwo(DefaultHandler(None)))

	def delegate(self, requests):
		for request in requests:
			self.handler.handle(request)

request = [3, 14, 34, 9]

c1 = Client()
c1.delegate(request)