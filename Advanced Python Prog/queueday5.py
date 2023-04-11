#max size:10
import time
myqueue=[]    #empty stack ,push elements
size=int(input("Enter the size of the queue: "))
if size>10:
    print("Queue size invalid")
else:
    for i in range (size):
        ele=int(input("Add element to the queue: "))
        myqueue.append(ele)
    else:
        print("Queue is full")
        print(myqueue)
    
    print("Start the pop operation: ")
    for i in range(size):
        time.sleep(3)
        print(myqueue.pop(0),"Remove the element from the queue")
    else:
        print("Queue is empty")
        print(myqueue)