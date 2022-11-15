class Mobile:
    #constructor
    def __init__(self,ram,price,processor):
        #self is a parameter refer to obj

        #attributes
        self.__ram=ram        #public changes to private
        self.__processor=processor   #protected changed to private
        self.__price=price      #private

    def __str__(self):
        return f'Ram: {self.__ram}\nProcessor:{self.__processor}\nPrice:{self.__price}'
			
		#getters
    def get_ram(self):
        return self.__ram 
    def get_processor(self):
        return self.__processor
    def get_price(self):
        return self.__price
       
m1=Mobile('16gb','8gen1',90000)
m2=Mobile('12gb','865+',70000)
m3=Mobile('8gb','855',45000)

print(m1)
print(m2)
print(m3)

---------------output-------------
Ram: 16gb
Processor:90000
Price:8gen1
Ram: 12gb
Processor:70000
Price:865+
Ram: 8gb
Processor:45000
Price:855
	
--------------------------------------------------------------------------------------------------------------------------------------------
class Mobile:
    #constructor
    def __init__(self,ram,price,processor):
        #self is a parameter refer to obj

        #attributes
        self._ram=ram        #public changes to private changes to protected
        self._processor=processor   #protected changed to private changes to protected
        self._price=price      #private changes to protected

    def __str__(self):
        return f'Ram: {self._ram}\nProcessor:{self._processor}\nPrice:{self._price}'
        
    #setters
    def set_ram(self):
        return self._ram 
    def set_processor(self):
        return self._processor
    def set_price(self):
        return self._price
 
m1=Mobile('16gb','8gen1',90000)
m2=Mobile('12gb','865+',70000)
m3=Mobile('8gb','855',45000)

print(m1)
print(m2)
print(m3)
print(m1.get_price)

-------------output------------
Ram: 16gb
Processor:90000
Price:8gen1
Ram: 12gb
Processor:70000
Price:865+
Ram: 8gb
Processor:45000
Price:855
