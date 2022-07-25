# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 14:48:10 2022

@author: pagar
"""

import random
cards=['Clubs','Daimonds','Hearts','Spades']
ranks=[2,3,4,5,6,7,8,9,10,'Jack','King','Queen','Ace']

def pick_a_card_R():
    card=random.choices(cards)
    rank=random.choices(ranks)
    return(f"The {rank} of {card}")

print(pick_a_card_R())