"""
线程基础示例
"""
from threading import Thread
from time import sleep
import os
def  music():

    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放:黄河大合唱")
t = threading.Thread(target=music)
t.start()
for i in range(4):
    sleep(1)
    print(os.getpid(),"播放:葫芦娃")
t.jion()
