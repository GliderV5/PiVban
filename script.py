from pyVBAN import *

cl = VBAN_Recv("127.0.0.1","Stream1",6980,8,verbose=True)
cl.runforever()