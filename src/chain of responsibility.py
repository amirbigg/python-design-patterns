"""
	Chain of Responsibility
	- a behavioral design pattern that lets you pass requests along a chain of handlers.
	Upon receiving a request, each handler decides either to process the request or to pass
	it to the next handler in the chain.
"""
import abc


class AbstractHandler(abc.ABC):
	@abc.abstractmethod
	def set_next(self, handler):
		pass

	@abc.abstractmethod
	def handle(self, request):
		pass


class BaseHandler(AbstractHandler):
	_next_handler = None

	def set_next(self, handler):
		self._next_handler = handler
		return handler

	@abc.abstractmethod
	def handle(self, request):
		if self._next_handler:
			return self._next_handler.handle(request)
		return None


class HandlerOne(BaseHandler):
	def handle(self, request):
		if 0 <= request <= 10:
			print(f'HandlerOne is processing this request {request}')
		else:
			return super().handle(request)


class HandlerTwo(BaseHandler):
	def handle(self, request):
		if 10 < request <= 20:
			print(f'HandlerTwo is processing this request {request}')
		else:
			return super().handle(request)


class DefaultHandler(BaseHandler):
	def handle(self, request):
		print(f'DefaultHandler is processing this request {request}')


def client(handler, request):
	for num in request:
		handler.handle(num)


nums = [3, 14, 31, 9]

h_one = HandlerOne()
h_two = HandlerTwo()
h_default = DefaultHandler()

h_one.set_next(h_two).set_next(h_default)

client(h_two, nums)

