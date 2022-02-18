# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 16:00:39 2022

@author: ADMIN
"""

import string
import random
symbols=[]
symbols=list(string.ascii_letters)
card1=[0]*8
card2=[0]*8
pos1=random.randint(0,8)
pos2=random.randint(0,8)
print(pos1)
print(pos2)
#position1 & 2 are same symbol position in card1&2
samesymbol=random.choice(symbols)
if(pos1==pos2):
    card2[pos1]=samesymbol
    card1[pos1]=samesymbol
else:
    card1[pos1]=samesymbol
    card2[pos2]=samesymbol
    card1[pos2]=random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1]=random.choice(symbols)
    symbols.remove(card2[pos1])
    
i=0
while(i<8):
    if(i!=pos1 and i!=pos2):
        alphabet1=random.choice(symbols)
        symbols.remove(alphabet1)
        alphabet2=random.choice(symbols)
        symbols.remove(alphabet2)
        card1[i]=alphabet1
        card2[i]=alphabet2
    i=i+1
print(card1)
print(card2)
        
        
        
