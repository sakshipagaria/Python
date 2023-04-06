#thread creation w/o using any class

import threading
import time
def activate():
    #user defined fn
    for i in range (1,11):
        time.sleep(2)
        print("THIS IS CHILD THREAD\n")
t=threading.Thread(target=activate)    #creating thread object
t.start()      #starting of there

for i in range(1,11):
    time.sleep(2)
    print("THIS IS:",threading.current_thread().getName())
    
#thread creation by extending thread  class

from threading import *
import time
class MyThread(Thread):
    #child class
    def run(self):
        for i in range(10):
            time.sleep(2)
            print("Child thread-1")
obj_t=MyThread()
obj_t.start()
for i in range(10):
    time.sleep(2)
    print("Main Thread-1")
    
    
