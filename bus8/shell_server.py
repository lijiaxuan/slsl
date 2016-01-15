from twisted.internet.protocol import Protocol,ServerFactory
from twisted.internet import reactor
import commands
import os
import subprocess
import busdata
base_path=os.path.dirname(os.path.abspath(__file__))
class shell_protocol(Protocol):
    def dataReceived(self, data):
        if data == '3':
            try:
                p = open(base_path  + '/pid','r')
                pid = p.read(-1)
                p.close()
                id = commands.getoutput('kill '+pid)
                print 'print restart'
                subprocess.Popen('python ' + base_path + '/bus.py',shell=True)
            except:
                subprocess.Popen('python ' + base_path + '/bus.py',shell=True)
                pass
class shell_Factory(ServerFactory):
    protocol = shell_protocol
reactor.listenTCP(50000 + busdata.bus_data[0]['bus_id'],shell_Factory())
reactor.run()