from pyVBAN import *

cl = VBAN_Recv("192.168.1.14","Stream1",6980,10,verbose=False)
cl.runforever()