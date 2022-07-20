# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 17:07:48 2022

@author: pagar
"""

import turtle
turtle.title("16Petals flower")
turtle.setworldcoordinates(-2000, -2000, 2000, 2000)

def draw_flower(x,y,tilt,radius):
    #turtle.begin_fill()
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.seth(tilt-45)
    turtle.circle(radius,90)
    turtle.left(90)
    turtle.circle(radius,90)
    #turtle.end_fill()
    
for tilt in range(0,360,30):
    draw_flower(0,0,tilt,1000)
    

