# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 22:16:33 2022

@author: ADMIN
"""
import random

doors=[0]*3
goatdoor=[0]*2
swap=0                 #no. swap wins
dont_swap=0             #no. of dont swap wins
j=0
while(j<10):
    x=random.randint(0,2)    #xth door comprise of BMW
    doors[x]="BMW"
    for i in range(0,3):
        if (i==x):
            continue
        else:
            doors[i]="Goat"
            goatdoor.append(i)
    choice=int(input("Enter your choice: "))
    door_open=random.choice(goatdoor)                  #open door that comprises of goat

    while(door_open==choice):                        #door open shouldn't be equal to choice made by participants
        door_open=random.choice(goatdoor)
    ch=input("Do you want to swap? y/n: ")
    if(ch=='y'):
        if(doors[choice]=='Goat'):
            print("Hurrray,You Won!")
            swap=swap+1
        else:
            print("Ohh oh! You Lost")
    else:
        if(doors[choice]=="Goat"):
            print("Ohh oh! You lost")
        else:
            print("Hurray,You won!")
            dont_swap=dont_swap+1
    j=j+1
print(swap)
print(dont_swap)



#higher probablity of winning if you swap.