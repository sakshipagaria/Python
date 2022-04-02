# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 17:18:04 2022

@author: ADMIN
"""

import turtle
turtle.bgcolor("black")
seurat=turtle.Turtle()
from random import randint

width=5
height=7
dot_distance=25

seurat.penup()
list_color=["violet","indigo","blue","green","yellow","orange","red"]
seurat.setpos(-250,250)


def spiralPrint(m, n):
    k=0
    l=0
    f=0
    
    seurat.color("white")
    '''
    k =starting index of row and
    l =starting index of col
    m =ending row index
    i =iterator
    n =ending col index
    '''
    col=randint(0,8)
    seurat.color(list_color[col])
    while(k<m and l<n):
        
        if(f==1):
            seurat.right(90)
        
        #print 1st row 
        for i in range(l,n):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(a[k][i], end=" ")
            
        k+=1
        f=1
        
        seurat.right(90)
        col=randint(0,8)
        seurat.color(list_color[col])
        #print last col 
        for i in range(k,m):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(a[i][n-1],end=" ")
            
        n-=1
        seurat.right(90)
        col=randint(0,8)
        seurat.color(list_color[col])
        
        if(k<m):
            
            #print  last row
            for i in range(n-1,l-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                #print(a[m-1][i],end=" ")
                
            m-=1
        seurat.right(90)
        col=randint(0,8)
        seurat.color(list_color[col])
            
        if(l<n):
            #print 1st col
            for i in range(m-1,k-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                #print(a[i][l], end=" ")
            l+=1
            
R=20;C=20      
spiralPrint(R,C)
turtle.done()
        
        
        
        
        