# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 22:18:30 2022

@author: pagar
"""

import random
#range of values of dice
min_value = 1            
max_value = 6

#to loop the rolling through yes
roll_again="yes"

#loop
while roll_again=="yes" or roll_again=="y":
     print("Rolling the dices..")
     print("The values are :")
     print(random.randint(min_value, max_value))         #for 1st no
     print(random.randint(min_value, max_value))          #for 2nd no
     roll_again = input("Roll the dices again?")          #asking user to roll the dice again 