from twisted.internet.protocol import Protocol,ServerFactory
from twisted.internet import reactor
from busdata import bus_data
import numpy as np
pdtype =np.dtype([('bus_id','<i4'),('pd','<f4'),('qd','<f4')],align=True)
class SmartMeter_protocol(Protocol):
    def __init__(self):
        global bus_data
    def dataReceived(self, data):
        if len(data) == 12:
            a = np.frombuffer(data,dtype=pdtype)
            if a['bus_id'] == bus_data['bus_id']:
                bus_data['pd'] = a['pd']
                bus_data['qd'] = a['qd']
                print 'smart',bus_data
    def connectionMade(self):
        pass
class SmartMeter_Factory(ServerFactory):
    protocol = SmartMeter_protocol
