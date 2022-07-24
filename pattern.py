# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 21:14:49 2022

@author: pagar
"""

def pyramid_pattern(n):                #n is no of rows
    a = 2*n-2             #space
    for i in range(0, n):
        for j in range(0, a):
            print(end=" ")
        a = a-1              #n=a-1 for rightsided pyramid & a=a-2 leftsided pyramid 
        for j in range(0, i+1):                #i+1-top of pyramid is 1*
            print("*", end=" ")
        print("\r")
print(pyramid_pattern(5))