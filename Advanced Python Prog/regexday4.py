
#-------------------------------------
#input value taken from user at runtime 

import re
obj=input("Enter any character: ")
objmatch=re.finditer(obj,"how much wood could a woodchuck chuck if a wood chuck could chuck wood")
print(objmatch)
for i in objmatch:
    print(i.start(),"-",i.end()," ",i.group())

#---------------------------------------
#match pointer

import re
a=input("Enter string to perform match operation:")
mtch=re.match(a,"Ich bin Sakshi und ich mag trinke kaffee")
print(mtch)
if mtch!=None:
    print("Match found at begining level")
    print(mtch.start()," ",mtch.end())
else:
    print("There is no match at begining level")
