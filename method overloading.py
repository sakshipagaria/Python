#method overloading
#it is not possible in python
#diff no. arguments then python will always consider only last method

class Arithmatic:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)

obj=Arithmatic()
obj.add(28)
obj.add(28,29)
obj.add(28,29,30)