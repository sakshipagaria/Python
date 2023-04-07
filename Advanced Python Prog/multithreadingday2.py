from threading import *
import time
def add(num):
    for n in num :
        time.sleep(1)
        print("Add=",2*n)
        print()
def mult(num):
    for n in num :
        time.sleep(1)
        print("Mult=",n*n)
        print()
def sub(num):
    for n in num :
        time.sleep(1)
        print("Sub=",n-n)
        print()
num=[2,3,4,5,8]
starttime=time.time()
#creating thread using no class
t1=Thread(target=add,args=(num,))
t2=Thread(target=mult,args=(num,))
t3=Thread(target=sub,args=(num,))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("The total time:",time.time()-starttime)

#----------------------------------

#ident-thread identification number

from threading import *
def show():
    print("Child thread\n")
child =Thread(target=show())
child.start()

print("Main thread ID",current_thread().ident)
print("Child thread ID",child.ident)