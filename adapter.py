"""
	Adapter
	- a structural design pattern that allows objects with incompatible interfaces to collaborate.
"""
import xmltodict


class Application:
	def send_request(self):
		return 'data.xml'


class Analytic:
	def receive_request(self, json):
		return json


class Adapter:
	def convert_xml_json(self, file):
		with open(file, 'r') as myfile:
			obj = xmltodict.parse(myfile.read())
			return obj


def client_adapter():
	sender = Application().send_request()
	converted_data = Adapter().convert_xml_json(sender)
	receiver = Analytic().receive_request(converted_data)
	print(receiver)


client_adapter()
