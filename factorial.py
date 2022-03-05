# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 17:12:26 2022

@author: ADMIN
"""

def factorial(n):
    prod=1
    for i in range(1,n+1):
        prod=prod *i
    return prod

n=int(input("Enter positive number:"))
if n<0:
    print("Factorial is not defined on negative number")
else:
    f=factorial(n)
    print("Factorial of ",n,'is',f)