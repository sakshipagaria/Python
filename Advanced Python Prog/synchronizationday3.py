# #Without Synchronization

from threading import*
import time
def conferenceCall(myname):
    print("Halo,Ich bin ")
    time.sleep(1)
    print(myname)
obj1 =Thread(target=conferenceCall,args=("Sakshi",))
obj2 =Thread(target=conferenceCall,args=("Chai",))
#here 2 objs are going to access same method at sam etime
obj1.start()
obj2.start()

#----------------------------------
#with synchronization 
#1)LOCK

from threading import *
import time
l=Lock() #lock obj created
def come_in(name):
    l.acquire()
    for i in range(2):
        print(name)
        print("Ja herr ",end="")
        time.sleep(1)

    l.release()
obj1=Thread(target=come_in,args=("Sakshi",))
obj2=Thread(target=come_in,args=("Chai",))
obj1.start()
obj2.start()

#------------------------------------
#problem in thread block

from threading import *
obj=Lock()
print("Lock acquired for the first time")
obj.acquire()
print("lock acquired second time")
obj.acquire()

#----------------------------------
#Rlock

from threading import *
obj=RLock()
print("Lock acquired for the first time")
obj.acquire()
print("lock acquired second time")
obj.acquire()

#---------------------------------------------
#semaphore

from threading import *
import time
l=Semaphore(4)
def come_in(name):
    l.acquire()
    for i in range(5):
        print("Ja herr: ",name)
        time.sleep(1)
    l.release()
obj1=Thread(target=come_in,args=("Aarish",))
obj2=Thread(target=come_in,args=("Murtasim",))
obj3=Thread(target=come_in,args=("Merrab",))
obj4=Thread(target=come_in,args=("Sasha",))
obj1.start()
obj2.start()
obj3.start()
obj4.start()
