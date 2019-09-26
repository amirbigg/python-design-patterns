"""
    Structural
        Adapter => 1.Adaptee, 2.Adapter, 3.Client
"""

class IranSocket:
    _type = '2'

class Adapter:
    _socket = None
    _pinType = '3To2'

    def __init__(self, socket):
        self._socket = socket

class Fridge:
    _adapter = None
    _pinType = '3'

    def __init__(self, adapter):
        self._adapter = adapter

    def freeze(self):
        if self._adapter._pinType == (self._pinType + 'To' + self._adapter._socket._type):
            print('Done...')
        else:
            print('Sorry, Not Usable...')

i = IranSocket()
adapter = Adapter(i)
f = Fridge(adapter)
f.freeze()