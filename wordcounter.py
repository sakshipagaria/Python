# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 20:01:33 2022

@author: pagar
"""

f=open("fileforcounter.txt","r")
c=[]
for x in f:
    print(x)
    c.append(x.split(" "))
print(c)          #c is list of words in the file

#d=0       #d is the counter
res=len(x.split(" "))
for i in range(len(c)):
    #d=d+1
 print(res)