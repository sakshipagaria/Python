# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 14:51:18 2022

@author: ADMIN
"""
#even number of stars

def recursive(num):
    if (num==1):
        print('*')
        return
    if(num%2==0):
        print('*'*num)
        recursive(num-1)
        return
    else:
        recursive(num-1)
        return
    
recursive(10)