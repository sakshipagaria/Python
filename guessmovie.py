# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 17:40:14 2022

@author: ADMIN
"""
import random
movies=['golmaal','geheraiyaan','kesari','ranjhana','jaane tu ya janne na','bhool bhulaiya','wednesday','a thrusday']
def create_question(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if letters[i]=='':
            temp.append('')
        else:
            temp.append('*')
    qn=''.join(str(x) for x in temp)
    return qn

def is_present(letter,movie):
    c=movie.count(letter)
    if (c==0):
        return False
    else:
        return True
    
def unlock(qn,movie,letter):
    ref=list(movie)
    qn_list=list(qn)
    temp=[]
    n=len(movie)
    for i in range(n):
        if ref[i]=='' or ref[i]==letter:
            temp.append(ref[i])
        else:
            if qn_list[i]=='*':
                temp.append('*')
            else:
                temp.append(ref[i])
    qn_new=''.join(str(x) for x in temp)
    return qn_new
            
    
    
def play():
    p1name=input("Player 1 Enter your name: ")
    p2name=input("Player 2 Enter your name: ")
    pp1=0
    pp2=0
    turn=0
    will=True
    while will:
        if turn%2==0:
            #player1 turn
            print(p1name,'Your turn')
            pick_movie=random.choice(movies)
            qn=create_question(pick_movie)
            print (qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letter=input("Your letter: ")
                if(is_present(letter,pick_movie)):
                    #unlock
                    modified_qn=unlock(modified_qn,pick_movie,letter)
                    print(modified_qn)
                    d=input('Press 1 to guess the movie or 2 to unlock another letter: ')
                    if (d==1):
                        ans=input("Your answer: ")
                        if ans==pick_movie:
                            pp1=pp1+1
                            print("Congrats! You are right.")
                            not_said=False
                            print(p1name,"Your score:",pp1)
                        else:
                            print("Wrong answer,try again.")
                else:
                    print(letter,"Not found")
            c=input("Press 1 to continue or 0 to quit: ")
            if(c==0):
                print(p1name,"Your score:" ,pp1)
                print(p2name,"Your score:" ,pp2)
                print("Thanks for playing!")
                will=False
                
                
        else:
            #player2 turn
            print(p2name,'Your turn')
            pick_movie=random.choice(movies)
            qn=create_question(pick_movie)
            print (qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letter=input("Your letter: ")
                if(is_present(letter,pick_movie)):
                    #unlock
                    modified_qn=unlock(modified_qn,pick_movie,letter)
                    print(modified_qn)
                    d=input('Press 1 to guess the movie or 2 to unlock another letter: ')
                    if (d==1):
                        ans=input("Your answer: ")
                        if ans==pick_movie:
                            pp1=pp1+1
                            print("Congrats! You are right.")
                            not_said=False
                            print(p1name,"Your score:",pp1)
                        else:
                            print("Wrong answer,try again.")
                else:
                    print(letter,"Not found")
            c=input("Press 1 to continue or 0 to quit: ")
            if(c==0):
                print(p1name,"Your score:" ,pp1)
                print(p2name,"Your score:" ,pp2)
                print("Thanks for playing!")
                will=False
            
        turn=turn+1
        
play()