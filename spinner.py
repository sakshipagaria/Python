from turtle import *

state={'turn':0}
def spinner():
    clear()
    angle=state['turn']/10
    left(angle)
    forward(100)
    dot(120,'grey')
    back(100)
    left(120)
    forward(100)
    dot(120,'grey')
    back(100)
    left(120)
    forward(100)
    dot(120,'grey')
    back(100)
    left(120)
    
    update()
    
    #outerlooks of spinner are completed here
    
def animate():
    if state['turn']>0:
        state['turn']-=1
    spinner()
    ontimer(animate, 20)
    
def flick():
    state['turn']+=50          #acceleration speed value
tracer(False)
width(20)
onkey(flick,'space')
listen()
animate()
done()
    