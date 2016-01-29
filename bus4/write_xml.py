import  random
import os
import xml.dom.minidom

base_path=os.path.dirname(os.path.abspath(__file__))
def writexml(data):
    V = random.random() * 2 + data['va']
    I = data['pd'] / V
    DOMTree = xml.dom.minidom.parse(base_path + "/pdata.xml")
    tree = DOMTree.documentElement
    devices = tree.getElementsByTagName("DEVICE_1")
    items = devices[0].getElementsByTagName("item")
    for item in items:
        if item.getAttribute('D_LABEL') == 'Inst Van':
            item.setAttribute('D_VALUE',str(V + random.random() * 2) + 'k')
        elif item.getAttribute('D_LABEL') == 'Inst Vbn':
            item.setAttribute('D_VALUE',str(V + random.random() * 2) + 'k')
        elif item.getAttribute('D_LABEL') == 'Inst Vcn':
            item.setAttribute('D_VALUE',str(V + random.random() * 2) + 'k')
        elif item.getAttribute('D_LABEL') == 'Inst Ia':
            item.setAttribute('D_VALUE',str(I + random.random() * 2))
        elif item.getAttribute('D_LABEL') == 'Inst Ib':
            item.setAttribute('D_VALUE',str(I + random.random() * 2))
        elif item.getAttribute('D_LABEL') == 'Inst Ic':
            item.setAttribute('D_VALUE',str(I + random.random() * 2))
    f = open(base_path + "/pdata_x.xml",'w')
    f.write(DOMTree.toxml())
    f.close()
