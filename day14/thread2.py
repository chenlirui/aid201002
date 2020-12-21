"""

"""

from threading import Thread
from time import sleep
def fun(sec,name):
    print("")
    sleep(sec)
    print()
for i in range(5):
    t = Thread(target=fun,args=(2,),kwargs={"name":"T "})


