# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 18:19:39 2022

@author: ADMIN
"""
def linear_search(n,x):
    element=[]
    for i in range(1,1001):
        element.append(i)
        
        
    count=0
    flag=0
    for i in element:
        count+=1
        if (i==x):
            print("Yes,i found ny no. at position:" +str(i))
            flag=1
            break
            
    if (flag==0):
        print("Number is not found")
    print("Number of iteration: "+str(count))
    
def binary_search(a,x):
    first_pos=0
    last_pos=len(a)-1
    flag=0                         #flag is element has not been found
    
    count=0
    
    while(first_pos<=last_pos and flag==0):
        count+=1
        mid=(first_pos+last_pos)//2
        if(x==a[mid]):
            flag=1
            print("Element present at position:" +str(mid+1))        #+1 for excat posiiton and if only mid then it is coz array starts with 0
            print("Number of iteration are:" +str(count))
            return
        else:
            if(x<a[mid]):
                last_pos=mid-1                    #first half
            else:
                first_pos=mid+1                   #second half\
                    
    print("Number NOT present")
    
a=[]
for i in range(1,101):
    a.append(i)
    
binary_search(a,33)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                