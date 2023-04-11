#validation logic
import re
mob=input("Enter mob number: ")
obj=re.fullmatch("[0-9]\d{9}",mob)
if obj!=None:
    print("Valid")
else:
    print("InValid")

#--------------------------
#wap to accept a pw and if pw containupper case small case digit and special then print(pw is strong) else (pw is weak)

import re
password=input("Enter your password: ")
obj=re.fullmatch("[a-zA-Z0-9]\w{1,8}",password)
if obj!=None:
    print("Strong password")
else:
    print("Weak password")

#-----------------------
#encrypted password
import re
obj=re.sub('[a-zA-Z0-9]','*','cash63vg45')
print(obj)