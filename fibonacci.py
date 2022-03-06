# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 14:41:26 2022

@author: ADMIN
"""

#n=(n-1)+(n-2)

def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
n=int(input("Enter the non-negative value for n:"))
if n<0:
    print("Fibonacci numbers are undefined for neagtive numbers ")
else:
    print("Fibonnaci number at position",n,"is ",fibonacci(n) )