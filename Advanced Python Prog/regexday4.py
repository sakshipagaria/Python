#regular expression using compile function
import re
count=0 
pattern=re.compile("wood")
print(pattern)
matcher=pattern.finditer("how much wood could a woodchuck chuck if a wood chuck could chuck wood")
print(matcher)
for i in matcher:
    count+=1
    print(i.start(),"",i.end(),"",i.group())
print("The number of occurences:",count)

#---------------------------------------------
#without complie function
import re
count=0
matcher=re.finditer("wood", "how much wood could a woodchuck chuck if a wood chuck could chuck wood")
for i in matcher: #loop executes four times
    count+=1
    print(i.start(),"",i.end(),"",i.group())
print("The number of occurences:",count)

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

#-----------------------------------------------------
#example
import re
count=0
with open('filehandling.txt','r') as f:
    data=f.readline()
pattern=re.compile("chuck")
matcher=pattern.finditer(data)
for i in matcher:
    count+=1
print("The number of occurences:",count)

#---------------------------------------------
#---------------------------------------------
# #fulll match function
import re
a=input("Enter string to perform match operation: ")
mtch=re.fullmatch(a,"python is very")
print(mtch)
if mtch!=None:
    print("Match found at the begining level")
    print(mtch.start()," ",mtch.end())
else:
    print("There is no match at the begining level")

#--------------------------------------------------
# #search fucntion
import re
a=input("Enter string to perform match operation: ")
mtch=re.search(a,"sakshiiscrazy")
print(mtch)
if mtch!=None:
    print(mtch.start()," ",mtch.end())
else:
    print("There is no match at the begining level")

#-----------------------------------------------
#find all fucntion

import re
mtch=re.findall('[0-5]',"sdgwed735egfd3")
print(mtch)
