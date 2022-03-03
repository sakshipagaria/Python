# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 01:51:15 2022

@author: ADMIN
"""
import string
dict={}
data=""
file=open("op_file.txt","w")
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
    
print(dict)
with open("ip_file.txt") as cr:
    while True:
        c=cr.read(1)
        if not c:
            print("End of file")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        file.write(data)
        print(data)
        
file.close()