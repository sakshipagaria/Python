# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 14:24:19 2022

@author: ADMIN
"""

import string
def test(word):
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    new=''
    
    
    for ch in word:
        if (ch in lower):
            index=lower.index(ch)
            new=new+lower[(index+2)%26]
            
        elif(ch in upper):
            index=upper.index(ch)
            new=new+upper[(index+3)%26]
            
        else:
            new=new+ch
            
    return new
print(test(input()))
