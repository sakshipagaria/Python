#constructor overloading is not possible in python
#if we define multiple constuctors then the last constructor will be considered

class Arithmatic:
    def __init__(self):
        print("There is no argument")
    def __init__(self,a):
        print("Passing an argument")
    def __init__(self,a,b):
        print("Passing two arguments")

obj=Arithmatic()
obj=Arithmatic(10)
obj=Arithmatic(22,32)