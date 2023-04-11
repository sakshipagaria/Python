import time
mystack=[]    #empty stack ,push elements
size=int(input("Enter the size of the array: "))
if size>10:
    print("Stack size invalid")
else:
    for i in range (size):
        ele=int(input("Push element into the stack: "))
        mystack.append(ele)
    else:
        print("Stack is full")
        print(mystack)

    print("Start the pop operation: ")
    for i in range(size):
        time.sleep(3)
        print(mystack.pop(),"Pop the element from the stack")
    else:
        print("Stack is empty")
        print(mystack)