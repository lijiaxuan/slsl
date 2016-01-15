from twisted.internet.protocol import Protocol,ServerFactory
from twisted.internet import reactor
from busdata import bus_data,bustype,bus_ip
from smart_meter_server import SmartMeter_Factory
from actuator_server import Actuator_Factory
from sensor_server import Sensor_Factory
import struct
import numpy as np
import os

BASEPORT = bus_ip[bus_data[0]['bus_id'] - 1][1]

pid = open('pid','w')
pid.write(str(os.getpid()))
pid.close()

class Bus_protocol(Protocol):
    def dataReceived(self, data):
        global bus_data
        if data == 'ASK':
            self.transport.write(bus_data.tobytes())
        elif len(data) == 96:
            if bus_data['status'] == 1:
                bus_data = np.frombuffer(data,dtype=bustype)
                f = open('data','a+')
                f.write(str(bus_data) + '\r\n')
                f.close()
    def connectionMade(self):
        pass
class Bus_Factory(ServerFactory):
    protocol = Bus_protocol
reactor.listenTCP(BASEPORT,Bus_Factory())
reactor.listenTCP(BASEPORT + 1,SmartMeter_Factory())
reactor.listenTCP(BASEPORT + 2,Sensor_Factory())
reactor.listenTCP(BASEPORT + 3,Actuator_Factory())
reactor.run()
#print len(bus_data.tobytes())